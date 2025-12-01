# UP Prepaid Engine Automation - Test Case Catalog

## Overview

This catalog documents all test cases (PE_101 through PE_225) in the UP Prepaid Engine Automation framework. Each test case validates specific billing scenarios for the prepaid engine.

---

## Test Case Categories

### Category 1: Basic Scenarios (PE_101 - PE_110)

Basic prepaid ledger calculations with standard supply types.

| Test ID | Description | Supply Type | Load (kW) | Consumption | Max Demand |
|---------|-------------|-------------|-----------|-------------|------------|
| PE_101 | Basic ledger calculation - ST=10, Consumption ≤100 kWh, MD ≤75% | 10 (Normal 10A) | 1 | ≤100 kWh | ≤75% |
| PE_102 | Basic ledger calculation - ST=10, Consumption ≤100 kWh, MD ≤150% | 10 (Normal 10A) | 1 | ≤100 kWh | ≤150% |
| PE_103 | Basic ledger calculation - ST=10, Consumption >100 kWh, Variable MD | 10 (Normal 10A) | 1 | >100 kWh | Variable |
| PE_104 | Basic ledger calculation - ST=10, Consumption 101-150 kWh | 10 (Normal 10A) | 1 | 101-150 kWh | ≤75% |
| PE_105 | Basic ledger calculation - ST=10, Consumption 151-300 kWh | 10 (Normal 10A) | 1 | 151-300 kWh | ≤75% |
| PE_106 | Basic ledger calculation - ST=10, Consumption >300 kWh | 10 (Normal 10A) | 1 | >300 kWh | ≤75% |
| PE_107 | Basic ledger calculation - ST=10, Zero consumption | 10 (Normal 10A) | 1 | 0 kWh | 0% |
| PE_108 | Basic ledger calculation - ST=10, Very high consumption | 10 (Normal 10A) | 1 | >500 kWh | ≤75% |
| PE_109 | Basic ledger calculation - ST=10, Low opening balance | 10 (Normal 10A) | 1 | ≤100 kWh | ≤75% |
| PE_110 | Basic ledger calculation - ST=10, High opening balance | 10 (Normal 10A) | 1 | ≤100 kWh | ≤75% |

---

### Category 2: Max Demand Scenarios (PE_111 - PE_120)

Scenarios testing various max demand (MD) levels and fixed charge adjustments.

| Test ID | Description | Supply Type | Load (kW) | Max Demand % | Features |
|---------|-------------|-------------|-----------|--------------|----------|
| PE_111 | MD exactly at 75% of contracted load | 10 | 1 | 75% | Boundary test |
| PE_112 | MD at 76% - triggers FC adjustment | 10 | 1 | 76% | FC adjustment |
| PE_113 | MD at 100% of contracted load | 10 | 1 | 100% | Boundary test |
| PE_114 | MD at 101% - triggers EDP | 10 | 1 | 101% | EDP calculation |
| PE_115 | MD at 150% with increasing demand | 10 | 1 | 150% | Progressive MD |
| PE_116 | MD at 200% - extreme excess demand | 10 | 1 | 200% | High EDP |
| PE_117 | MD fluctuating around 75% boundary | 10 | 1 | 70-80% | FC adjustment logic |
| PE_118 | MD fluctuating around 100% boundary | 10 | 1 | 95-105% | EDP on/off |
| PE_119 | MD increasing throughout month | 10 | 1 | 50-150% | Progressive adjustment |
| PE_120 | MD constant at high level | 10 | 1 | 120% | Steady high EDP |

---

### Category 3: Life Line Switch Scenarios (PE_121 - PE_135)

Scenarios testing the life line (tariff) switch when consumption crosses thresholds.

