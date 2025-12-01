# UP Prepaid Engine Automation - API Documentation

## Table of Contents

1. [Overview](#overview)
2. [Module: account.py](#module-accountpy)
3. [Module: Download_Ledger.py](#module-download_ledgerpy)
4. [Module: Formula Validation](#module-formula-validation)
5. [Module: Incremental_Trigger.py](#module-incremental_triggerpy)
6. [Module: Test Plan Scripts](#module-test-plan-scripts)
7. [Common Utilities](#common-utilities)
8. [Configuration](#configuration)

---

## Overview

This project is an automation testing framework for UP Prepaid Engine validation. It provides tools for:
- Extracting consumer details from Excel reports
- Downloading prepaid ledger data from APIs
- Validating formula calculations
- Executing comprehensive test cases

---

## Module: account.py

### Description
Extracts consumer details from Excel report files and consolidates them into a CSV file.

### Public Functions

#### `get_report_identifier(filename: str) -> str`

Extracts the report identifier from an Excel filename.

**Parameters:**
- `filename` (str): The Excel filename (e.g., "Report_PE_101.xlsx")

**Returns:**
- `str`: The report identifier without extension (e.g., "Report_PE_101")

**Example:**
```python
from account import get_report_identifier

report_id = get_report_identifier("Report_PE_101.xlsx")
# Returns: "Report_PE_101"
```

---

#### `extract_consumer_details(excel_file: str) -> pd.DataFrame`

Extracts consumer details from a single Excel file's "Consumer Details" sheet.

**Parameters:**
- `excel_file` (str): Path to the Excel file

**Returns:**
- `pd.DataFrame`: DataFrame containing consumer details with columns:
  - `Report_ID`: Report identifier
  - `accountId`: Account ID
  - `meterSrno`: Meter serial number
  - `supplyTypecode`: Supply type code
  - `sanctionedLoad`: Sanctioned load
  - `loadUnit`: Load unit
  - `meterInstalldate`: Meter installation date
  - `greenEnergyflag`: Green energy flag
  - `prepaidOpeningbalance`: Prepaid opening balance

**Raises:**
- `FileNotFoundError`: If the Excel file doesn't exist
- `ValueError`: If the sheet structure is unexpected

**Example:**
```python
from account import extract_consumer_details
import pandas as pd

df = extract_consumer_details("Result_File/Report_PE_101.xlsx")
print(df.head())
```

**Notes:**
- The function expects a Parameter/Value column structure in the Excel sheet
- Parameter matching is case-insensitive
- Missing parameters are logged as warnings

---

#### `process_all_reports() -> pd.DataFrame`

Processes all Excel report files matching the pattern `Report_PE_*.xlsx` in the `Result_File` folder.

**Returns:**
- `pd.DataFrame`: Combined DataFrame with all consumer details from all reports

**Example:**
```python
from account import process_all_reports

combined_df = process_all_reports()
print(f"Total records: {len(combined_df)}")
print(f"Unique reports: {combined_df['Report_ID'].nunique()}")
```

**Configuration:**
- `RESULT_FOLDER`: Default is `"Result_File"`
- Files are processed in sorted order

---

#### `save_to_csv(df: pd.DataFrame, output_file: str)`

Saves a DataFrame to a CSV file with UTF-8 BOM encoding.

**Parameters:**
- `df` (pd.DataFrame): DataFrame to save
- `output_file` (str): Output CSV filename

**Example:**
```python
from account import process_all_reports, save_to_csv

df = process_all_reports()
save_to_csv(df, "Consumer_details.csv")
```

---

#### `main()`

Main entry point that processes all reports and saves to CSV.

**Example:**
```python
from account import main

if __name__ == "__main__":
    main()
```

**Output:**
- Creates `Consumer_details.csv` with all extracted consumer details
- Prints summary statistics

---

## Module: Download_Ledger.py

### Description
Downloads prepaid ledger data from the API for all consumers listed in `Consumer_details.csv` and saves to an Excel file.

### Configuration Constants

```python
API_URL = "https://engine-web.stage.gomatimvvnl.in/daily_prepaid_ledger/"
CSV_FILE = "Consumer_details.csv"
```

### Public Functions

#### `read_consumer_details() -> List[Tuple[str, str, str]]`

Reads account IDs, meter numbers, and Report IDs from the CSV file.

**Returns:**
- `List[Tuple[str, str, str]]`: List of tuples containing (report_id, account_id, meter_number)

**Example:**
```python
from Download_Ledger import read_consumer_details

consumer_data = read_consumer_details()
for report_id, account_id, meter_number in consumer_data:
    print(f"{report_id}: Account {account_id}, Meter {meter_number}")
```

**Notes:**
- Preserves leading zeros in account IDs and meter numbers by reading as strings
- Filters out rows with empty accountId or meterSrno
- If Report_ID column is missing, generates it as `accountId_meterSrno`

---

#### `fetch_and_save_data()`

Fetches prepaid ledger data from the API for all consumers and saves to Excel.

**Output:**
- Creates `Prepaid_Ledger_Report.xlsx` with:
  - One sheet per consumer (named by Report_ID)
  - An "Errors" sheet if any API calls fail
  - A "Summary" sheet if no data is found

**Example:**
```python
from Download_Ledger import fetch_and_save_data

fetch_and_save_data()
```

**API Endpoint:**
```
GET {API_URL}{account_id}/?meter_number={meter_number}
Headers: {"accept": "application/json"}
```

**Error Handling:**
- HTTP errors are logged to the "Errors" sheet
- Timeout errors (30 seconds) are captured
- Request exceptions are handled gracefully

**Required Fields Extracted:**
- `start_date_time`, `end_date_time`
- `account_id`, `meter_number`
- `daily_consumption`, `cumm_daily_consumption_mtd`
- `daily_consumption_in_rupees`, `cumm_daily_consumption_rupees_mtd`
- `daily_fixed_charges`, `cumm_daily_fixed_charges_mtd`
- `daily_ec_plus_fc_charge`, `cumm_daily_ec_plus_fc_charge_mtd`
- `daily_ed_charge`, `cumm_ed_charges_mtd`
- `daily_final_rebate`, `cumm_daily_final_rebate_mtd`
- `daily_final_charge`, `cumm_daily_final_charge_mtd`
- `opening_balance`, `closing_balance`
- And more (see `REQUIRED_FIELDS` constant)

---

## Module: Formula Validation

### Description
Validates prepaid ledger calculations by comparing API responses with expected formula-based calculations.

### Classes

#### `PrepaidLedgerComparison` (Formula_101.py, Formula_102.py, Formula_103.py)

Base class for formula validation. Each formula file implements a specific calculation scenario.

**Location:** `Formula/Formula_101.py`, `Formula/Formula_102.py`, `Formula/Formula_103.py`

---

### Formula_101.py

#### Description
Validates basic prepaid ledger calculations with:
- Fixed EC rate
- Fixed charges based on contracted load
- Electricity duty and rebate calculations

#### Configuration

```python
contracted_load = 1  # kW
fc_rate = 50  # Per kW FC Rate
ed_rate = 0.05  # 5%
rebate_rate = 0.02  # 2%
opening_balance = 5000
ec_rate = 3  # Fixed EC rate
days_in_month = 31
```

#### Public Methods

##### `__init__(self)`

Initializes the comparison object with configuration parameters.

**Example:**
```python
from Formula.Formula_101 import PrepaidLedgerComparison

comparator = PrepaidLedgerComparison()
```

---

##### `fetch_prepaid_ledger_data(self) -> pd.DataFrame`

Fetches prepaid ledger data from the API for the configured account and date range.

**Returns:**
- `pd.DataFrame`: Filtered DataFrame containing ledger entries for the specified date range

**Example:**
```python
comparator = PrepaidLedgerComparison()
df = comparator.fetch_prepaid_ledger_data()
print(f"Fetched {len(df)} records")
```

**API Configuration:**
- `api_url`: Configured in `__init__`
- `start_date`: Start date for filtering (default: "2025-10-01T00:00:00")
- `end_date`: End date for filtering (default: "2025-11-01T00:00:00", exclusive)

---

##### `calculate_expected_values(self, df: pd.DataFrame) -> pd.DataFrame`

Calculates expected values based on formula rules.

**Parameters:**
- `df` (pd.DataFrame): DataFrame with API data

**Returns:**
- `pd.DataFrame`: DataFrame with added `expected_*` columns

**Formulas Used:**

1. **Daily EC (Energy Charges):**
   ```
   Daily EC = daily_consumption × EC_rate
   ```

2. **Daily FC (Fixed Charges):**
   ```
   Daily FC = (0.75 × Contracted_Load × FC_Rate) / days_in_month
   ```

3. **Daily EC + FC:**
   ```
   Daily EC + FC = Daily EC + Daily FC
   ```

4. **Daily ED (Electricity Duty):**
   ```
   Daily ED = (EC + FC) × ED_rate
   ```

5. **Daily Rebate:**
   ```
   Daily Rebate = (EC + FC) × Rebate_rate
   ```

6. **Daily Final Charge:**
   ```
   Daily Final Charge = (EC + FC + ED) - Rebate
   ```

7. **Closing Balance:**
   ```
   Closing Balance = Opening Balance - Daily Final Charge
   ```

**Example:**
```python
df_with_expected = comparator.calculate_expected_values(df)
```

---

##### `compare_values(self, df: pd.DataFrame) -> pd.DataFrame`

Compares calculated expected values with actual API values.

**Parameters:**
- `df` (pd.DataFrame): DataFrame with expected values

**Returns:**
- `pd.DataFrame`: DataFrame with comparison results and status

**Tolerance:**
- Floating point comparison tolerance: 0.01

**Status Column:**
- `"All Match"`: All values match within tolerance
- Otherwise: Comma-separated list of mismatched columns

**Example:**
```python
df_comparison = comparator.compare_values(df_with_expected)
print(df_comparison[['start_date_time', 'Status']].head())
```

---

##### `generate_comparison_report(self, df: pd.DataFrame, filename: str = "Formula_101.xlsx")`

Generates an Excel report with comparison results.

**Parameters:**
- `df` (pd.DataFrame): DataFrame with comparison results
- `filename` (str): Output Excel filename (default: "Formula_101.xlsx")

**Output:**
- Excel file with "Prepaid_Ledger" sheet containing:
  - Actual values
  - Expected values
  - Comparison status

**Example:**
```python
comparator.generate_comparison_report(df_comparison, "Formula_101_Results.xlsx")
```

---

##### `run_comparison(self)`

Runs the complete comparison process: fetch → calculate → compare → report.

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
5. Log results

---

### Formula_102.py

#### Description
Extends Formula_101 with additional calculations:
- Max demand-based fixed charges
- Fixed charge adjustments
- Excess demand penalty (EDP)

#### Additional Configuration

```python
# Same as Formula_101, plus:
# Max demand percentage calculations
# EDP (Excess Demand Penalty) calculations
```

#### Additional Formulas

1. **Fixed Charges (Variable based on Max Demand):**
   - If Max Demand ≤ 75%: `FC = (0.75 × Contracted_Load × FC_Rate) / days_in_month`
   - If 75% < Max Demand ≤ 100%: `FC = (FC_Rate × Contracted_Load × (Max_Demand / Contracted_Load)) / days_in_month`
   - If Max Demand > 100%: `FC = (FC_Rate × Contracted_Load × (Max_Demand / Contracted_Load)) / days_in_month`

2. **Fixed Charge Adjustment:**
   ```
   If Max Demand > 75% and not first day:
   Adjustment = ((FC_Rate × Contracted_Load × Current_Day_Percentage × (Current_Day - 1)) / days_in_month) 
                - ((FC_Rate × Contracted_Load × Previous_Day_Percentage × (Current_Day - 1)) / days_in_month)
   ```

3. **Excess Demand Penalty (EDP):**
   ```
   If Max Demand > 100%:
   Excess_Demand = Max_Demand - Contracted_Load
   Total_Penalty = Excess_Demand × FC_Rate
   Daily_EDP = Remaining_Penalty / Remaining_Days
   ```

4. **Daily Final Charge (Updated):**
   ```
   Daily Final Charge = (EC + FC + ED + EDP) - Rebate
   ```

**Public Methods:** Same as Formula_101, with enhanced calculations.

---

### Formula_103.py

#### Description
Extends Formula_102 with:
- Tiered EC rates based on cumulative consumption
- Life line switch charges
- Dynamic FC rates based on consumption threshold

#### Additional Configuration

```python
# EC Rates (Tiered):
ec_rate_0 = 3      # Rs. per kWh (upto 100 kWh)
ec_rate_1 = 5.5    # Rs. per kWh (0 to 100 kWh when consumption crosses 100)
ec_rate_2 = 5.5    # Rs. per kWh (101 to 150 kWh)
ec_rate_3 = 6      # Rs. per kWh (151 to 300 kWh)
ec_rate_4 = 6.5    # Rs. per kWh (above 301 kWh)

# FC Rates:
fc_rate_0 = 50     # Rs. per kW (if cumm_daily_consumption_mtd <= 100 kWh)
fc_rate_1 = 110    # Rs. per kW (if cumm_daily_consumption_mtd > 100 kWh)
```

#### Additional Formulas

1. **Tiered EC Calculation:**
   - Consumption is split across tiers
   - Each tier uses its respective rate
   - Example: If cumulative consumption is 120 kWh and daily consumption is 10 kWh:
     - 0-100 kWh: Uses `ec_rate_0`
     - 101-120 kWh: Uses `ec_rate_2`

2. **Life Line Switch Charge (EC):**
   ```
   When cumulative consumption crosses 100 kWh:
   Total_EC_Switch_Charge = (Previous_Cumm_Consumption × ec_rate_1) 
                           - (Previous_Cumm_Consumption × ec_rate_0)
   Daily_EC_Switch_Charge = Total_EC_Switch_Charge / 3 (distributed over 3 days)
   Daily_EC_Final = Daily_EC - Daily_EC_Switch_Charge
   ```

3. **Life Line Switch Charge (FC):**
   ```
   When cumulative consumption crosses 100 kWh:
   Days_Crossed = Current_Day - 1
   Max_Demand_Ratio = Max_Demand / Contracted_Load
   Total_FC_Switch_Charge = ((fc_rate_1 × Contracted_Load × Days_Crossed × Max_Demand_Ratio) / days_in_month)
                          - ((fc_rate_0 × Contracted_Load × Days_Crossed × Max_Demand_Ratio) / days_in_month)
   Daily_FC_Switch_Charge = Total_FC_Switch_Charge / 3
   Daily_FC_Final = Daily_FC + Adjustment - Daily_FC_Switch_Charge
   ```

**Public Methods:** Same as Formula_102, with tiered rate calculations.

---

## Module: Incremental_Trigger.py

### Description
Triggers the incremental task API to process incremental prepaid ledger calculations.

### Public Functions

#### `trigger_incremental_task() -> bool`

Triggers the incremental task API endpoint.

**Returns:**
- `bool`: `True` if API call was successful (status 200), `False` otherwise

**API Endpoint:**
```
GET https://engine-web.stage.gomatimvvnl.in/trigger_task/incremental_task/
Headers: {"accept": "application/json"}
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

**Logging:**
- Logs API call details to `logs/Incremental_Trigger.log`
- Also outputs to console

**Usage:**
```python
if __name__ == "__main__":
    result = trigger_incremental_task()
```

---

## Module: Test Plan Scripts

### Description
Test case scripts (PE_101.py through PE_225.py) for validating prepaid engine functionality.

### Common Structure

Each test script follows a similar structure:

1. **Configuration Section:** Test parameters
2. **Helper Functions:** Utility functions for data generation
3. **Step 1:** Create account
4. **Step 2:** Fill daily load data
5. **Step 3:** Fill profile instant data
6. **Step 4:** Trigger prepaid ledger
7. **Step 5:** Generate Excel report

### Common Public Functions

#### `generate_random_number(length: int) -> str`

Generates a random number string of specified length.

**Parameters:**
- `length` (int): Length of the number string

**Returns:**
- `str`: Random number string

**Example:**
```python
account_id = generate_random_number(10)
# Returns: "1234567890"
```

---

#### `generate_random_alphanumeric(length: int) -> str`

Generates a random alphanumeric string.

**Parameters:**
- `length` (int): Length of the string

**Returns:**
- `str`: Random alphanumeric string (uppercase letters and digits)

**Example:**
```python
meter_srno = generate_random_alphanumeric(12)
# Returns: "ABC123XYZ456"
```

---

#### `generate_consumer_name() -> str`

Generates a random consumer name.

**Returns:**
- `str`: Random first and last name combination

**Example:**
```python
name = generate_consumer_name()
# Returns: "John Smith"
```

---

#### `generate_email(consumer_name: str) -> str`

Generates an email address based on consumer name.

**Parameters:**
- `consumer_name` (str): Consumer name

**Returns:**
- `str`: Email address

**Example:**
```python
email = generate_email("John Smith")
# Returns: "johnsmith123@example.com"
```

---

#### `generate_mobile_number() -> int`

Generates a random 10-digit mobile number.

**Returns:**
- `int`: 10-digit mobile number

**Example:**
```python
mobile = generate_mobile_number()
# Returns: 9876543210
```

---

#### `parse_install_date(date_str: str) -> str`

Parses meter installation date from ISO format to database format.

**Parameters:**
- `date_str` (str): Date string in format "2025-10-01T00:00:00" or "2025-10-01 00:00:00"

**Returns:**
- `str`: Date string in format "yyyy-mm-dd HH:MM:SS"

**Example:**
```python
db_date = parse_install_date("2025-10-01T00:00:00")
# Returns: "2025-10-01 00:00:00"
```

---

#### `get_month_end_date(start_date_str: str) -> str`

Calculates the first day of the next month (month end + 1 day).

**Parameters:**
- `start_date_str` (str): Start date string in format "yyyy-mm-dd HH:MM:SS"

**Returns:**
- `str`: First day of next month in format "yyyy-mm-dd HH:MM:SS"

**Example:**
```python
end_date = get_month_end_date("2025-10-01 00:00:00")
# Returns: "2025-11-01 00:00:00"
```

---

#### `create_account() -> Dict[str, Any]`

Creates a new account via the account API.

**Returns:**
- `Dict[str, Any]`: Account data including accountId, meterSrno, etc.

**API Endpoint:**
```
POST https://integration1.stage.gomatimvvnl.in/initial_master_sync/
```

**Example:**
```python
account_data = create_account()
print(f"Account ID: {account_data['accountId']}")
print(f"Meter Serial: {account_data['meterSrno']}")
```

---

#### `fill_daily_load_data(account_data: Dict[str, Any])`

Fills daily load data into the database for the account.

**Parameters:**
- `account_data` (Dict[str, Any]): Account data dictionary

**Database:**
- Table: `dailyload_vee_validated`
- Inserts records for each day in the month

**Example:**
```python
fill_daily_load_data(account_data)
```

---

#### `fill_profile_instant_data(account_data: Dict[str, Any])`

Fills profile instant data into the database for the account.

**Parameters:**
- `account_data` (Dict[str, Any]): Account data dictionary

**Database:**
- Table: `profile_instant_vee`
- Inserts records for each day in the month

**Example:**
```python
fill_profile_instant_data(account_data)
```

---

#### `trigger_prepaid_ledger(account_id: str)`

Triggers the prepaid ledger calculation API.

**Parameters:**
- `account_id` (str): Account ID

**API Endpoint:**
```
POST https://engine-web.stage.gomatimvvnl.in/prepaid_ledger_trigger/{account_id}
```

**Example:**
```python
trigger_prepaid_ledger("1234567890")
```

---

#### `fetch_daily_load_data(meter_srno: str) -> pd.DataFrame`

Fetches daily load data from MDMS API.

**Parameters:**
- `meter_srno` (str): Meter serial number

**Returns:**
- `pd.DataFrame`: Daily load data

**API Endpoint:**
```
GET https://mdms-api.stage.gomatimvvnl.in/db-service/dailyloads?meter_srno={meter_srno}
```

**Example:**
```python
df = fetch_daily_load_data("ABC123XYZ456")
```

---

#### `fetch_profile_instant_data(meter_srno: str) -> pd.DataFrame`

Fetches profile instant data from MDMS API.

**Parameters:**
- `meter_srno` (str): Meter serial number

**Returns:**
- `pd.DataFrame`: Profile instant data

**API Endpoint:**
```
GET https://mdms-api.stage.gomatimvvnl.in/db-service/profileinstant?meter_srno={meter_srno}
```

**Example:**
```python
df = fetch_profile_instant_data("ABC123XYZ456")
```

---

#### `generate_excel_report(account_data: Dict[str, Any])`

Generates a comprehensive Excel report with all test data and results.

**Parameters:**
- `account_data` (Dict[str, Any]): Account data dictionary

**Output:**
- Excel file: `Report_PE_{test_id}.xlsx` with sheets:
  - Consumer Details
  - Daily Load Data
  - Profile Instant Data
  - Prepaid Ledger Data

**Example:**
```python
generate_excel_report(account_data)
```

---

#### `main()`

Main entry point for the test script.

**Example:**
```python
if __name__ == "__main__":
    main()
```

**Process Flow:**
1. Create account
2. Fill daily load data
3. Fill profile instant data
4. Trigger prepaid ledger
5. Fetch and validate data
6. Generate Excel report

---

## Common Utilities

### Database Configuration

```python
DB_CONFIG = {
    'host': 'db_mdms.stage.mvvnl.internal',
    'database': 'validation_rules',
    'user': 'postgres',
    'password': 'LBjsKJkd937042!!',
    'port': 5432
}
```

### API Configuration

```python
# Account API
ACCOUNT_API_URL = "https://integration1.stage.gomatimvvnl.in/initial_master_sync/"
ACCOUNT_API_HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer {token}'
}

# Ledger API
LEDGER_API_BASE = "https://engine-web.stage.gomatimvvnl.in"

# MDMS API
MDMS_API_BASE = "https://mdms-api.stage.gomatimvvnl.in/db-service"
DAILYLOAD_API_URL = f"{MDMS_API_BASE}/dailyloads"
PROFILE_INSTANT_API_URL = f"{MDMS_API_BASE}/profileinstant"
```

---

## Configuration

### Environment Variables

No environment variables are currently used. All configuration is hardcoded in scripts.

### File Paths

- **Result Files:** `Result_File/` directory
- **Logs:** `logs/` directory
- **Output CSV:** `Consumer_details.csv`
- **Output Excel:** `Prepaid_Ledger_Report.xlsx` (Download_Ledger.py)
- **Formula Reports:** `Formula_{id}.xlsx` (Formula scripts)
- **Test Reports:** `Report_PE_{id}.xlsx` (Test scripts)

---

## Usage Examples

### Example 1: Extract Consumer Details

```python
from account import main

# Extract all consumer details from Excel reports
main()
# Output: Consumer_details.csv
```

### Example 2: Download Ledger Data

```python
from Download_Ledger import fetch_and_save_data

# Download ledger data for all consumers
fetch_and_save_data()
# Output: Prepaid_Ledger_Report.xlsx
```

### Example 3: Validate Formula 101

```python
from Formula.Formula_101 import PrepaidLedgerComparison

# Run formula validation
comparator = PrepaidLedgerComparison()
comparator.run_comparison()
# Output: Formula_101.xlsx, logs/Formula_101.log
```

### Example 4: Trigger Incremental Task

```python
from Test_Plan.Incremental_Trigger import trigger_incremental_task

# Trigger incremental task API
success = trigger_incremental_task()
if success:
    print("Incremental task triggered successfully")
# Output: logs/Incremental_Trigger.log
```

### Example 5: Run Test Case PE_101

```python
from Test_Plan.PE_101 import main

# Execute test case
main()
# Output: Report_PE_101.xlsx, logs/PE_101.log
```

---

## Error Handling

### Common Exceptions

1. **FileNotFoundError:** When Excel/CSV files are missing
2. **ValueError:** When data format is unexpected
3. **requests.exceptions.HTTPError:** When API calls fail
4. **requests.exceptions.Timeout:** When API calls timeout (30 seconds)
5. **psycopg2.Error:** When database operations fail

### Error Logging

All modules use Python's `logging` module:
- Log files are saved in `logs/` directory
- Console output is also enabled
- Log format: `%(asctime)s - %(levelname)s - %(message)s`

---

## Dependencies

### Required Python Packages

```python
pandas>=1.0.0
requests>=2.25.0
openpyxl>=3.0.0
psycopg2-binary>=2.8.0
numpy>=1.19.0
```

### Installation

```bash
pip install pandas requests openpyxl psycopg2-binary numpy
```

---

## Notes

1. **API Authentication:** Bearer token authentication is used for account API
2. **Database Connection:** Direct PostgreSQL connection is used for data insertion
3. **Date Handling:** All dates are handled in UTC timezone
4. **Tolerance:** Floating point comparisons use 0.01 tolerance
5. **Sheet Names:** Excel sheet names are limited to 31 characters
6. **CSV Encoding:** UTF-8 BOM encoding is used for CSV files

---

## Support

For issues or questions, refer to:
- Log files in `logs/` directory
- Excel reports for detailed data
- Test case descriptions in script docstrings

---

**Last Updated:** Generated automatically
**Version:** 1.0
