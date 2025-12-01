# UP Prepaid Engine Automation - API Reference

## Table of Contents

1. [Overview](#overview)
2. [Core Modules](#core-modules)
   - [account.py - Consumer Details Extractor](#accountpy---consumer-details-extractor)
   - [Download_Ledger.py - Ledger Data Downloader](#download_ledgerpy---ledger-data-downloader)
3. [Formula Validation Modules](#formula-validation-modules)
   - [Formula_101 - Basic Prepaid Ledger Comparison](#formula_101---basic-prepaid-ledger-comparison)
   - [Formula_102 - Advanced with Max Demand Penalty](#formula_102---advanced-with-max-demand-penalty)
   - [Formula_103 - Tiered Rate Structure with Life Line Switch](#formula_103---tiered-rate-structure-with-life-line-switch)
4. [Test Plan Modules](#test-plan-modules)
   - [Test Case Structure (PE_101 - PE_225)](#test-case-structure-pe_101---pe_225)
   - [Incremental_Trigger - Task Trigger Utility](#incremental_trigger---task-trigger-utility)
5. [Configuration Reference](#configuration-reference)
6. [API Endpoints](#api-endpoints)
7. [Database Schema](#database-schema)

---

## Overview

The UP Prepaid Engine Automation framework provides comprehensive testing and validation tools for the Prepaid Engine billing system. It consists of three main components:

1. **Data Extraction Tools** - Extract and process consumer data from Excel reports
2. **Formula Validation** - Validate prepaid ledger calculations against expected formulas
3. **Test Plan Execution** - Automated end-to-end test cases for various billing scenarios

---

## Core Modules

### account.py - Consumer Details Extractor

**Purpose:** Reads Excel report files from the `Result_File` folder and extracts consumer details into a consolidated CSV file.

#### Configuration Constants

| Constant | Type | Default | Description |
|----------|------|---------|-------------|
| `RESULT_FOLDER` | `str` | `"Result_File"` | Folder containing Excel reports |
| `SHEET_NAME` | `str` | `"Consumer Details"` | Name of the sheet to extract |
| `OUTPUT_CSV` | `str` | `"Consumer_details.csv"` | Output CSV filename |

#### Required Columns

The following columns are extracted from each report:

```python
REQUIRED_COLUMNS = [
    "accountId",
    "meterSrno",
    "supplyTypecode",
    "sanctionedLoad",
    "loadUnit",
    "meterInstalldate",
    "greenEnergyflag",
    "prepaidOpeningbalance"
]
```

#### Functions

##### `get_report_identifier(filename: str) -> str`

Extracts the report identifier from a filename.

**Parameters:**
- `filename` (str): The Excel filename

**Returns:**
- `str`: Report identifier (filename without extension)

**Example:**
```python
>>> get_report_identifier("Report_PE_101.xlsx")
'Report_PE_101'
```

---

##### `extract_consumer_details(excel_file: str) -> pd.DataFrame`

Extracts consumer details from a single Excel file with a key-value (Parameter/Value) structure.

**Parameters:**
- `excel_file` (str): Path to the Excel file

**Returns:**
- `pd.DataFrame`: DataFrame with consumer details including report identifier

**Example:**
```python
df = extract_consumer_details("Result_File/Report_PE_101.xlsx")
print(df.columns)
# Output: ['Report_ID', 'accountId', 'meterSrno', 'supplyTypecode', ...]
```

**Behavior:**
- Handles case-insensitive parameter matching
- Returns empty DataFrame on file not found or sheet not found errors
- Logs warnings for missing parameters

---

##### `process_all_reports() -> pd.DataFrame`

Processes all Excel report files matching `Report_PE_*.xlsx` pattern in the Result_File folder.

**Returns:**
- `pd.DataFrame`: Combined DataFrame with all consumer details

**Example:**
```python
combined_df = process_all_reports()
print(f"Total records: {len(combined_df)}")
```

---

##### `save_to_csv(df: pd.DataFrame, output_file: str)`

Saves DataFrame to a CSV file with UTF-8 BOM encoding.

**Parameters:**
- `df` (pd.DataFrame): DataFrame to save
- `output_file` (str): Output CSV filename

**Example:**
```python
save_to_csv(combined_df, "Consumer_details.csv")
```

---

##### `main()`

Main entry point that orchestrates the complete extraction process.

**Usage:**
```bash
python account.py
```

**Output:**
- Creates `Consumer_details.csv` with extracted data
- Logs progress and summary to console

---

### Download_Ledger.py - Ledger Data Downloader

**Purpose:** Downloads prepaid ledger data from the API for all consumers in the CSV file and saves to Excel.

#### Configuration Constants

| Constant | Type | Default | Description |
|----------|------|---------|-------------|
| `API_URL` | `str` | `"https://engine-web.stage.gomatimvvnl.in/daily_prepaid_ledger/"` | Base API URL |
| `CSV_FILE` | `str` | `"Consumer_details.csv"` | Input CSV file |

#### Required API Fields

```python
REQUIRED_FIELDS = [
    "start_date_time", "end_date_time", "account_id", "meter_number",
    "applied_supply_type_code", "daily_consumption", "cumm_daily_consumption_mtd",
    "daily_consumption_in_rupees", "cumm_daily_consumption_rupees_mtd",
    "remaining_ec_life_line_switch_charge", "cumm_ec_life_line_switch_charge_deducted",
    "max_demand", "daily_max_demand_penalty", "cumm_daily_max_demand_penalty_mtd",
    "daily_fixed_charge_adjustment", "cumm_daily_fixed_charge_adjustment_mtd",
    "daily_fixed_charges", "cumm_daily_fixed_charges_mtd",
    "remaining_fc_life_line_switch_charge", "cumm_fc_life_line_switch_charge_deducted",
    "daily_ec_final_charge", "cumm_ec_final_charges_mtd",
    "daily_fc_final_charge", "cumm_fc_final_charges_mtd",
    "daily_ec_plus_fc_charge", "cumm_daily_ec_plus_fc_charge_mtd",
    "daily_ed_charge", "cumm_ed_charges_mtd",
    "daily_final_rebate", "cumm_daily_final_rebate_mtd",
    "daily_green_energy_consumption_in_rupees", "cumm_daily_green_energy_consumption_rupees_mtd",
    "daily_final_charge", "cumm_daily_final_charge_mtd",
    "opening_balance", "closing_balance"
]
```

#### Functions

##### `read_consumer_details() -> List[Tuple[str, str, str]]`

Reads account IDs, meter numbers, and Report IDs from the CSV file.

**Returns:**
- `List[Tuple[str, str, str]]`: List of tuples containing (report_id, account_id, meter_number)

**Example:**
```python
consumer_data = read_consumer_details()
for report_id, account_id, meter_number in consumer_data:
    print(f"Report: {report_id}, Account: {account_id}, Meter: {meter_number}")
```

---

##### `fetch_and_save_data()`

Fetches ledger data for all consumers and saves to Excel with multiple sheets.

**Output:**
- Creates `Prepaid_Ledger_Report.xlsx` with:
  - One sheet per consumer (named by Report_ID)
  - An "Errors" sheet (if any errors occurred)
  - A "Summary" sheet (if no data found)

**Example:**
```bash
python Download_Ledger.py
```

**Error Handling:**
- HTTP errors are captured with response details
- Timeouts after 30 seconds
- All errors are logged to the "Errors" sheet

---

## Formula Validation Modules

### Formula_101 - Basic Prepaid Ledger Comparison

**Purpose:** Validates basic prepaid ledger calculations for simple scenarios with fixed EC rate.

#### Class: `PrepaidLedgerComparison`

##### Configuration Parameters

```python
contracted_load = 1      # kW
fc_rate = 50             # Per kW FC Rate
ed_rate = 0.05           # 5% Electricity Duty
rebate_rate = 0.02       # 2% Rebate
opening_balance = 5000   # Initial balance
ec_rate = 3              # Fixed EC rate per kWh
days_in_month = 31       # Days in billing month
```

##### Methods

###### `__init__(self)`

Initializes the comparison with configuration parameters and API settings.

---

###### `fetch_prepaid_ledger_data(self) -> pd.DataFrame`

Fetches prepaid ledger data from the API for the configured date range.

**Returns:**
- `pd.DataFrame`: Filtered and sorted ledger data

**Example:**
```python
comparator = PrepaidLedgerComparison()
df = comparator.fetch_prepaid_ledger_data()
```

---

###### `calculate_expected_values(self, df: pd.DataFrame) -> pd.DataFrame`

Calculates expected values based on billing formulas.

**Formulas Applied:**

1. **Daily EC (Energy Charges):**
   ```
   daily_ec = daily_consumption × ec_rate
   ```

2. **Daily FC (Fixed Charges):**
   ```
   daily_fc = (0.75 × contracted_load × fc_rate) / days_in_month
   ```

3. **Daily EC + FC:**
   ```
   daily_ec_plus_fc = daily_ec + daily_fc
   ```

4. **Daily ED (Electricity Duty):**
   ```
   daily_ed = daily_ec_plus_fc × ed_rate
   ```

5. **Daily Rebate:**
   ```
   daily_rebate = daily_ec_plus_fc × rebate_rate
   ```

6. **Daily Final Charge:**
   ```
   daily_final_charge = daily_ec_plus_fc + daily_ed - daily_rebate
   ```

7. **Closing Balance:**
   ```
   closing_balance = opening_balance - daily_final_charge
   ```

**Parameters:**
- `df` (pd.DataFrame): Ledger data from API

**Returns:**
- `pd.DataFrame`: Data with expected values columns added

---

###### `compare_values(self, df: pd.DataFrame) -> pd.DataFrame`

Compares API values with calculated expected values.

**Parameters:**
- `df` (pd.DataFrame): DataFrame with actual and expected values

**Returns:**
- `pd.DataFrame`: DataFrame with Status column indicating match/mismatch

**Comparison Tolerance:** 0.01 (values within ±0.01 are considered matching)

---

###### `generate_comparison_report(self, df: pd.DataFrame, filename: str = "Formula_101.xlsx")`

Generates an Excel report with comparison results.

**Parameters:**
- `df` (pd.DataFrame): Comparison DataFrame
- `filename` (str): Output Excel filename

**Output Columns:**
- All API columns
- Expected value columns (prefixed with `expected_`)
- Status column

---

###### `run_comparison(self)`

Executes the complete comparison workflow.

**Steps:**
1. Fetch data from API
2. Calculate expected values
3. Compare values
4. Generate comparison report

**Example:**
```python
comparator = PrepaidLedgerComparison()
comparator.run_comparison()
```

---

### Formula_102 - Advanced with Max Demand Penalty

**Purpose:** Validates prepaid ledger calculations including Max Demand (MD) based FC adjustments and Excess Demand Penalty (EDP).

#### Additional Configuration Parameters

Same as Formula_101, plus advanced MD handling.

#### FC Calculation Based on Max Demand

```python
# If MD <= 75% of contracted load
daily_fc = (0.75 × contracted_load × fc_rate) / days_in_month

# If MD between 75% to 100% of contracted load
daily_fc = (fc_rate × contracted_load × (max_demand / contracted_load)) / days_in_month

# If MD > 100% of contracted load
daily_fc = (fc_rate × contracted_load × (max_demand / contracted_load)) / days_in_month
```

#### Fixed Charge Adjustment Formula

When MD > 75%:
```
fc_adjustment = ((fc_rate × contracted_load × current_day_% × (current_day - 1)) / days_in_month)
              - ((fc_rate × contracted_load × previous_day_% × (current_day - 1)) / days_in_month)
```

#### Excess Demand Penalty (EDP) Formula

When MD > 100%:
```python
excess_demand = max_demand - contracted_load
remaining_days = days_in_month - current_day + 1
new_total_penalty = excess_demand × fc_rate
daily_edp = new_total_penalty / remaining_days
```

---

### Formula_103 - Tiered Rate Structure with Life Line Switch

**Purpose:** Validates prepaid ledger calculations with tiered energy rates and life line switch functionality.

#### Tiered EC Rates

| Consumption Range | Rate (Rs/kWh) |
|-------------------|---------------|
| 0 - 100 kWh | 3.00 |
| 101 - 150 kWh | 5.50 |
| 151 - 300 kWh | 6.00 |
| > 300 kWh | 6.50 |

#### Tiered FC Rates

| Consumption Level | FC Rate (Rs/kW) |
|-------------------|-----------------|
| ≤ 100 kWh | 50 |
| > 100 kWh | 110 |

#### Life Line Switch Logic

When cumulative consumption crosses 100 kWh:

```python
# EC Life Line Switch Charge
previous_cumm_consumption = cumm_consumption - daily_consumption
total_ec_switch = (previous_cumm × 5.5) - (previous_cumm × 3.0)
daily_ec_switch = total_ec_switch / 3  # Spread over 3 days

# FC Life Line Switch Charge
days_crossed = current_day - 1
total_fc_switch = ((110 × contracted_load × days_crossed × md_ratio) / 31) 
                - ((50 × contracted_load × days_crossed × md_ratio) / 31)
daily_fc_switch = total_fc_switch / 3  # Spread over 3 days
```

---

## Test Plan Modules

### Test Case Structure (PE_101 - PE_225)

Each test case (PE_101 through PE_225) follows a consistent 5-step structure:

#### Test Case Configuration

```python
# Consumer Configuration
SUPPLY_TYPECODE = "10"           # Supply type code
SANCTIONED_LOAD = 1              # kW
LOAD_UNIT = "KW"
METER_INSTALL_DATE = "2025-11-01T00:00:00"
NET_METER_FLAG = "N"
GREEN_ENERGY_FLAG = "N"
POWER_LOOM_COUNT = 0
PREPAID_OPENING_BALANCE = 4000
PREPAID_POSTPAID_FLAG = "1"
ED_APPLICABLE = "1"

# Daily Load Configuration
END_WH = 100000                  # Target end Wh reading
MD_W = 750                       # Max demand in Watts
```

#### Test Case Matrix

| Test ID | Supply Type | Consumption | Max Demand | Special Features |
|---------|-------------|-------------|------------|------------------|
| PE_101 | 10 (Normal 10A) | Up to 100 kWh | ≤75% | Basic |
| PE_102 | 10 (Normal 10A) | Up to 100 kWh | ≤150% | With EDP |
| PE_103 | 10 (Normal 10A) | > 100 kWh | Variable | Life Line Switch |
| ... | ... | ... | ... | ... |
| PE_225 | Various | Various | Various | Various |

#### Helper Functions

##### `generate_random_number(length: int) -> str`

Generates a random numeric string of specified length.

**Parameters:**
- `length` (int): Desired length of the number string

**Returns:**
- `str`: Random numeric string

**Example:**
```python
>>> generate_random_number(10)
'4829176304'
```

---

##### `generate_random_alphanumeric(length: int) -> str`

Generates a random alphanumeric string (uppercase letters and digits).

**Parameters:**
- `length` (int): Desired length

**Returns:**
- `str`: Random alphanumeric string

---

##### `generate_consumer_name() -> str`

Generates a random consumer name from predefined first and last name lists.

**Returns:**
- `str`: Random consumer name (e.g., "John Smith")

---

##### `generate_email(consumer_name: str) -> str`

Generates an email address based on consumer name.

**Parameters:**
- `consumer_name` (str): The consumer's name

**Returns:**
- `str`: Email address

**Example:**
```python
>>> generate_email("John Smith")
'johnsmith427@example.com'
```

---

##### `generate_mobile_number() -> int`

Generates a random 10-digit mobile number.

**Returns:**
- `int`: 10-digit mobile number

---

##### `parse_install_date(date_str: str) -> str`

Parses meter install date from ISO format to standard format.

**Parameters:**
- `date_str` (str): Date string (e.g., "2025-10-01T00:00:00")

**Returns:**
- `str`: Formatted date string (e.g., "2025-10-01 00:00:00")

---

##### `get_month_end_date(start_date_str: str) -> str`

Calculates the first day of the next month from the given start date.

**Parameters:**
- `start_date_str` (str): Start date string

**Returns:**
- `str`: Month end date + 1 day

---

#### Step Functions

##### `create_account() -> Dict[str, Any]`

**Step 1:** Creates a new consumer account via the Integration API.

**Returns:**
```python
{
    'accountId': str,        # 10-digit account ID
    'meterSrno': str,        # Meter serial number (PO + last 8 digits)
    'meterInstalldate': str, # Installation date
    'badgeNumber': str,      # Badge number
    'payload': dict          # Complete API payload
}
```

**API Endpoint:** `POST https://integration1.stage.gomatimvvnl.in/initial_master_sync/`

---

##### `fill_daily_load_data(account_data: Dict) -> bool`

**Step 2:** Fills daily load data in the database for the meter.

**Parameters:**
- `account_data` (dict): Account data from Step 1

**Database Table:** `dailyload_vee_validated`

**Data Generation:**
- Generates cumulative Wh readings that reach `END_WH` by month end
- Uses random increments within min/max factors (0.3 to 1.7 of average)

---

##### `fill_profile_instant_data(account_data: Dict) -> bool`

**Step 3:** Fills profile instant data in the database.

**Parameters:**
- `account_data` (dict): Account data from Step 1

**Database Table:** `profile_instant_vee`

**Data Generation:**
- Progressive MD values reaching `MD_W` by month end

---

##### `trigger_prepaid_ledger(account_id: str) -> bool`

**Step 4:** Triggers prepaid ledger calculation APIs.

**Parameters:**
- `account_id` (str): Account ID to process

**API Endpoint:** 
```
GET https://engine-web.stage.gomatimvvnl.in/trigger_task/daily_ledger_task/{date}?wallet_balance_sync_flag=False&account_id={account_id}
```

---

##### `generate_excel_report(account_data: Dict) -> bool`

**Step 5:** Generates an Excel report with test results.

**Parameters:**
- `account_data` (dict): Account data from Step 1

**Output:** `Result_File/Report_PE_{test_id}.xlsx`

**Sheets:**
1. **Summary** - Test case ID, description, account info, status
2. **Consumer Details** - All account parameters
3. **Daily Load** - Daily load readings from MDMS API
4. **Profile Instant** - Profile instant readings from MDMS API

---

##### `fetch_daily_load_data(meter_srno: str) -> List[Dict]`

Fetches daily load data from MDMS API.

**Parameters:**
- `meter_srno` (str): Meter serial number

**Returns:**
- `List[Dict]`: List of daily load records

**API Endpoint:** `POST https://mdms-api.stage.gomatimvvnl.in/db-service/dailyloads`

---

##### `fetch_profile_instant_data(meter_srno: str) -> List[Dict]`

Fetches profile instant data from MDMS API.

**Parameters:**
- `meter_srno` (str): Meter serial number

**Returns:**
- `List[Dict]`: List of profile instant records

**API Endpoint:** `POST https://mdms-api.stage.gomatimvvnl.in/db-service/profileinstant`

---

##### `main()`

Main function that orchestrates all 5 steps.

**Usage:**
```bash
python Test_Plan/PE_101.py
```

---

### Incremental_Trigger - Task Trigger Utility

**Purpose:** Triggers the incremental task API for processing pending ledger calculations.

#### Function

##### `trigger_incremental_task() -> bool`

Triggers the incremental_task API.

**Returns:**
- `bool`: True if successful (HTTP 200), False otherwise

**API Endpoint:** `GET https://engine-web.stage.gomatimvvnl.in/trigger_task/incremental_task/`

**Example:**
```python
from Incremental_Trigger import trigger_incremental_task

if trigger_incremental_task():
    print("Incremental task triggered successfully")
else:
    print("Failed to trigger incremental task")
```

---

## Configuration Reference

### Database Configuration

```python
DB_CONFIG = {
    'host': 'db_mdms.stage.mvvnl.internal',
    'database': 'validation_rules',
    'user': 'postgres',
    'password': '****',
    'port': 5432
}
```

### API Endpoints Summary

| Service | Base URL |
|---------|----------|
| Integration API | `https://integration1.stage.gomatimvvnl.in` |
| Engine API | `https://engine-web.stage.gomatimvvnl.in` |
| MDMS API | `https://mdms-api.stage.gomatimvvnl.in/db-service` |

---

## API Endpoints

### Integration API

#### Create Account

```http
POST /initial_master_sync/
Authorization: Bearer <token>
Content-Type: application/json
```

**Request Body:**
```json
{
    "requestId": "string",
    "accountId": "string",
    "consumerName": "string",
    "supplyTypecode": "string",
    "meterSrno": "string",
    "sanctionedLoad": "number",
    "loadUnit": "string",
    "meterInstalldate": "string",
    "prepaidOpeningbalance": "number",
    ...
}
```

### Engine API

#### Trigger Daily Ledger Task

```http
GET /trigger_task/daily_ledger_task/{date}?wallet_balance_sync_flag=False&account_id={account_id}
Accept: application/json
```

#### Trigger Incremental Task

```http
GET /trigger_task/incremental_task/
Accept: application/json
```

#### Get Daily Prepaid Ledger

```http
GET /daily_prepaid_ledger/{account_id}/?meter_number={meter_number}
Accept: application/json
```

### MDMS API

#### Get Daily Loads

```http
POST /dailyloads
Content-Type: application/json

{
    "badge_numbers": ["string"],
    "page": 1,
    "limit": 100
}
```

#### Get Profile Instant

```http
POST /profileinstant
Content-Type: application/json

{
    "badge_numbers": ["string"],
    "page": 1,
    "limit": 100
}
```

---

## Database Schema

### Table: dailyload_vee_validated

| Column | Type | Description |
|--------|------|-------------|
| device_id | integer | Device ID |
| data_timestamp | timestamp | Data timestamp |
| dcu_serial | varchar | DCU serial number |
| device_identifier | varchar | Meter serial number |
| data_source | varchar | Data source (e.g., "PUSH") |
| data_type | varchar | Data type (e.g., "DLFV") |
| import_Wh | bigint | Import Wh reading |
| import_VAh | bigint | Import VAh reading |
| export_Wh | bigint | Export Wh reading |
| export_VAh | bigint | Export VAh reading |
| is_valid | boolean | Validation status |
| is_estimated | boolean | Estimation flag |
| meter_type | varchar | Meter type |

### Table: profile_instant_vee

| Column | Type | Description |
|--------|------|-------------|
| meter_id | integer | Meter ID |
| device_identifier | varchar | Meter serial number |
| data_timestamp | timestamp | Data timestamp |
| MD_W | integer | Max demand in Watts |
| MD_VA | integer | Max demand in VA |
| MD_W_datetime | timestamp | MD timestamp |
| voltage | integer | Voltage reading |
| frequency | float | Frequency reading |
| is_valid | boolean | Validation status |

---

## Error Handling

### Common Error Codes

| Error | Description | Resolution |
|-------|-------------|------------|
| HTTP 404 | Account not found | Verify account ID exists |
| HTTP 500 | Server error | Check API service status |
| Timeout | Request timeout | Retry with increased timeout |
| DB Connection Error | Cannot connect to database | Verify network and credentials |

### Logging

All modules use Python's `logging` module with the following configuration:

```python
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/{module_name}.log'),
        logging.StreamHandler()
    ]
)
```

Log files are stored in the `logs/` directory with module-specific filenames.

---

## Best Practices

1. **Always run test cases in order** - Some tests depend on previous configurations
2. **Check logs for detailed output** - All operations are logged with timestamps
3. **Verify API connectivity** - Ensure network access to all API endpoints
4. **Backup data before testing** - Test cases create real database records
5. **Review Excel reports** - Generated reports contain detailed test results

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0.0 | 2025-01-01 | Initial release |

---

*Documentation generated for UP Prepaid Engine Automation Framework*