| Test ID | Description | Consumption Pattern | Switch Day | Features |
|---------|-------------|---------------------|------------|----------|
| PE_121 | Life line switch at 100 kWh - day 10 | Low daily consumption | Day 10 | Early switch |
| PE_122 | Life line switch at 100 kWh - day 20 | Moderate consumption | Day 20 | Mid-month switch |
| PE_123 | Life line switch at 100 kWh - day 30 | High early consumption | Day 30 | Late switch |
| PE_124 | Consumption just below 100 kWh | 99.9 kWh total | Never | No switch |
| PE_125 | Consumption exactly at 100 kWh | 100 kWh total | Boundary | Boundary test |
| PE_126 | Rapid consumption increase post-switch | Normal → High | Day 15 | Rate change effect |
| PE_127 | Life line switch with MD >100% | Combined scenario | Day 12 | Switch + EDP |
| PE_128 | Life line switch with FC adjustment | Combined scenario | Day 18 | Switch + FC adj |
| PE_129 | Multiple tier crossings in single month | Rapid consumption | Days 5,15,25 | Multiple switches |
| PE_130 | Life line EC spread calculation (3 days) | Normal pattern | Day 10 | EC spread test |
| PE_131 | Life line FC spread calculation (3 days) | Normal pattern | Day 10 | FC spread test |
| PE_132 | Life line switch on last day of month | End-of-month consumption | Day 31 | Edge case |
| PE_133 | Life line switch on first day of month | High first-day consumption | Day 1 | Edge case |
| PE_134 | Life line with zero opening balance | Negative balance scenario | Day 15 | Balance edge case |
| PE_135 | Life line with negative closing balance | Depletion scenario | Day 20 | Wallet exhaustion |

---

### Category 4: Different Supply Types (PE_136 - PE_155)

Scenarios testing various supply type codes and their tariff structures.

| Test ID | Description | Supply Type | Contracted Load | Special Features |
|---------|-------------|-------------|-----------------|------------------|
| PE_136 | Supply Type 11 - Rural domestic | 11 | 1 kW | Rural tariff |
| PE_137 | Supply Type 20 - Commercial small | 20 | 2 kW | Commercial rates |
| PE_138 | Supply Type 21 - Commercial large | 21 | 5 kW | Higher load |
| PE_139 | Supply Type 30 - Industrial small | 30 | 10 kW | Industrial rates |
| PE_140 | Supply Type 31 - Industrial large | 31 | 50 kW | High capacity |
| PE_141 | Supply Type 40 - Agricultural | 40 | 3 kW | Agri subsidy |
| PE_142 | Supply Type 41 - Agricultural pump | 41 | 5 kW | Pump specific |
| PE_143 | Supply Type 50 - Government | 50 | 10 kW | Govt rates |
| PE_144 | Supply Type 60 - Street lighting | 60 | 5 kW | Public lighting |
| PE_145 | Supply Type 70 - Temporary connection | 70 | 2 kW | Temp tariff |
| PE_146 | Supply Type 10 with net metering | 10 | 3 kW | Net meter flag |
| PE_147 | Supply Type 10 with green energy | 10 | 1 kW | Green energy flag |
| PE_148 | Supply Type 10 with power loom | 10 | 2 kW | Power loom count |
| PE_149 | Supply Type 10 with seasonal load | 10 | 5 kW | Off-season benefit |
| PE_150 | Supply Type 10 with LPSC applied | 10 | 1 kW | Late payment surcharge |
| PE_151 | Multi-tariff scenario type 1 | Variable | 1 kW | Rate changes |
| PE_152 | Multi-tariff scenario type 2 | Variable | 2 kW | Rate changes |
| PE_153 | Special category - Below Poverty Line | BPL | 0.5 kW | BPL subsidy |
| PE_154 | Special category - Senior Citizen | 10 | 1 kW | Senior discount |
| PE_155 | Special category - Freedom Fighter | 10 | 1 kW | FF discount |

---

### Category 5: Balance Scenarios (PE_156 - PE_170)

Scenarios testing various opening balance and wallet conditions.

| Test ID | Description | Opening Balance | Expected Behavior |
|---------|-------------|-----------------|-------------------|
| PE_156 | Zero opening balance | ₹0 | Immediate negative |
| PE_157 | Very low opening balance | ₹100 | Quick exhaustion |
| PE_158 | Exactly covering monthly charges | ₹calculated | Zero closing |
| PE_159 | Excess opening balance | ₹50,000 | Large positive closing |
| PE_160 | Opening balance equals first day charge | ₹calculated | Zero after day 1 |
| PE_161 | Opening balance insufficient for ED | ₹calculated | Partial charges |
| PE_162 | Negative opening balance (arrears) | -₹500 | Deeper negative |
| PE_163 | Large arrears carried forward | -₹10,000 | Arrears handling |
| PE_164 | Recharge during billing period | ₹1,000 | Mid-month top-up |
| PE_165 | Multiple recharges in month | Various | Multiple top-ups |
| PE_166 | Balance sufficient until mid-month | ₹2,000 | Partial month positive |
| PE_167 | Balance exactly at warning threshold | ₹500 | Low balance warning |
| PE_168 | Balance at disconnection threshold | ₹100 | Disconnect logic |
| PE_169 | Balance recovery after negative | -₹1,000 → ₹500 | Recovery scenario |
| PE_170 | Maximum balance cap scenario | ₹100,000 | Cap handling |

