# UP Prepaid Engine - Formula Reference

This document provides a comprehensive reference of all billing formulas used in the UP Prepaid Engine. These formulas are used for calculating daily charges, cumulative values, and wallet balance updates.

---

## Table of Contents

1. [Energy Charges (EC)](#energy-charges-ec)
2. [Fixed Charges (FC)](#fixed-charges-fc)
3. [Max Demand Calculations](#max-demand-calculations)
4. [Electricity Duty (ED)](#electricity-duty-ed)
5. [Rebate Calculation](#rebate-calculation)
6. [Final Charge Calculation](#final-charge-calculation)
7. [Balance Calculations](#balance-calculations)
8. [Life Line Switch Calculations](#life-line-switch-calculations)
9. [Green Energy Charges](#green-energy-charges)
10. [Cumulative Values](#cumulative-values)

---

## Energy Charges (EC)

### Basic EC Calculation

For simple tariff structures with a single rate:

```
Daily EC = Daily Consumption (kWh) × EC Rate (Rs/kWh)
```

**Example:**
```
Daily Consumption = 3.2258 kWh
EC Rate = 3 Rs/kWh
Daily EC = 3.2258 × 3 = 9.6774 Rs
```

### Tiered EC Calculation

For tariff structures with consumption-based slabs:

| Consumption Slab | EC Rate |
|------------------|---------|
| 0 - 100 kWh | Rs 3.00/kWh |
| 101 - 150 kWh | Rs 5.50/kWh |
| 151 - 300 kWh | Rs 6.00/kWh |
| > 300 kWh | Rs 6.50/kWh |

**Formula for slab crossing:**

```python
# When cumulative consumption spans multiple slabs
if cumm_consumption <= 100:
    daily_ec = daily_consumption × 3.0
    
elif cumm_consumption <= 150:
    if (cumm_consumption - daily_consumption) < 100:
        # Crosses 100 kWh boundary today
        consumption_in_0_100 = 100 - (cumm_consumption - daily_consumption)
        consumption_in_101_150 = daily_consumption - consumption_in_0_100
        daily_ec = (consumption_in_0_100 × 3.0) + (consumption_in_101_150 × 5.5)
    else:
        daily_ec = daily_consumption × 5.5
        
elif cumm_consumption <= 300:
    # Similar logic for 150-300 range
    # ...
    
else:
    # Above 300 kWh
    daily_ec = daily_consumption × 6.5
```

**Example - Crossing 100 kWh:**
```
Previous cumulative = 95 kWh
Daily consumption = 10 kWh
New cumulative = 105 kWh

Consumption in 0-100 slab = 100 - 95 = 5 kWh @ Rs 3.00 = Rs 15.00
Consumption in 101-150 slab = 10 - 5 = 5 kWh @ Rs 5.50 = Rs 27.50
Total Daily EC = Rs 42.50
```

---

## Fixed Charges (FC)

### Basic FC Calculation

FC is calculated based on contracted load and varies with max demand utilization:

#### Case 1: MD ≤ 75% of Contracted Load

```
Daily FC = (0.75 × Contracted Load × FC Rate) ÷ Days in Month
```

**Example:**
```
Contracted Load = 1 kW
FC Rate = 50 Rs/kW
Days in Month = 31
Daily FC = (0.75 × 1 × 50) ÷ 31 = 1.2097 Rs
```

#### Case 2: MD between 75% and 100% of Contracted Load

```
Daily FC = (FC Rate × Contracted Load × (Max Demand ÷ Contracted Load)) ÷ Days in Month
```

**Example:**
```
Contracted Load = 1 kW
Max Demand = 0.85 kW (85%)
FC Rate = 50 Rs/kW
Days in Month = 31
Daily FC = (50 × 1 × (0.85 ÷ 1)) ÷ 31 = 1.3710 Rs
```

#### Case 3: MD > 100% of Contracted Load

```
Daily FC = (FC Rate × Contracted Load × (Max Demand ÷ Contracted Load)) ÷ Days in Month
```

**Example:**
```
Contracted Load = 1 kW
Max Demand = 1.5 kW (150%)
FC Rate = 50 Rs/kW
Days in Month = 31
Daily FC = (50 × 1 × (1.5 ÷ 1)) ÷ 31 = 2.4194 Rs
```

### FC with Tiered Rates

FC rates change when consumption crosses thresholds:

| Consumption Level | FC Rate |
|-------------------|---------|
| ≤ 100 kWh | Rs 50/kW |
| > 100 kWh | Rs 110/kW |

---

## Max Demand Calculations

### Max Demand Percentage

```
MD Percentage = (Max Demand ÷ Contracted Load) × 100
```

### Fixed Charge Adjustment

When MD exceeds 75%, adjustment is needed for previous days in the month:

```
FC Adjustment = ((FC Rate × Contracted Load × Current Day % × (Current Day - 1)) ÷ Days in Month)
              - ((FC Rate × Contracted Load × Previous Day % × (Current Day - 1)) ÷ Days in Month)
```

**Example:**
```
Current Day = 10
Current MD = 0.90 kW (90%)
Previous MD = 0.75 kW (75%)
FC Rate = 50 Rs/kW
Contracted Load = 1 kW
Days in Month = 31

Current Adjustment = (50 × 1 × 0.90 × 9) ÷ 31 = 13.0645 Rs
Previous Adjustment = (50 × 1 × 0.75 × 9) ÷ 31 = 10.8871 Rs
FC Adjustment = 13.0645 - 10.8871 = 2.1774 Rs
```

### Excess Demand Penalty (EDP)

When MD > 100% of contracted load:

```
Excess Demand = Max Demand - Contracted Load
Remaining Days = Days in Month - Current Day + 1
Total Penalty = Excess Demand × FC Rate
Daily EDP = Total Penalty ÷ Remaining Days
```

**Example:**
```
Max Demand = 1.5 kW
Contracted Load = 1 kW
Excess Demand = 1.5 - 1 = 0.5 kW
FC Rate = 50 Rs/kW
Current Day = 15
Remaining Days = 31 - 15 + 1 = 17

Total Penalty = 0.5 × 50 = 25 Rs
Daily EDP = 25 ÷ 17 = 1.4706 Rs
```

#### EDP Recalculation on MD Increase

When MD increases after EDP has already been charged:

```
New Total Penalty = New Excess Demand × FC Rate
EDP Already Charged = Previous Cumulative EDP
Remaining Penalty = New Total Penalty - EDP Already Charged
New Daily EDP = Remaining Penalty ÷ Remaining Days
```

---

## Electricity Duty (ED)

### Standard ED Calculation

```
Daily ED = (Daily EC + Daily FC Final + Daily EDP) × ED Rate
```

**Example:**
```
Daily EC = 10 Rs
Daily FC Final = 2 Rs
Daily EDP = 0 Rs
ED Rate = 5%
Daily ED = (10 + 2 + 0) × 0.05 = 0.60 Rs
```

### ED Base Components

| Component | Included in ED Base |
|-----------|-------------------|
| Energy Charges (EC) | ✓ |
| Fixed Charges (FC) | ✓ |
| FC Adjustment | ✓ |
| Excess Demand Penalty | ✓ |
| Rebate | ✗ |

---

## Rebate Calculation

### Standard Rebate

```
Daily Rebate = (Daily EC Final + Daily FC Final) × Rebate Rate
```

**Example:**
```
Daily EC Final = 10 Rs
Daily FC Final = 2 Rs
Rebate Rate = 2%
Daily Rebate = (10 + 2) × 0.02 = 0.24 Rs
```

**Note:** Rebate is calculated on EC + FC before ED, and is applied after ED.

---

## Final Charge Calculation

### Complete Formula

```
Daily Final Charge = Daily EC Final + Daily FC Final + Daily ED + Daily EDP - Daily Rebate
```

### Expanded Formula

```
Daily Final Charge = (EC + FC + FC Adjustment - Life Line EC Switch - Life Line FC Switch)
                   + (ED on EC + FC + EDP)
                   + EDP
                   - Rebate
```

**Example:**
```
Daily EC Final = 10.00 Rs
Daily FC Final = 1.50 Rs
Daily ED = 0.60 Rs
Daily EDP = 0.00 Rs
Daily Rebate = 0.23 Rs

Daily Final Charge = 10.00 + 1.50 + 0.60 + 0.00 - 0.23 = 11.87 Rs
```

---

## Balance Calculations

### Opening Balance

```
Opening Balance (Day N) = Closing Balance (Day N-1)
Opening Balance (Day 1) = Prepaid Opening Balance
```

### Closing Balance

```
Closing Balance = Opening Balance - Daily Final Charge
```

**Example:**
```
Opening Balance = 5000.00 Rs
Daily Final Charge = 11.87 Rs
Closing Balance = 5000.00 - 11.87 = 4988.13 Rs
```

---

## Life Line Switch Calculations

When consumption crosses 100 kWh, the tariff switches from "Life Line" to regular rates. This requires adjustment for previously charged amounts.

### EC Life Line Switch Charge

```
Previous Cumulative Consumption = Cumm Consumption - Daily Consumption
Total EC Switch Charge = (Previous Cumm Consumption × Higher Rate) 
                       - (Previous Cumm Consumption × Lower Rate)
Daily EC Switch Charge = Total EC Switch Charge ÷ 3  (spread over 3 days)
```

**Example:**
```
Previous Cumulative = 95 kWh
Lower Rate = Rs 3.00/kWh
Higher Rate = Rs 5.50/kWh

Total EC Switch = (95 × 5.50) - (95 × 3.00)
                = 522.50 - 285.00
                = 237.50 Rs

Daily EC Switch Charge = 237.50 ÷ 3 = 79.17 Rs (for 3 days)
```

### FC Life Line Switch Charge

```
Days Before Switch = Current Day - 1
MD Ratio = Max Demand ÷ Contracted Load

Total FC Switch = ((Higher FC Rate × Load × Days Before × MD Ratio) ÷ Days in Month)
                - ((Lower FC Rate × Load × Days Before × MD Ratio) ÷ Days in Month)
                
Daily FC Switch Charge = Total FC Switch ÷ 3
```

**Example:**
```
Days Before Switch = 9 (switch on day 10)
MD Ratio = 0.75
Lower FC Rate = 50 Rs/kW
Higher FC Rate = 110 Rs/kW
Contracted Load = 1 kW
Days in Month = 31

Total FC Switch = ((110 × 1 × 9 × 0.75) ÷ 31) - ((50 × 1 × 9 × 0.75) ÷ 31)
                = 23.87 - 10.85
                = 13.02 Rs
                
Daily FC Switch Charge = 13.02 ÷ 3 = 4.34 Rs (for 3 days)
```

### Final Charges with Life Line Switch

```
Daily EC Final = Daily EC - Daily EC Life Line Switch Charge
Daily FC Final = Daily FC + FC Adjustment - Daily FC Life Line Switch Charge
```

---

## Green Energy Charges

When green energy flag is enabled:

```
Green Energy Charge = Daily Consumption × Green Energy Rate
```

---

## Cumulative Values

All daily values have corresponding month-to-date (MTD) cumulative values:

```
Cumm Daily Consumption MTD = Sum of all daily consumptions in month
Cumm Daily EC MTD = Sum of all daily EC in month
Cumm Daily FC MTD = Sum of all daily FC in month
Cumm Daily ED MTD = Sum of all daily ED in month
Cumm Daily Rebate MTD = Sum of all daily rebates in month
Cumm Daily Final Charge MTD = Sum of all daily final charges in month
Cumm Daily EDP MTD = Sum of all daily EDP in month
```

---

## Complete Calculation Flow

```
For each day in billing period:

1. Calculate Daily EC based on consumption and applicable rate
2. Calculate MD Percentage = (MD ÷ Contracted Load) × 100

3. If MD% ≤ 75%:
      Daily FC = (0.75 × Load × FC Rate) ÷ Days
   Else:
      Daily FC = (Load × FC Rate × MD%) ÷ Days
      
4. If MD% > 75% and not first day:
      Calculate FC Adjustment
      
5. If MD% > 100%:
      Calculate Daily EDP
      
6. If cumulative consumption crosses 100 kWh (first time):
      Calculate EC Life Line Switch Charge
      Calculate FC Life Line Switch Charge
      
7. Apply Life Line adjustments for 3 days after switch

8. Daily EC Final = Daily EC - EC Switch Charge (if applicable)
   Daily FC Final = Daily FC + FC Adjustment - FC Switch Charge (if applicable)
   
9. Daily ED = (EC Final + FC Final + EDP) × ED Rate

10. Daily Rebate = (EC Final + FC Final) × Rebate Rate

11. Daily Final Charge = EC Final + FC Final + ED + EDP - Rebate

12. Closing Balance = Opening Balance - Daily Final Charge

13. Update all cumulative values
```

---

## Tolerance for Validation

When comparing calculated vs actual values, a tolerance of **0.01** (1 paisa) is used:

```python
def check_match(actual, expected):
    return abs(actual - expected) <= 0.01
```

---

## Summary of Rates

| Charge Type | Parameter | Value |
|-------------|-----------|-------|
| EC Rate (Basic) | ec_rate | Rs 3.00/kWh |
| EC Rate (101-150) | ec_rate_2 | Rs 5.50/kWh |
| EC Rate (151-300) | ec_rate_3 | Rs 6.00/kWh |
| EC Rate (>300) | ec_rate_4 | Rs 6.50/kWh |
| FC Rate (≤100 kWh) | fc_rate_0 | Rs 50/kW |
| FC Rate (>100 kWh) | fc_rate_1 | Rs 110/kW |
| ED Rate | ed_rate | 5% |
| Rebate Rate | rebate_rate | 2% |

---

*Formula Reference for UP Prepaid Engine v1.0*
