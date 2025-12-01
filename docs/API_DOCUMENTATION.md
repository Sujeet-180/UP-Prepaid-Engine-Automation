# API Documentation

## Table of Contents
- [Overview](#overview)
- [Core Modules](#core-modules)
  - [account.py](#accountpy)
  - [Download_Ledger.py](#download_ledgerpy)
- [Formula Validation](#formula-validation)
  - [Formula_101.py](#formula_101py)
  - [Formula_102.py](#formula_102py)
  - [Formula_103.py](#formula_103py)
- [Test Plan Modules](#test-plan-modules)
  - [PE_101.py](#pe_101py)
  - [Incremental_Trigger.py](#incremental_triggerpy)

---

## Overview

This document provides comprehensive API documentation for the UP Prepaid Engine Automation Testing Framework. The framework consists of core utility modules, formula validation scripts, and test plan execution modules.

---

## Core Modules

### account.py

Extract consumer details from Excel reports and consolidate them into a CSV file.

#### Module Configuration

```python
RESULT_FOLDER = "Result_File"
SHEET_NAME = "Consumer Details"
OUTPUT_CSV = "Consumer_details.csv"
```

#### Required Columns

The module extracts the following consumer information:
- `accountId` - Account identifier
- `meterSrno` - Meter serial number
- `supplyTypecode` - Supply type code
- `sanctionedLoad` - Sanctioned load value
- `loadUnit` - Unit of load measurement
- `meterInstalldate` - Meter installation date
- `greenEnergyflag` - Green energy flag
- `prepaidOpeningbalance` - Prepaid opening balance

#### Public Functions

##### `get_report_identifier(filename: str) -> str`

Extract report identifier from filename.

**Parameters:**
- `filename` (str): Name of the Excel file

**Returns:**
- str: Report identifier (e.g., "Report_PE_101")

**Example:**
```python
identifier = get_report_identifier("Report_PE_101.xlsx")
# Returns: "Report_PE_101"
```

---

##### `extract_consumer_details(excel_file: str) -> pd.DataFrame`

Extract consumer details from a single Excel file with Parameter/Value structure.

**Parameters:**
- `excel_file` (str): Path to the Excel file

**Returns:**
- pd.DataFrame: DataFrame containing consumer details with Report_ID

**Example:**
```python
import pandas as pd

df = extract_consumer_details("Result_File/Report_PE_101.xlsx")
print(df.columns)
# ['Report_ID', 'accountId', 'meterSrno', 'supplyTypecode', ...]
```

**Features:**
- Case-insensitive parameter matching
- Handles missing parameters with None values
- Warning messages for missing or unexpected data

---

##### `process_all_reports() -> pd.DataFrame`

Process all Excel report files in the Result_File folder.

**Returns:**
- pd.DataFrame: Combined DataFrame with all consumer details

**Example:**
```python
combined_df = process_all_reports()
print(f"Total records: {len(combined_df)}")
```

**Features:**
- Automatically finds all `Report_PE_*.xlsx` files
- Sorts files for consistent processing
- Progress logging for each file
- Error handling for individual files

---

##### `save_to_csv(df: pd.DataFrame, output_file: str)`

Save DataFrame to CSV file with UTF-8 encoding.

**Parameters:**
- `df` (pd.DataFrame): DataFrame to save
- `output_file` (str): Output CSV filename

**Example:**
```python
save_to_csv(df, "Consumer_details.csv")
```

**Features:**
- UTF-8-sig encoding for Excel compatibility
- No index column
- Logs column names and file path

---

##### `main()`

Main entry point that orchestrates the extraction process.

**Example:**
```python
if __name__ == "__main__":
    main()
```

**Process Flow:**
1. Prints header banner
2. Processes all Excel reports
3. Saves combined data to CSV
4. Displays summary statistics

---

### Download_Ledger.py

Download prepaid ledger data from API for multiple consumers and save to Excel.

#### Module Configuration

```python
API_URL = "https://engine-web.stage.gomatimvvnl.in/daily_prepaid_ledger/"
CSV_FILE = "Consumer_details.csv"
```

#### Required Fields

The module fetches the following ledger data:
- `start_date_time`, `end_date_time` - Time period
- `account_id`, `meter_number` - Consumer identifiers
- `daily_consumption`, `cumm_daily_consumption_mtd` - Consumption metrics
- `daily_consumption_in_rupees`, `cumm_daily_consumption_rupees_mtd` - Cost metrics
- `daily_fixed_charges`, `cumm_daily_fixed_charges_mtd` - Fixed charges
- `daily_ec_plus_fc_charge`, `cumm_daily_ec_plus_fc_charge_mtd` - Combined charges
- `daily_ed_charge`, `cumm_ed_charges_mtd` - Electricity duty
- `daily_final_rebate`, `cumm_daily_final_rebate_mtd` - Rebates
- `daily_final_charge`, `cumm_daily_final_charge_mtd` - Final charges
- `opening_balance`, `closing_balance` - Balance tracking
- And many more (see REQUIRED_FIELDS in code)

#### Public Functions

##### `read_consumer_details() -> List[Tuple[str, str, str]]`

Read account IDs, meter numbers, and Report IDs from CSV file.

**Returns:**
- List[Tuple[str, str, str]]: List of (report_id, account_id, meter_number) tuples

**Example:**
```python
consumers = read_consumer_details()
for report_id, account_id, meter_number in consumers:
    print(f"{report_id}: {account_id} - {meter_number}")
```

**Features:**
- Preserves leading zeros in account IDs and meter numbers
- Validates required columns exist
- Filters out empty/invalid rows
- Generates Report_ID if not present

---

##### `fetch_and_save_data()`

Fetch data from API for all consumers and save to Excel with error tracking.

**Example:**
```python
fetch_and_save_data()
```

**Process Flow:**
1. Reads consumer details from CSV
2. Creates Excel file with timestamp
3. For each consumer:
   - Fetches data from API
   - Creates separate sheet with Report_ID as name
   - Logs errors to separate "Errors" sheet
4. Saves consolidated Excel file

**Features:**
- Timeout handling (30 seconds per request)
- Comprehensive error logging with API responses
- Sheet naming using Report_ID (truncated to 31 chars)
- Progress indicators
- Summary statistics

**Error Handling:**
- HTTP errors (404, 500, etc.)
- Timeouts
- Request exceptions
- Empty data responses

**Output:**
- Excel file: `Prepaid_Ledger_Report.xlsx`
- Sheets: One per consumer + "Errors" sheet (if any)
- Summary sheet (if no data found)

---

## Formula Validation

### Formula_101.py

Basic prepaid ledger validation with flat rates (ST = 10, consumption ≤ 100 kWh, MD ≤ 75%).

#### Class: PrepaidLedgerComparison

Main class for comparing actual vs expected ledger calculations.

##### Configuration Parameters

```python
contracted_load = 1  # kW
fc_rate = 50  # Per kW FC Rate
ed_rate = 0.05  # 5%
rebate_rate = 0.02  # 2%
opening_balance = 5000
ec_rate = 3  # Fixed EC rate
days_in_month = 31
```

##### Constructor: `__init__()`

Initialize the comparison engine with test configuration.

**Example:**
```python
comparator = PrepaidLedgerComparison()
```

**Configuration:**
- API URL, date range, and account ID
- Required columns from API
- Comparison columns
- Logging setup

---

##### `fetch_prepaid_ledger_data() -> pd.DataFrame`

Fetch prepaid ledger data from API and filter by date range.

**Returns:**
- pd.DataFrame: Filtered and sorted ledger data

**Example:**
```python
df = comparator.fetch_prepaid_ledger_data()
print(f"Fetched {len(df)} records")
```

**Features:**
- UTC timestamp handling
- Date range filtering (start inclusive, end exclusive)
- Automatic sorting by start_date_time
- Error handling with empty DataFrame return

---

##### `calculate_expected_values(df: pd.DataFrame) -> pd.DataFrame`

Calculate expected values based on formulas for basic flat-rate scenario.

**Parameters:**
- `df` (pd.DataFrame): DataFrame with actual API data

**Returns:**
- pd.DataFrame: Original data plus expected value columns

**Formulas:**
- **Daily EC** = daily_consumption × ec_rate
- **Daily FC** = (0.75 × contracted_load × fc_rate) / days_in_month
- **Daily EC + FC** = Daily EC + Daily FC
- **Daily ED** = (Daily EC + FC) × ed_rate
- **Daily Rebate** = (Daily EC + FC) × rebate_rate
- **Daily Final Charge** = (EC + FC + ED) - Rebate
- **Closing Balance** = Opening Balance - Daily Final Charge

**Example:**
```python
df_with_expected = comparator.calculate_expected_values(df)
print(df_with_expected[['daily_final_charge', 'expected_daily_final_charge']])
```

**Features:**
- Day-by-day calculation with logging
- Running balance tracking
- Cumulative value calculation
- 4 decimal place precision

---

##### `compare_values(df: pd.DataFrame) -> pd.DataFrame`

Compare actual vs expected values with tolerance.

**Parameters:**
- `df` (pd.DataFrame): DataFrame with both actual and expected values

**Returns:**
- pd.DataFrame: Original data plus comparison status columns

**Tolerance:** ±0.01 for floating-point comparison

**Example:**
```python
df_comparison = comparator.compare_values(df_with_expected)
all_match = df_comparison[df_comparison['Status'] == 'All Match']
print(f"Matching records: {len(all_match)}")
```

**Status Values:**
- `"All Match"` - All fields match within tolerance
- Comma-separated list of mismatched columns

---

##### `generate_comparison_report(df: pd.DataFrame, filename: str = "Formula_101.xlsx")`

Generate comprehensive Excel report with comparison results.

**Parameters:**
- `df` (pd.DataFrame): Comparison DataFrame
- `filename` (str): Output Excel filename

**Example:**
```python
comparator.generate_comparison_report(df_comparison, "Formula_101.xlsx")
```

**Report Contents:**
- Sheet: "Prepaid_Ledger"
  - Actual vs Expected columns side-by-side
  - Status column showing match/mismatch
  - Formatted dates and numeric values
  - All comparison data

**Features:**
- 4 decimal place formatting for numbers
- Date/time formatting (YYYY-MM-DD HH:MM:SS)
- Test status logging (PASS/FAIL)
- Success rate calculation
- Detailed mismatch analysis

---

##### `run_comparison()`

Execute the complete comparison workflow.

**Example:**
```python
comparator = PrepaidLedgerComparison()
comparator.run_comparison()
```

**Process Flow:**
1. Fetch data from API
2. Calculate expected values
3. Compare values
4. Generate Excel report
5. Log final test status

**Output:**
- Excel file: `Formula_101.xlsx`
- Log file: `logs/Formula_101.log`
- Console output with pass/fail status

---

### Formula_102.py

Advanced prepaid ledger validation with max demand penalties and adjustments.

#### Class: PrepaidLedgerComparison

Extended validation including:
- Variable FC based on max demand
- Fixed charge adjustments
- Excess demand penalty (EDP)
- Dynamic recalculation logic

##### Additional Configuration

```python
# Same base config as Formula_101, plus:
# - daily_max_demand_penalty
# - cumm_daily_max_demand_penalty_mtd
# - daily_fixed_charge_adjustment
# - cumm_daily_fixed_charge_adjustment_mtd
```

##### Enhanced Formulas

**Daily FC (Variable by Max Demand):**
```python
if max_demand_percentage <= 75:
    FC = (0.75 × contracted_load × fc_rate) / days_in_month
elif max_demand_percentage <= 100:
    FC = (fc_rate × contracted_load × (max_demand / contracted_load)) / days_in_month
else:  # > 100%
    FC = (fc_rate × contracted_load × (max_demand / contracted_load)) / days_in_month
```

**Fixed Charge Adjustment:**
```python
if max_demand_percentage > 75 and previous_day > 0:
    current_adjustment = (fc_rate × contracted_load × current_day_percentage × (current_day - 1)) / days_in_month
    previous_adjustment = (fc_rate × contracted_load × previous_day_percentage × (current_day - 1)) / days_in_month
    FC_adjustment = current_adjustment - previous_adjustment
```

**Excess Demand Penalty (EDP):**
```python
if max_demand_percentage > 100:
    excess_demand = max_demand - contracted_load
    remaining_days = days_in_month - current_day + 1
    new_total_penalty = excess_demand × fc_rate
    
    if max_demand increased:
        edp_already_charged = cumm_daily_max_demand_penalty
        remaining_penalty = new_total_penalty - edp_already_charged
        daily_edp = remaining_penalty / remaining_days
    else:
        daily_edp = new_total_penalty / remaining_days
```

**Daily ED (Updated):**
```python
Daily ED = (EC + FC_final + EDP) × ed_rate
```

**Daily Final Charge (Updated):**
```python
Daily Final Charge = (EC + FC_final + ED + EDP) - Rebate
```

**Example:**
```python
comparator = PrepaidLedgerComparison()
comparator.run_comparison()
# Output: Formula_102.xlsx with advanced validation
```

---

### Formula_103.py

Most complex validation with tiered EC rates and lifeline switch charges.

#### Class: PrepaidLedgerComparison

Complete validation including:
- Tiered energy charges
- Lifeline switch mechanism
- Two-tier FC rates
- All Formula_102 features

##### Configuration

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
```

##### Lifeline Switch Mechanism

When cumulative consumption crosses 100 kWh:

**EC Lifeline Switch Charge:**
```python
total_ec_switch = (previous_cumm_consumption × ec_rate_1) - (previous_cumm_consumption × ec_rate_0)
# Deducted over 3 days
daily_ec_switch = total_ec_switch / 3
```

**FC Lifeline Switch Charge:**
```python
days_crossed = current_day - 1
max_demand_ratio = max_demand / contracted_load
total_fc_switch = ((fc_rate_1 × contracted_load × days_crossed × max_demand_ratio) / days_in_month) 
                - ((fc_rate_0 × contracted_load × days_crossed × max_demand_ratio) / days_in_month)
# Deducted over 3 days
daily_fc_switch = total_fc_switch / 3
```

##### Tiered EC Calculation

The module calculates EC based on consumption slabs:

```python
def calculate_tiered_ec(daily_consumption, cumm_consumption):
    """
    Calculate EC with tiered rates based on cumulative consumption
    
    Slabs:
    - 0-100 kWh: ec_rate_0 (3.0)
    - 101-150 kWh: ec_rate_2 (5.5)
    - 151-300 kWh: ec_rate_3 (6.0)
    - 301+ kWh: ec_rate_4 (6.5)
    """
    # Complex slab calculation logic
    # See full implementation in code
```

**Example:**
```python
comparator = PrepaidLedgerComparison()
comparator.run_comparison()
# Output: Formula_103.xlsx with complete validation
```

---

## Test Plan Modules

### PE_101.py

Complete test case execution for ST=10, consumption ≤ 100 kWh, MD ≤ 75%.

#### Test Configuration

```python
SUPPLY_TYPECODE = "10"
SANCTIONED_LOAD = 1
LOAD_UNIT = "KW"
METER_INSTALL_DATE = "2025-11-01T00:00:00"
PREPAID_OPENING_BALANCE = 4000
END_WH = 100000
MD_W = 750
```

#### Database Configuration

```python
DB_CONFIG = {
    'host': 'db_mdms.stage.mvvnl.internal',
    'database': 'validation_rules',
    'user': 'postgres',
    'password': '***',
    'port': 5432
}
```

#### Helper Functions

##### `generate_random_number(length: int) -> str`

Generate random numeric string.

**Parameters:**
- `length` (int): Length of string

**Returns:**
- str: Random numeric string

**Example:**
```python
account_id = generate_random_number(10)
# Returns: "4728390561"
```

---

##### `generate_random_alphanumeric(length: int) -> str`

Generate random alphanumeric string (uppercase + digits).

**Parameters:**
- `length` (int): Length of string

**Returns:**
- str: Random alphanumeric string

**Example:**
```python
rate_schedule = generate_random_alphanumeric(6)
# Returns: "A3X9K2"
```

---

##### `generate_consumer_name() -> str`

Generate realistic random consumer name.

**Returns:**
- str: Random first and last name combination

**Example:**
```python
name = generate_consumer_name()
# Returns: "John Smith" or "Mary Garcia"
```

---

##### `generate_email(consumer_name: str) -> str`

Generate email from consumer name with random 3-digit suffix.

**Parameters:**
- `consumer_name` (str): Consumer's full name

**Returns:**
- str: Email address

**Example:**
```python
email = generate_email("John Smith")
# Returns: "johnsmith123@example.com"
```

---

##### `generate_mobile_number() -> int`

Generate 10-digit mobile number.

**Returns:**
- int: Random 10-digit number

**Example:**
```python
mobile = generate_mobile_number()
# Returns: 9876543210
```

---

##### `parse_install_date(date_str: str) -> str`

Parse meter installation date to database format.

**Parameters:**
- `date_str` (str): Date in format "YYYY-MM-DDTHH:MM:SS"

**Returns:**
- str: Date in format "YYYY-MM-DD HH:MM:SS"

**Example:**
```python
parsed = parse_install_date("2025-11-01T00:00:00")
# Returns: "2025-11-01 00:00:00"
```

---

##### `get_month_end_date(start_date_str: str) -> str`

Calculate first day of next month (month end + 1 day).

**Parameters:**
- `start_date_str` (str): Start date in format "YYYY-MM-DD HH:MM:SS"

**Returns:**
- str: End date in format "YYYY-MM-DD HH:MM:SS"

**Example:**
```python
end = get_month_end_date("2025-10-01 00:00:00")
# Returns: "2025-11-01 00:00:00"
```

---

#### Main Functions

##### `create_account() -> Dict[str, Any]`

**Step 1:** Create account with specified parameters via API.

**Returns:**
- Dict containing:
  - `accountId` (str): Generated account ID
  - `meterSrno` (str): Generated meter serial number
  - `meterInstalldate` (str): Installation date
  - `badgeNumber` (str): Badge number
  - `payload` (dict): Complete API payload

**API Endpoint:**
```
POST https://integration1.stage.gomatimvvnl.in/initial_master_sync/
```

**Example:**
```python
account_data = create_account()
if account_data:
    print(f"Account ID: {account_data['accountId']}")
    print(f"Meter No: {account_data['meterSrno']}")
```

**Features:**
- Automatic ID generation (10 digits)
- Meter serial number: "PO" + last 8 digits of account ID
- Random consumer details generation
- Comprehensive logging
- Error handling

---

##### `fill_daily_load_data(account_data: Dict) -> bool`

**Step 2:** Fill daily load data into database for the entire month.

**Parameters:**
- `account_data` (Dict): Account data from create_account()

**Returns:**
- bool: True if successful, False otherwise

**Database Table:** `dailyload_vee_validated`

**Data Generated:**
- Progressive daily values from 0 to END_WH (100000)
- Variability factor: 0.3 to 1.7 of average increment
- VAh calculated from Wh with 0.90 power factor
- Export values (750 Wh total)

**Example:**
```python
success = fill_daily_load_data(account_data)
if success:
    print("Daily load data filled successfully")
```

**Features:**
- Natural consumption patterns with random variation
- Ensures final day reaches exact END_WH value
- UTC-5:30 timestamp adjustment
- Bulk insert for efficiency
- Progress logging every 10 days

---

##### `fill_profile_instant_data(account_data: Dict) -> bool`

**Step 3:** Fill profile instant data (max demand) into database.

**Parameters:**
- `account_data` (Dict): Account data from create_account()

**Returns:**
- bool: True if successful, False otherwise

**Database Table:** `profile_instant_vee`

**Data Generated:**
- Progressive MD_W from 0 to 750W
- MD_VA calculated with 0.90 power factor
- Voltage: 230V, Frequency: 50Hz
- All meter status fields

**Example:**
```python
success = fill_profile_instant_data(account_data)
if success:
    print("Profile instant data filled successfully")
```

**Features:**
- Linear progression of max demand
- Complete meter metadata
- UTC-5:30 timestamp adjustment
- Bulk insert operation

---

##### `trigger_prepaid_ledger(account_id: str) -> bool`

**Step 4:** Trigger prepaid ledger calculation API.

**Parameters:**
- `account_id` (str): Account ID to process

**Returns:**
- bool: True if successful, False otherwise

**API Endpoint:**
```
GET https://engine-web.stage.gomatimvvnl.in/trigger_task/daily_ledger_task/{date}?wallet_balance_sync_flag=False&account_id={account_id}
```

**Example:**
```python
success = trigger_prepaid_ledger(account_data['accountId'])
if success:
    print("Ledger calculation triggered")
```

**Features:**
- Uses yesterday's date
- URL encoding for date parameter
- Error handling and logging

---

##### `fetch_daily_load_data(meter_srno: str) -> List[Dict]`

Fetch daily load data from MDMS API for Excel report.

**Parameters:**
- `meter_srno` (str): Meter serial number

**Returns:**
- List[Dict]: List of daily load records

**API Endpoint:**
```
POST https://mdms-api.stage.gomatimvvnl.in/db-service/dailyloads
```

**Example:**
```python
daily_load = fetch_daily_load_data("PO12345678")
print(f"Fetched {len(daily_load)} records")
```

---

##### `fetch_profile_instant_data(meter_srno: str) -> List[Dict]`

Fetch profile instant data from MDMS API for Excel report.

**Parameters:**
- `meter_srno` (str): Meter serial number

**Returns:**
- List[Dict]: List of profile instant records

**API Endpoint:**
```
POST https://mdms-api.stage.gomatimvvnl.in/db-service/profileinstant
```

**Example:**
```python
profile_data = fetch_profile_instant_data("PO12345678")
print(f"Fetched {len(profile_data)} records")
```

---

##### `generate_excel_report(account_data: Dict) -> bool`

**Step 5:** Generate comprehensive Excel report with all test data.

**Parameters:**
- `account_data` (Dict): Complete account data

**Returns:**
- bool: True if successful, False otherwise

**Output File:** `Result_File/Report_PE_101.xlsx`

**Sheets:**
1. **Summary** - Test case overview
   - Test Case ID, Description
   - Account ID, Meter Number, Badge Number
   - Status

2. **Consumer Details** - Account creation payload
   - All consumer parameters in key-value format

3. **Daily Load** - Daily consumption data
   - Filtered fields from MDMS API
   - Import/Export Wh and VAh

4. **Profile Instant** - Max demand data
   - MD_W, MD_VA, timestamps
   - Voltage, frequency

**Example:**
```python
success = generate_excel_report(account_data)
if success:
    print("Excel report generated: Result_File/Report_PE_101.xlsx")
```

**Features:**
- Professional formatting with headers
- Auto-adjusted column widths
- Color-coded headers (blue background, white text)
- Multiple sheets for organized data
- Error handling

---

##### `main()`

Main orchestration function that executes all 5 steps sequentially.

**Process Flow:**
1. Create account
2. Fill daily load data
3. Fill profile instant data
4. Trigger prepaid ledger API
5. Generate Excel report

**Example:**
```python
if __name__ == "__main__":
    main()
```

**Features:**
- Step-by-step execution with logging
- Abort on failure with error messages
- Final summary with key information
- Complete logging to `logs/PE_101.log`

**Output:**
```
============================================================
PE_101 Test Plan - All Steps Completed Successfully!
============================================================
Account ID: 1234567890
Meter Serial No: PO34567890
Meter Install Date: 2025-11-01T00:00:00
Excel Report: Result_File/Report_PE_101.xlsx
============================================================
```

---

### Incremental_Trigger.py

Utility module to trigger incremental task API.

#### Configuration

```python
LEDGER_API_BASE = "https://engine-web.stage.gomatimvvnl.in"
```

#### Public Functions

##### `trigger_incremental_task() -> bool`

Trigger the incremental_task API for batch processing.

**Returns:**
- bool: True if successful (status 200), False otherwise

**API Endpoint:**
```
GET https://engine-web.stage.gomatimvvnl.in/trigger_task/incremental_task/
```

**Example:**
```python
from Test_Plan.Incremental_Trigger import trigger_incremental_task

success = trigger_incremental_task()
if success:
    print("Incremental task triggered successfully")
else:
    print("Failed to trigger incremental task")
```

**Use Case:**
- Run after multiple account creations
- Batch process pending ledger calculations
- Schedule periodic processing

**Features:**
- Simple GET request
- Error handling and logging
- Status code validation
- Can be imported or run standalone

**Standalone Usage:**
```bash
python Test_Plan/Incremental_Trigger.py
```

---

## Common Patterns

### Error Handling

All modules follow consistent error handling:

```python
try:
    # Operation
    result = perform_operation()
    logger.info("Operation successful")
    return result
except SpecificException as e:
    logger.error(f"Specific error: {str(e)}")
    return default_value
except Exception as e:
    logger.error(f"Unexpected error: {str(e)}")
    import traceback
    traceback.print_exc()
    return default_value
```

### Logging

All modules use structured logging:

```python
import logging
import os

os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/module_name.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
```

### Data Validation

Common validation patterns:

```python
# Check required columns
if 'required_column' not in df.columns:
    logger.error("Missing required column")
    return None

# Filter out invalid data
df_filtered = df.dropna(subset=['key_column'])
df_filtered = df_filtered[df_filtered['key_column'].str.strip() != '']

# Type preservation
df = pd.read_csv(file, dtype={'accountId': str, 'meterSrno': str})
```

---

## API Endpoints Reference

### Integration API
- **Account Creation:** `POST https://integration1.stage.gomatimvvnl.in/initial_master_sync/`
  - Headers: `Authorization: Bearer {token}`
  - Content-Type: `application/json`

### Engine Web API
- **Daily Ledger:** `GET https://engine-web.stage.gomatimvvnl.in/daily_prepaid_ledger/{account_id}/?meter_number={meter}`
- **Trigger Daily Task:** `GET https://engine-web.stage.gomatimvvnl.in/trigger_task/daily_ledger_task/{date}?wallet_balance_sync_flag=False&account_id={id}`
- **Trigger Incremental:** `GET https://engine-web.stage.gomatimvvnl.in/trigger_task/incremental_task/`

### MDMS API
- **Daily Load:** `POST https://mdms-api.stage.gomatimvvnl.in/db-service/dailyloads`
- **Profile Instant:** `POST https://mdms-api.stage.gomatimvvnl.in/db-service/profileinstant`

---

## Data Models

### Consumer Record
```python
{
    "Report_ID": str,
    "accountId": str,
    "meterSrno": str,
    "supplyTypecode": str,
    "sanctionedLoad": float,
    "loadUnit": str,
    "meterInstalldate": str,
    "greenEnergyflag": str,
    "prepaidOpeningbalance": float
}
```

### Daily Load Record
```python
{
    "device_identifier": str,
    "data_timestamp": str,
    "import_Wh": int,
    "import_VAh": int,
    "export_Wh": int,
    "export_VAh": int,
    "meter_type": str,
    "is_valid": bool,
    "is_estimated": bool,
    "is_edited": bool
}
```

### Profile Instant Record
```python
{
    "device_identifier": str,
    "data_timestamp": str,
    "MD_W": int,
    "MD_VA": int,
    "MD_W_datetime": str,
    "MD_VA_datetime": str,
    "voltage": int,
    "frequency": float,
    "meter_type": str
}
```

### Prepaid Ledger Record
```python
{
    "start_date_time": str,
    "end_date_time": str,
    "account_id": str,
    "meter_number": str,
    "daily_consumption": float,
    "cumm_daily_consumption_mtd": float,
    "daily_consumption_in_rupees": float,
    "cumm_daily_consumption_rupees_mtd": float,
    "daily_fixed_charges": float,
    "cumm_daily_fixed_charges_mtd": float,
    "daily_ec_plus_fc_charge": float,
    "cumm_daily_ec_plus_fc_charge_mtd": float,
    "daily_ed_charge": float,
    "cumm_ed_charges_mtd": float,
    "daily_final_rebate": float,
    "cumm_daily_final_rebate_mtd": float,
    "daily_final_charge": float,
    "cumm_daily_final_charge_mtd": float,
    "opening_balance": float,
    "closing_balance": float
}
```

---

## Version Information

- **Framework Version:** 1.0
- **Python Version:** 3.7+
- **Last Updated:** December 2025

For more information, see the main [README.md](../README.md) file.