---

### Category 6: Electricity Duty (ED) Scenarios (PE_171 - PE_180)

Scenarios testing electricity duty calculations.

| Test ID | Description | ED Rate | ED Applicable | Features |
|---------|-------------|---------|---------------|----------|
| PE_171 | Standard ED calculation (5%) | 5% | Yes | Basic ED |
| PE_172 | ED on EC only | 5% | Yes | EC-based ED |
| PE_173 | ED on FC only | 5% | Yes | FC-based ED |
| PE_174 | ED on EC+FC+EDP | 5% | Yes | Full ED base |
| PE_175 | ED not applicable | N/A | No | ED exemption |
| PE_176 | ED exemption for BPL | 0% | Exempt | BPL exemption |
| PE_177 | ED at higher rate (7.5%) | 7.5% | Yes | Higher ED |
| PE_178 | ED with life line rates | 5% | Yes | Pre/post switch |
| PE_179 | ED rounding scenarios | 5% | Yes | Decimal handling |
| PE_180 | ED ceiling/cap scenarios | 5% | Yes | Max ED limit |

---

### Category 7: Rebate Scenarios (PE_181 - PE_190)

Scenarios testing prepaid rebate calculations.

| Test ID | Description | Rebate Rate | Rebate Base | Features |
|---------|-------------|-------------|-------------|----------|
| PE_181 | Standard rebate calculation (2%) | 2% | EC+FC | Basic rebate |
| PE_182 | Rebate on EC only | 2% | EC | EC-based |
| PE_183 | Rebate on FC only | 2% | FC | FC-based |
| PE_184 | Rebate at higher rate (3%) | 3% | EC+FC | Higher rebate |
| PE_185 | Rebate at lower rate (1%) | 1% | EC+FC | Lower rebate |
| PE_186 | Rebate with life line switch | 2% | Variable | Pre/post switch |
| PE_187 | Rebate after EDP deduction | 2% | EC+FC | EDP excluded |
| PE_188 | Rebate ceiling/cap | 2% | EC+FC | Max rebate limit |
| PE_189 | Rebate on zero consumption | 2% | FC only | Minimum bill |
| PE_190 | Rebate rounding scenarios | 2% | EC+FC | Decimal handling |

---

### Category 8: Date/Time Scenarios (PE_191 - PE_200)

Scenarios testing various date and time-based calculations.

| Test ID | Description | Month | Days | Features |
|---------|-------------|-------|------|----------|
| PE_191 | 31-day month calculation | January | 31 | Standard month |
| PE_192 | 30-day month calculation | April | 30 | Shorter month |
| PE_193 | 28-day month (February) | February | 28 | Shortest month |
| PE_194 | 29-day month (Leap year) | February | 29 | Leap year |
| PE_195 | Mid-month connection | Any | 15 days | Partial month |
| PE_196 | Last day connection | Any | 1 day | Single day |
| PE_197 | First day disconnection | Any | 0 days | No consumption |
| PE_198 | Meter replacement mid-month | Any | Split | New meter |
| PE_199 | Time zone handling | Any | 31 | UTC conversion |
| PE_200 | Daylight saving transition | Any | 31 | DST handling |

---

### Category 9: Edge Cases (PE_201 - PE_215)

Edge cases and boundary condition testing.

| Test ID | Description | Scenario Type | Expected Behavior |
|---------|-------------|---------------|-------------------|
| PE_201 | Maximum consumption capacity | Extreme high | System limits |
| PE_202 | Minimum consumption (0.001 kWh) | Extreme low | Minimum bill |
| PE_203 | All readings as zero | No consumption | Fixed charges only |
| PE_204 | Missing daily load data | Data gaps | Estimation |
| PE_205 | Missing profile instant data | Data gaps | Default MD |
| PE_206 | Duplicate data timestamps | Data quality | Deduplication |
| PE_207 | Out-of-sequence data | Data quality | Sorting |
| PE_208 | Future dated records | Data quality | Validation |
| PE_209 | Negative consumption values | Data quality | Error handling |
| PE_210 | Extremely high MD spike | One-day anomaly | Spike handling |
| PE_211 | Null/empty meter reading | Data quality | Default values |
| PE_212 | Very long decimal values | Precision | Rounding |
| PE_213 | Special characters in data | Data quality | Sanitization |
| PE_214 | Concurrent API calls | Race condition | Locking |
| PE_215 | API timeout scenarios | Network | Retry logic |

