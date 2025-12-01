# Formula Validation Guide

## Table of Contents
- [Overview](#overview)
- [Formula Validation Architecture](#formula-validation-architecture)
- [Formula_101: Basic Validation](#formula_101-basic-validation)
- [Formula_102: Advanced Validation](#formula_102-advanced-validation)
- [Formula_103: Complete Validation](#formula_103-complete-validation)
- [Common Concepts](#common-concepts)
- [Calculation Examples](#calculation-examples)
- [Troubleshooting](#troubleshooting)

---

## Overview

Formula validation modules compare actual prepaid ledger calculations from the API with expected values calculated using documented formulas. Each module validates progressively more complex billing scenarios.

### Validation Levels

| Module | Complexity | Features |
|--------|------------|----------|
| Formula_101 | Basic | Flat rates, ≤75% MD, ≤100 kWh |
| Formula_102 | Advanced | Variable MD, penalties, adjustments |
| Formula_103 | Complete | Tiered rates, lifeline switch, all features |

### Output

All formula modules generate:
- **Excel Report** (`Formula_10X.xlsx`) with actual vs expected comparison
- **Log File** (`logs/Formula_10X.log`) with detailed calculations
- **Pass/Fail Status** based on comparison tolerance (±0.01)

---

## Formula Validation Architecture

### Common Workflow

```python
1. Initialize Configuration
   ↓
2. Fetch API Data (daily_prepaid_ledger)
   ↓
3. Calculate Expected Values (using formulas)
   ↓
4. Compare Actual vs Expected
   ↓
5. Generate Report & Log Status
```

### Configuration Parameters

All modules use these base parameters:

```python
contracted_load = 1        # kW
days_in_month = 31        # Days
tolerance = 0.01          # Comparison tolerance
```

### Date Range

Modules validate a specific date range (typically one month):

```python
start_date = "2025-10-01T00:00:00"
end_date = "2025-11-01T00:00:00"  # Exclusive
```

---

## Formula_101: Basic Validation

### Scenario

- **Supply Type**: 10 (Normal 10A)
- **Consumption**: ≤ 100 kWh monthly
- **Max Demand**: ≤ 75% of contracted load
- **Rate Structure**: Flat rates

### Configuration

```python
contracted_load = 1       # kW
fc_rate = 50              # Rs per kW
ed_rate = 0.05            # 5%
rebate_rate = 0.02        # 2%
opening_balance = 5000    # Rs
ec_rate = 3               # Rs per kWh (flat)
```

### Formulas

#### Daily Energy Charge (EC)

```
Daily EC = daily_consumption × ec_rate
```

**Example:**
```
Daily consumption = 3.2258 kWh
Daily EC = 3.2258 × 3 = 9.6774 Rs
```

#### Daily Fixed Charge (FC)

Since max demand ≤ 75%, use 75% of contracted load:

```
Daily FC = (0.75 × contracted_load × fc_rate) / days_in_month
```

**Example:**
```
Daily FC = (0.75 × 1 × 50) / 31 = 1.2097 Rs
```

#### Daily EC + FC

```
Daily EC + FC = Daily EC + Daily FC
```

**Example:**
```
Daily EC + FC = 9.6774 + 1.2097 = 10.8871 Rs
```

#### Daily Electricity Duty (ED)

```
Daily ED = (Daily EC + FC) × ed_rate
```

**Example:**
```
Daily ED = 10.8871 × 0.05 = 0.5444 Rs
```

#### Daily Rebate

```
Daily Rebate = (Daily EC + FC) × rebate_rate
```

**Example:**
```
Daily Rebate = 10.8871 × 0.02 = 0.2177 Rs
```

#### Daily Final Charge

```
Daily Final Charge = (Daily EC + FC + Daily ED) - Daily Rebate
```

**Example:**
```
Daily Final Charge = (10.8871 + 0.5444) - 0.2177 = 11.2138 Rs
```

#### Balance Calculation

```
Closing Balance = Opening Balance - Daily Final Charge
```

**Example:**
```
Day 1:
  Opening = 5000.0000 Rs
  Daily Final = 11.2138 Rs
  Closing = 5000.0000 - 11.2138 = 4988.7862 Rs

Day 2:
  Opening = 4988.7862 Rs (previous closing)
  Daily Final = 10.9876 Rs
  Closing = 4988.7862 - 10.9876 = 4977.7986 Rs
```

### Cumulative Values

All MTD (Month-To-Date) values are cumulative:

```
Cumm EC MTD (Day 1) = 9.6774
Cumm EC MTD (Day 2) = 9.6774 + 10.5432 = 20.2206
Cumm EC MTD (Day 3) = 20.2206 + 8.9123 = 29.1329
...
```

### Usage Example

```bash
python Formula/Formula_101.py
```

**Log Output:**
```
**********DAY 1 - 2025-10-01************
Daily Consumption: 3.2258 kWh
Daily EC: 3.2258 x 3 = 9.6774 Rs.
Daily FC: (0.75 x 1 x 50) / 31 = 1.2097 Rs.
Daily EC + FC: 9.6774 + 1.2097 = 10.8871 Rs.
Daily ED: 10.8871 x 0.05 = 0.5444 Rs.
Daily Rebate: 10.8871 x 0.02 = 0.2177 Rs.
Daily Final Charge: (10.8871 + 0.5444) - 0.2177 = 11.2138 Rs.
Opening Balance: 5000.0000 Rs.
Closing Balance: 5000.0000 - 11.2138 = 4988.7862 Rs.
```

---

## Formula_102: Advanced Validation

### Scenario

- **Max Demand**: Variable (can exceed 75% and 100%)
- **Fixed Charge**: Variable based on MD percentage
- **Penalties**: Excess Demand Penalty (EDP)
- **Adjustments**: Fixed Charge Adjustment

### Additional Configuration

```python
# Same as Formula_101, plus tracking variables for:
# - previous_max_demand
# - previous_max_demand_percentage
# - EDP calculation state
```

### Enhanced Formulas

#### Variable Fixed Charge (FC)

FC varies based on max demand percentage:

```python
max_demand_percentage = (max_demand / contracted_load) × 100

if max_demand_percentage <= 75:
    Daily FC = (0.75 × contracted_load × fc_rate) / days_in_month
    
elif max_demand_percentage <= 100:
    Daily FC = (fc_rate × contracted_load × (max_demand / contracted_load)) / days_in_month
    
else:  # > 100%
    Daily FC = (fc_rate × contracted_load × (max_demand / contracted_load)) / days_in_month
```

**Example (MD = 85%):**
```
max_demand = 0.85 kW
contracted_load = 1 kW
max_demand_percentage = (0.85 / 1) × 100 = 85%

Since 75% < 85% <= 100%:
Daily FC = (50 × 1 × (0.85 / 1)) / 31 = 1.3710 Rs
```

**Example (MD = 110%):**
```
max_demand = 1.10 kW
max_demand_percentage = (1.10 / 1) × 100 = 110%

Since 110% > 100%:
Daily FC = (50 × 1 × (1.10 / 1)) / 31 = 1.7742 Rs
```

#### Fixed Charge Adjustment

Applied when max demand > 75% and day > 1:

```python
if max_demand_percentage > 75 and previous_day > 0:
    current_day_percentage = max_demand / contracted_load
    
    # If previous MD <= 75%, use 0.75
    if previous_max_demand_percentage <= 75:
        previous_day_percentage = 0.75
    else:
        previous_day_percentage = previous_max_demand / contracted_load
    
    # If current MD equals previous MD, adjustment = 0
    if abs(max_demand - previous_max_demand) < 0.0001:
        FC_adjustment = 0
    else:
        current_adjustment = (fc_rate × contracted_load × current_day_percentage × (current_day - 1)) / days_in_month
        previous_adjustment = (fc_rate × contracted_load × previous_day_percentage × (current_day - 1)) / days_in_month
        FC_adjustment = current_adjustment - previous_adjustment
```

**Example:**
```
Day 3:
  Current MD = 0.90 kW (90%)
  Previous MD = 0.85 kW (85%)
  Current Day = 3
  
  current_adjustment = (50 × 1 × 0.90 × 2) / 31 = 2.9032
  previous_adjustment = (50 × 1 × 0.85 × 2) / 31 = 2.7419
  FC_adjustment = 2.9032 - 2.7419 = 0.1613 Rs
```

#### Final Fixed Charge

```
Daily FC Final = Daily FC + FC Adjustment
```

**Example:**
```
Daily FC = 1.4516 Rs
FC Adjustment = 0.1613 Rs
Daily FC Final = 1.4516 + 0.1613 = 1.6129 Rs
```

#### Excess Demand Penalty (EDP)

Applied when max demand > 100% of contracted load:

```python
if max_demand_percentage > 100:
    excess_demand = max_demand - contracted_load
    remaining_days = days_in_month - current_day + 1
    new_total_penalty = excess_demand × fc_rate
    
    if max_demand >= previous_max_demand_for_edp and previous_max_demand_for_edp > 0:
        # Max demand increased - recalculate
        edp_already_charged = cumm_daily_max_demand_penalty
        remaining_penalty = new_total_penalty - edp_already_charged
        if remaining_penalty > 0:
            daily_edp = remaining_penalty / remaining_days
        else:
            daily_edp = 0
    else:
        # First time or max demand hasn't increased
        daily_edp = new_total_penalty / remaining_days
```

**Example (First Day with MD > 100%):**
```
Day 15:
  Max demand = 1.10 kW (110%)
  Excess demand = 1.10 - 1.00 = 0.10 kW
  Remaining days = 31 - 15 + 1 = 17 days
  Total penalty = 0.10 × 50 = 5.00 Rs
  Daily EDP = 5.00 / 17 = 0.2941 Rs
```

**Example (Max Demand Increased):**
```
Day 20:
  Previous MD = 1.10 kW, New MD = 1.15 kW
  New excess = 0.15 kW
  New total penalty = 0.15 × 50 = 7.50 Rs
  EDP already charged = 0.2941 × 5 = 1.4705 Rs
  Remaining penalty = 7.50 - 1.4705 = 6.0295 Rs
  Remaining days = 31 - 20 + 1 = 12 days
  Daily EDP = 6.0295 / 12 = 0.5025 Rs
```

#### Updated Daily ED

```
Daily ED = (EC + FC_final + EDP) × ed_rate
```

**Example:**
```
Daily EC = 9.5432 Rs
Daily FC Final = 1.6129 Rs
Daily EDP = 0.2941 Rs
Daily ED = (9.5432 + 1.6129 + 0.2941) × 0.05 = 0.5725 Rs
```

#### Updated Daily Final Charge

```
Daily Final Charge = (EC + FC_final + ED + EDP) - Rebate
```

**Example:**
```
Daily Final Charge = (9.5432 + 1.6129 + 0.5725 + 0.2941) - 0.2279 = 11.7948 Rs
```

### Usage Example

```bash
python Formula/Formula_102.py
```

---

## Formula_103: Complete Validation

### Scenario

- **Tiered EC Rates**: 5 consumption slabs
- **Tiered FC Rates**: 2 rate levels
- **Lifeline Switch**: Rate change at 100 kWh
- **All Formula_102 Features**: MD penalties, adjustments, EDP

### Configuration

```python
# Tiered EC Rates
ec_rate_0 = 3      # Up to 100 kWh
ec_rate_1 = 5.5    # 0-100 kWh (after crossing 100)
ec_rate_2 = 5.5    # 101-150 kWh
ec_rate_3 = 6      # 151-300 kWh
ec_rate_4 = 6.5    # Above 301 kWh

# Tiered FC Rates
fc_rate_0 = 50     # If cumm_consumption <= 100 kWh
fc_rate_1 = 110    # If cumm_consumption > 100 kWh

# Opening balance
opening_balance = 0  # Changed from 5000
```

### Tiered Energy Charge Calculation

EC rate depends on cumulative consumption slabs:

```python
if cumm_consumption <= 100:
    rate = ec_rate_0 (3.0)
elif cumm_consumption <= 150:
    rate = ec_rate_2 (5.5)
elif cumm_consumption <= 300:
    rate = ec_rate_3 (6.0)
else:
    rate = ec_rate_4 (6.5)
```

**Important**: When consumption crosses slab boundaries, calculate proportionally.

#### Example 1: Within Single Slab

```
Day 1:
  Daily consumption = 3.2258 kWh
  Cumm consumption = 3.2258 kWh (≤ 100)
  Daily EC = 3.2258 × 3.0 = 9.6774 Rs
```

#### Example 2: Crossing 100 kWh Boundary

```
Day 5:
  Previous cumm = 97.5 kWh
  Daily consumption = 5.5 kWh
  New cumm = 103.0 kWh

Calculation:
  - From 97.5 to 100.0 = 2.5 kWh @ 3.0 = 7.50 Rs
  - From 100.0 to 103.0 = 3.0 kWh @ 5.5 = 16.50 Rs
  - Daily EC = 7.50 + 16.50 = 24.00 Rs
```

#### Example 3: Crossing Multiple Boundaries

```
Day 1 (huge consumption):
  Daily consumption = 175 kWh
  Cumm = 175 kWh

Calculation:
  - 0 to 100 = 100 kWh @ 3.0 = 300.00 Rs
  - 101 to 150 = 50 kWh @ 5.5 = 275.00 Rs
  - 151 to 175 = 25 kWh @ 6.0 = 150.00 Rs
  - Daily EC = 300.00 + 275.00 + 150.00 = 725.00 Rs
```

### Lifeline Switch Mechanism

When cumulative consumption crosses 100 kWh, lifeline switch is triggered:

#### EC Lifeline Switch Charge

```python
# Calculated once when crossing 100 kWh
previous_cumm_consumption = cumm_consumption - daily_consumption
total_ec_switch = (previous_cumm_consumption × ec_rate_1) - (previous_cumm_consumption × ec_rate_0)

# Deducted over next 3 days
daily_ec_switch = total_ec_switch / 3

# Applied for 3 days
for next 3 days:
    deduct daily_ec_switch from Daily EC
```

**Example:**
```
Day 5: Consumption crosses 100 kWh
  Previous cumm = 97.5 kWh
  total_ec_switch = (97.5 × 5.5) - (97.5 × 3.0)
                  = 536.25 - 292.50
                  = 243.75 Rs
  daily_ec_switch = 243.75 / 3 = 81.25 Rs

Day 5: Deduct 81.25 Rs
Day 6: Deduct 81.25 Rs
Day 7: Deduct 81.25 Rs
Total deducted = 243.75 Rs
```

#### FC Lifeline Switch Charge

```python
days_crossed = current_day - 1
max_demand_ratio = max_demand / contracted_load

total_fc_switch = ((fc_rate_1 × contracted_load × days_crossed × max_demand_ratio) / days_in_month) 
                - ((fc_rate_0 × contracted_load × days_crossed × max_demand_ratio) / days_in_month)

# Deducted over next 3 days
daily_fc_switch = total_fc_switch / 3
```

**Example:**
```
Day 5: Consumption crosses 100 kWh
  Days crossed = 5 - 1 = 4 days
  Max demand ratio = 0.75 (assuming MD = 0.75 kW)
  
  total_fc_switch = ((110 × 1 × 4 × 0.75) / 31) - ((50 × 1 × 4 × 0.75) / 31)
                  = (330 / 31) - (150 / 31)
                  = 10.6452 - 4.8387
                  = 5.8065 Rs
  
  daily_fc_switch = 5.8065 / 3 = 1.9355 Rs

Day 5: Deduct 1.9355 Rs
Day 6: Deduct 1.9355 Rs
Day 7: Deduct 1.9355 Rs
Total deducted = 5.8065 Rs
```

### Final Charge Calculation with Lifeline

```
Daily EC Final = Daily EC - Daily EC Lifeline Switch
Daily FC Final = (Daily FC + FC Adjustment) - Daily FC Lifeline Switch
Daily EC + FC = Daily EC Final + Daily FC Final
Daily ED = (Daily EC Final + Daily FC Final + EDP) × ed_rate
Daily Rebate = (Daily EC Final + Daily FC Final) × rebate_rate
Daily Final Charge = (Daily EC Final + Daily FC Final + Daily ED + EDP) - Daily Rebate
```

**Example (Day 5 - Lifeline triggered):**
```
Daily EC = 24.00 Rs (calculated with tiered rates)
Daily EC Lifeline = 81.25 Rs
Daily EC Final = 24.00 - 81.25 = -57.25 Rs (credit!)

Daily FC = 1.2097 Rs
Daily FC Lifeline = 1.9355 Rs
Daily FC Final = 1.2097 - 1.9355 = -0.7258 Rs (credit!)

Daily EC + FC = -57.25 + (-0.7258) = -57.9758 Rs
Daily ED = -57.9758 × 0.05 = -2.8988 Rs
Daily Rebate = -57.9758 × 0.02 = -1.1595 Rs
Daily Final = (-57.9758 + (-2.8988)) - (-1.1595) = -59.7151 Rs

Since final charge is negative, opening balance increases!
Opening = 5000.00 Rs
Closing = 5000.00 - (-59.7151) = 5059.7151 Rs
```

### Cumulative Tracking

```python
cumm_ec_life_line_switch_charge_deducted += daily_ec_lifeline
remaining_ec_life_line_switch_charge -= daily_ec_lifeline

cumm_fc_life_line_switch_charge_deducted += daily_fc_lifeline
remaining_fc_life_line_switch_charge -= daily_fc_lifeline
```

**After 3 days:**
```
cumm_ec_life_line_switch_charge_deducted = 243.75 Rs
remaining_ec_life_line_switch_charge = 0.00 Rs

cumm_fc_life_line_switch_charge_deducted = 5.8065 Rs
remaining_fc_life_line_switch_charge = 0.00 Rs
```

### Usage Example

```bash
python Formula/Formula_103.py
```

---

## Common Concepts

### Comparison Tolerance

All comparisons use ±0.01 tolerance for floating-point precision:

```python
def check_match(actual, expected):
    return abs(actual - expected) <= 0.01
```

### Status Determination

For each day:
- **"All Match"** - All columns match within tolerance
- **Column names** - Comma-separated list of mismatched columns

**Example:**
```
Day 1: All Match
Day 2: All Match
Day 3: daily_final_charge, closing_balance
Day 4: All Match
```

### Test Result

Final status based on all days:
- **PASS** - All days match (Status = "All Match")
- **FAIL** - One or more days have mismatches

### Excel Report Structure

All formula modules generate similar reports:

**Prepaid_Ledger Sheet:**
```
| start_date_time | daily_consumption | daily_consumption_in_rupees | expected_daily_consumption_in_rupees | ... | Status |
|-----------------|-------------------|-----------------------------|--------------------------------------|-----|--------|
| 2025-10-01      | 3.2258           | 9.6774                      | 9.6774                               | ... | All Match |
| 2025-10-02      | 3.1234           | 9.3702                      | 9.3702                               | ... | All Match |
```

### Logging Patterns

All modules log detailed calculations:

```
**********DAY X - YYYY-MM-DD************
Daily Consumption: X.XXXX kWh
[Detailed calculations...]
Opening Balance: XXXX.XXXX Rs.
Daily Final Charge: XX.XXXX Rs.
Closing Balance: XXXX.XXXX Rs.
```

---

## Calculation Examples

### Complete Day Calculation (Formula_101)

```
Day 1: 2025-10-01
Given:
  daily_consumption = 3.2258 kWh
  max_demand = 0.75 kW (75%)
  opening_balance = 5000.00 Rs
  
Step 1: Daily EC
  = 3.2258 × 3.0
  = 9.6774 Rs

Step 2: Daily FC
  = (0.75 × 1 × 50) / 31
  = 1.2097 Rs

Step 3: Daily EC + FC
  = 9.6774 + 1.2097
  = 10.8871 Rs

Step 4: Daily ED
  = 10.8871 × 0.05
  = 0.5444 Rs

Step 5: Daily Rebate
  = 10.8871 × 0.02
  = 0.2177 Rs

Step 6: Daily Final Charge
  = (10.8871 + 0.5444) - 0.2177
  = 11.2138 Rs

Step 7: Closing Balance
  = 5000.0000 - 11.2138
  = 4988.7862 Rs

Cumulative Values (Day 1):
  cumm_daily_consumption_mtd = 3.2258 kWh
  cumm_daily_consumption_rupees_mtd = 9.6774 Rs
  cumm_daily_fixed_charges_mtd = 1.2097 Rs
  cumm_daily_ec_plus_fc_charge_mtd = 10.8871 Rs
  cumm_ed_charges_mtd = 0.5444 Rs
  cumm_daily_final_rebate_mtd = 0.2177 Rs
  cumm_daily_final_charge_mtd = 11.2138 Rs
```

### Complete Day with EDP (Formula_102)

```
Day 15: 2025-10-15
Given:
  daily_consumption = 3.5432 kWh
  max_demand = 1.10 kW (110%)
  previous_max_demand = 0.85 kW (85%)
  opening_balance = 4750.23 Rs
  
Step 1: Daily EC
  = 3.5432 × 3.0
  = 10.6296 Rs

Step 2: Daily FC (MD = 110%)
  = (50 × 1 × 1.10) / 31
  = 1.7742 Rs

Step 3: FC Adjustment (MD increased from 85% to 110%)
  current = (50 × 1 × 1.10 × 14) / 31 = 24.8387
  previous = (50 × 1 × 0.85 × 14) / 31 = 19.1935
  adjustment = 24.8387 - 19.1935 = 5.6452 Rs

Step 4: Daily FC Final
  = 1.7742 + 5.6452
  = 7.4194 Rs

Step 5: Daily EDP (MD = 110%, first day > 100%)
  excess = 1.10 - 1.00 = 0.10 kW
  remaining_days = 31 - 15 + 1 = 17 days
  total_penalty = 0.10 × 50 = 5.00 Rs
  daily_edp = 5.00 / 17 = 0.2941 Rs

Step 6: Daily EC + FC
  = 10.6296 + 7.4194
  = 18.0490 Rs

Step 7: Daily ED
  = (10.6296 + 7.4194 + 0.2941) × 0.05
  = 0.9072 Rs

Step 8: Daily Rebate
  = 18.0490 × 0.02
  = 0.3610 Rs

Step 9: Daily Final Charge
  = (18.0490 + 0.9072 + 0.2941) - 0.3610
  = 18.8893 Rs

Step 10: Closing Balance
  = 4750.23 - 18.8893
  = 4731.3407 Rs
```

### Complete Day with Lifeline (Formula_103)

```
Day 5: 2025-10-05
Given:
  Previous cumm = 97.5 kWh
  daily_consumption = 5.5 kWh
  New cumm = 103.0 kWh (crosses 100!)
  max_demand = 0.75 kW (75%)
  opening_balance = 4950.00 Rs
  
Lifeline Triggered!

Step 1: Calculate Tiered EC
  From 97.5 to 100.0 = 2.5 kWh @ 3.0 = 7.50 Rs
  From 100.0 to 103.0 = 3.0 kWh @ 5.5 = 16.50 Rs
  Daily EC = 24.00 Rs

Step 2: Calculate EC Lifeline Switch
  total_ec_switch = (97.5 × 5.5) - (97.5 × 3.0)
                  = 536.25 - 292.50 = 243.75 Rs
  daily_ec_switch = 243.75 / 3 = 81.25 Rs

Step 3: Daily EC Final
  = 24.00 - 81.25
  = -57.25 Rs (credit!)

Step 4: Calculate FC (now using fc_rate_1 = 110)
  = (0.75 × 1 × 110) / 31
  = 2.6613 Rs

Step 5: Calculate FC Lifeline Switch
  days_crossed = 4
  total_fc_switch = ((110 × 1 × 4 × 0.75) / 31) - ((50 × 1 × 4 × 0.75) / 31)
                  = 10.6452 - 4.8387 = 5.8065 Rs
  daily_fc_switch = 5.8065 / 3 = 1.9355 Rs

Step 6: Daily FC Final
  = 2.6613 - 1.9355
  = 0.7258 Rs

Step 7: Daily EC + FC
  = -57.25 + 0.7258
  = -56.5242 Rs

Step 8: Daily ED
  = -56.5242 × 0.05
  = -2.8262 Rs

Step 9: Daily Rebate
  = -56.5242 × 0.02
  = -1.1305 Rs

Step 10: Daily Final Charge
  = (-56.5242 + (-2.8262)) - (-1.1305)
  = -58.2199 Rs (credit!)

Step 11: Closing Balance
  = 4950.00 - (-58.2199)
  = 5008.2199 Rs (balance increased!)
```

---

## Troubleshooting

### Common Issues

#### 1. "No data fetched from API"

**Causes:**
- Invalid account ID or API URL
- Date range has no data
- API is down or network issue

**Solutions:**
- Verify API URL and account ID in code
- Check date range matches available data
- Test API manually with curl or browser
- Check network connectivity

#### 2. "All values showing mismatch"

**Causes:**
- Wrong formula parameters (rates, load)
- Date range mismatch
- API data format changed

**Solutions:**
- Verify all configuration parameters match test case
- Ensure date range exactly matches API filter
- Check API response structure

#### 3. "Cumulative values don't match"

**Causes:**
- Rounding errors accumulating
- Initial value mismatch
- Missing data for some days

**Solutions:**
- Check opening balance matches
- Verify all days present in dataset
- Review rounding logic (should round to 4 decimals)

#### 4. "Lifeline switch not triggering (Formula_103)"

**Causes:**
- Consumption never crosses 100 kWh
- Lifeline logic bug
- Wrong cumulative calculation

**Solutions:**
- Verify cumulative consumption crosses 100
- Check switch trigger condition
- Review cumulative consumption logic

#### 5. "EDP calculations wrong (Formula_102/103)"

**Causes:**
- Max demand tracking incorrect
- Remaining days calculation wrong
- Previous EDP not considered

**Solutions:**
- Verify max demand values each day
- Check current_day and days_in_month
- Review EDP recalculation logic when MD increases

### Debug Tips

1. **Enable detailed logging:**
```python
logger.setLevel(logging.DEBUG)
```

2. **Check specific day:**
```python
# Add print statements in calculate_expected_values()
if idx == 4:  # Day 5
    print(f"DEBUG: cumm_consumption = {cumm_daily_consumption}")
    print(f"DEBUG: lifeline_triggered = {life_line_switch_triggered}")
```

3. **Compare Excel columns:**
- Open generated Excel file
- Look for mismatched rows (Status != "All Match")
- Compare actual vs expected columns side-by-side
- Calculate manually to verify

4. **Check tolerance:**
```python
# Adjust tolerance if needed (but 0.01 should be sufficient)
tolerance = 0.1  # More lenient
```

5. **Verify data types:**
```python
# Ensure numeric values are float, not string
df['daily_consumption'] = pd.to_numeric(df['daily_consumption'])
```

---

## Best Practices

### 1. Run in Sequence

```bash
# Always validate in order
python Formula/Formula_101.py  # First
python Formula/Formula_102.py  # Then
python Formula/Formula_103.py  # Finally
```

### 2. Check Logs First

```bash
# Check for errors and status
tail -20 logs/Formula_101.log
grep "Test Case Result" logs/Formula_101.log
```

### 3. Validate Configuration

```python
# Before running, verify:
print(f"API URL: {comparator.api_url}")
print(f"Date Range: {comparator.start_date} to {comparator.end_date}")
print(f"EC Rate: {comparator.ec_rate}")
print(f"FC Rate: {comparator.fc_rate}")
```

### 4. Manual Spot Check

- Pick a random day from Excel report
- Manually calculate using formulas
- Compare with both actual and expected
- Should match within ±0.01

### 5. Understand the Formulas

- Read the formula documentation
- Work through calculation examples
- Understand when each formula applies
- Know the edge cases (lifeline, EDP, etc.)

---

## Summary

| Formula | Best For | Key Features |
|---------|----------|--------------|
| 101 | Basic validation | Flat rates, simple calculations |
| 102 | Variable MD | Penalties, adjustments, EDP |
| 103 | Complete testing | Tiers, lifeline, all features |

All formulas:
- Fetch data from API
- Calculate expected values
- Compare with tolerance
- Generate Excel report
- Log detailed results
- Return PASS/FAIL status

For more information:
- See [API Documentation](API_DOCUMENTATION.md) for function details
- See [Test Plan Guide](TEST_PLAN_GUIDE.md) for test execution
- See [Examples](EXAMPLES.md) for code examples