---

### Category 10: Integration Scenarios (PE_216 - PE_225)

Integration and end-to-end scenarios.

| Test ID | Description | Components | Validation Focus |
|---------|-------------|------------|------------------|
| PE_216 | Full month billing cycle | All | End-to-end |
| PE_217 | Multi-month consecutive billing | All | Carryover |
| PE_218 | Account creation to first bill | All | Onboarding |
| PE_219 | Meter replacement scenario | All | Transition |
| PE_220 | Supply type change mid-month | All | Tariff change |
| PE_221 | Load enhancement mid-month | All | Capacity change |
| PE_222 | Connection suspension/resumption | All | Status change |
| PE_223 | Balance sync with wallet system | API | Integration |
| PE_224 | Concurrent billing and payment | API | Race condition |
| PE_225 | Complete audit trail | All | Data integrity |

---

## Test Case Configuration Reference

### Standard Configuration Parameters

```python
# Consumer Configuration
SUPPLY_TYPECODE = "10"           # Supply type code
SANCTIONED_LOAD = 1              # Contracted load in kW
LOAD_UNIT = "KW"                 # Load unit
METER_INSTALL_DATE = "2025-11-01T00:00:00"  # Installation date
NET_METER_FLAG = "N"             # Net metering flag
GREEN_ENERGY_FLAG = "N"          # Green energy flag
POWER_LOOM_COUNT = 0             # Power loom count
PREPAID_OPENING_BALANCE = 4000   # Opening balance in Rs
PREPAID_POSTPAID_FLAG = "1"      # 1=Prepaid, 0=Postpaid
ED_APPLICABLE = "1"              # 1=ED applicable, 0=Exempt

# Daily Load Configuration
END_WH = 100000                  # Target end Wh reading
MD_W = 750                       # Max demand in Watts
```

### Varying Parameters by Test Case

| Test ID | END_WH | MD_W | PREPAID_OPENING_BALANCE |
|---------|--------|------|-------------------------|
| PE_101 | 100,000 | 750 | 4,000 |
| PE_102 | 100,000 | 1,500 | 4,000 |
| PE_103 | 200,000 | 750 | 4,000 |
| PE_104 | 150,000 | 750 | 4,000 |
| PE_105 | 300,000 | 750 | 4,000 |
| PE_106 | 500,000 | 750 | 6,000 |
| PE_107 | 0 | 0 | 4,000 |
| PE_108 | 1,000,000 | 750 | 10,000 |
| PE_109 | 100,000 | 750 | 500 |
| PE_110 | 100,000 | 750 | 50,000 |

---

## Running Test Cases

### Individual Test Case

```bash
python Test_Plan/PE_101.py
```

### Batch Execution

```bash
# Run all basic scenarios
for i in {101..110}; do
    python Test_Plan/PE_$i.py
done

# Run specific category
for i in {121..135}; do
    python Test_Plan/PE_$i.py
done
```

### Validation After Test

```bash
# Extract consumer details
python account.py

# Download ledger data
python Download_Ledger.py

# Validate with formula
python Formula/Formula_101.py
```

---

## Test Results Location

| Output | Location |
|--------|----------|
| Test Reports | `Result_File/Report_PE_XXX.xlsx` |
| Logs | `logs/PE_XXX.log` |
| Consumer CSV | `Consumer_details.csv` |
| Ledger Report | `Prepaid_Ledger_Report.xlsx` |
| Formula Reports | `Formula_XXX.xlsx` |

---

## Adding New Test Cases

To add a new test case:

1. Copy an existing test case file:
   ```bash
   cp Test_Plan/PE_101.py Test_Plan/PE_226.py
   ```

2. Modify the configuration parameters:
   ```python
   # Update test case ID
   test_case_id = "PE_226"
   test_case_description = "New scenario description"
   
   # Modify parameters as needed
   SUPPLY_TYPECODE = "30"
   SANCTIONED_LOAD = 10
   END_WH = 500000
   MD_W = 8000
   ```

3. Update log file and report names:
   ```python
   logging.FileHandler('logs/PE_226.log')
   excel_file = "Result_File/Report_PE_226.xlsx"
   ```

4. Run and validate:
   ```bash
   python Test_Plan/PE_226.py
   python account.py
   python Download_Ledger.py
   ```

---

*Test Case Catalog for UP Prepaid Engine Automation Framework v1.0*
