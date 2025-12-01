# UP Prepaid Engine Automation - API Documentation

## Table of Contents

1. [Overview](#overview)
2. [Module: account.py](#module-accountpy)
3. [Module: Download_Ledger.py](#module-download_ledgerpy)
4. [Module: Formula Validation](#module-formula-validation)
5. [Module: Test Cases (PE_*.py)](#module-test-cases-pe_py)
6. [Usage Examples](#usage-examples)
7. [Configuration](#configuration)

---

## Overview

This project is an automation testing framework for UP Prepaid Engine validation. It provides tools for:
- Extracting consumer details from Excel reports
- Downloading prepaid ledger data from APIs
- Validating billing formulas
- Running automated test cases

### Project Structure

```
/workspace/
├── account.py                    # Consumer details extraction
├── Download_Ledger.py           # Ledger data download
├── Formula/                      # Formula validation scripts
│   ├── Formula_101.py
│   ├── Formula_102.py
│   └── Formula_103.py
├── Test_Plan/                    # Test case scripts (PE_101.py - PE_225.py)
├── Incremental_Trigger.py        # Incremental trigger functionality
└── logs/                         # Log files
```

---

## Module: account.py

### Description
Extracts consumer details from Excel report files (`Report_PE_*.xlsx`) in the `Result_File` folder and consolidates them into a CSV file.

### Public Functions

#### `get_report_identifier(filename: str) -> str`
Extracts the report identifier from a filename.

**Parameters:**
- `filename` (str): The Excel filename (e.g., "Report_PE_101.xlsx")

**Returns:**
- `str`: Report identifier without extension (e.g., "Report_PE_101")

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
- `FileNotFoundError`: If the file doesn't exist
- `ValueError`: If the sheet structure is unexpected

**Example:**
```python
from account import extract_consumer_details
import pandas as pd

df = extract_consumer_details("Result_File/Report_PE_101.xlsx")
print(df.head())
```

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
```

---

#### `save_to_csv(df: pd.DataFrame, output_file: str)`
Saves a DataFrame to a CSV file with UTF-8 encoding.

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
Main entry point that processes all reports and saves to `Consumer_details.csv`.

**Usage:**
```bash
python account.py
```

**Output:**
- Creates `Consumer_details.csv` in the current directory
- Prints processing summary to console

---

## Module: Download_Ledger.py

### Description
Downloads prepaid ledger data from the API for all consumers listed in `Consumer_details.csv` and saves the results to an Excel file.

### Configuration Constants

- `API_URL` (str): Base URL for the prepaid ledger API
  - Default: `"https://engine-web.stage.gomatimvvnl.in/daily_prepaid_ledger/"`
- `CSV_FILE` (str): Input CSV file path
  - Default: `"Consumer_details.csv"`
- `REQUIRED_FIELDS` (list): List of fields to extract from API response

### Public Functions

#### `read_consumer_details() -> List[Tuple[str, str, str]]`
Reads account IDs, meter numbers, and Report IDs from the CSV file.

**Returns:**
- `List[Tuple[str, str, str]]`: List of tuples containing (report_id, account_id, meter_number)

**Raises:**
- `FileNotFoundError`: If CSV file doesn't exist

**Example:**
```python
from Download_Ledger import read_consumer_details

consumer_data = read_consumer_details()
for report_id, account_id, meter_number in consumer_data:
    print(f"{report_id}: {account_id} - {meter_number}")
```

---

#### `fetch_and_save_data()`
Fetches ledger data from the API for all consumers in the CSV file and saves to Excel.

**Process:**
1. Reads consumer details from CSV
2. For each consumer, calls the API endpoint: `{API_URL}{account_id}/?meter_number={meter_number}`
3. Extracts required fields from API response
4. Saves each consumer's data to a separate sheet in Excel
5. Creates an "Errors" sheet for any failed requests

**Output:**
- Creates `Prepaid_Ledger_Report.xlsx` with:
  - One sheet per consumer (named by Report_ID)
  - An "Errors" sheet (if any errors occurred)
  - A "Summary" sheet (if no data was found)

**Example:**
```python
from Download_Ledger import fetch_and_save_data

fetch_and_save_data()
# Creates Prepaid_Ledger_Report.xlsx
```

**Error Handling:**
- HTTP errors (404, 500, etc.) are logged in the "Errors" sheet
- Timeout errors (30 seconds) are captured
- Network errors are handled gracefully

---

## Module: Formula Validation

### Description
The Formula modules validate prepaid ledger calculations by comparing API responses with expected calculated values.

### Classes

#### `PrepaidLedgerComparison` (Formula_101.py, Formula_102.py, Formula_103.py)

Base class for formula validation. Each formula file implements specific billing calculation rules.

##### Constructor: `__init__(self)`

Initializes the comparison object with configuration parameters.

**Configuration Parameters (varies by formula):**
- `contracted_load` (float): Contracted load in kW
- `fc_rate` (float): Fixed charge rate per kW
- `ed_rate` (float): Electricity duty rate (e.g., 0.05 for 5%)
- `rebate_rate` (float): Rebate rate (e.g., 0.02 for 2%)
- `opening_balance` (float): Opening balance
- `ec_rate` (float): Energy charge rate per kWh
- `days_in_month` (int): Number of days in the month
- `api_url` (str): API endpoint URL
- `start_date` (str): Start date for data range (ISO format)
- `end_date` (str): End date for data range (ISO format)

**Example:**
```python
from Formula.Formula_101 import PrepaidLedgerComparison

comparator = PrepaidLedgerComparison()
# Configuration is set automatically
```

---

##### `fetch_prepaid_ledger_data(self) -> pd.DataFrame`
Fetches prepaid ledger data from the API for the configured account and date range.

**Returns:**
- `pd.DataFrame`: DataFrame containing ledger data filtered by date range

**Raises:**
- `requests.exceptions.RequestException`: On API errors
- `ValueError`: If API response format is unexpected

**Example:**
```python
df = comparator.fetch_prepaid_ledger_data()
print(f"Fetched {len(df)} records")
```

---

##### `calculate_expected_values(self, df: pd.DataFrame) -> pd.DataFrame`
Calculates expected values based on billing formulas.

**Parameters:**
- `df` (pd.DataFrame): DataFrame with API data

**Returns:**
- `pd.DataFrame`: DataFrame with added `expected_*` columns for each calculated field

**Calculated Fields (varies by formula):**
- `expected_daily_consumption_in_rupees`
- `expected_daily_fixed_charges`
- `expected_daily_ec_plus_fc_charge`
- `expected_daily_ed_charge`
- `expected_daily_final_rebate`
- `expected_daily_final_charge`
- `expected_opening_balance`
- `expected_closing_balance`
- Plus cumulative (MTD) versions of each

**Example:**
```python
df_with_expected = comparator.calculate_expected_values(df)
```

---

##### `compare_values(self, df: pd.DataFrame) -> pd.DataFrame`
Compares calculated expected values with actual API values.

**Parameters:**
- `df` (pd.DataFrame): DataFrame with both actual and expected values

**Returns:**
- `pd.DataFrame`: DataFrame with comparison results and `Status` column

**Status Values:**
- `"All Match"`: All values match within tolerance (0.01)
- `"column1, column2, ..."`: List of mismatched columns

**Example:**
```python
df_comparison = comparator.compare_values(df_with_expected)
mismatches = df_comparison[df_comparison['Status'] != 'All Match']
print(f"Mismatches: {len(mismatches)}")
```

---

##### `generate_comparison_report(self, df: pd.DataFrame, filename: str = None)`
Generates an Excel report with comparison results.

**Parameters:**
- `df` (pd.DataFrame): DataFrame with comparison results
- `filename` (str, optional): Output filename (default: Formula-specific)

**Output:**
- Excel file with columns showing actual vs expected values
- Status column indicating matches/mismatches

**Example:**
```python
comparator.generate_comparison_report(df_comparison, "Formula_101_Report.xlsx")
```

---

##### `run_comparison(self)`
Runs the complete comparison workflow.

**Process:**
1. Fetches data from API
2. Calculates expected values
3. Compares values
4. Generates report
5. Logs test results (PASS/FAIL)

**Example:**
```python
comparator = PrepaidLedgerComparison()
comparator.run_comparison()
# Outputs: Formula_101.xlsx and logs to logs/Formula_101.log
```

---

### Formula-Specific Details

#### Formula_101.py
Validates basic prepaid ledger calculations:
- Simple EC and FC calculations
- ED and rebate calculations
- Balance tracking

**Key Formulas:**
- Daily EC = `daily_consumption × ec_rate`
- Daily FC = `(0.75 × contracted_load × fc_rate) / days_in_month`
- Daily ED = `(EC + FC) × ed_rate`
- Daily Rebate = `(EC + FC) × rebate_rate`
- Daily Final Charge = `(EC + FC + ED) - Rebate`

---

#### Formula_102.py
Extends Formula_101 with:
- Max demand-based FC calculations
- Fixed charge adjustments
- Excess demand penalty (EDP)

**Key Formulas:**
- FC varies based on max demand percentage (≤75%, 75-100%, >100%)
- FC Adjustment for max demand changes
- EDP = `(excess_demand × fc_rate) / remaining_days` when MD > 100%

---

#### Formula_103.py
Extends Formula_102 with:
- Tiered energy charge rates
- Life line switch charges
- Multiple FC rates based on consumption

**Key Formulas:**
- EC uses tiered rates (0-100 kWh, 101-150 kWh, 151-300 kWh, >300 kWh)
- Life line switch charges when consumption crosses 100 kWh
- FC rate switches based on cumulative consumption

---

## Module: Test Cases (PE_*.py)

### Description
Test case scripts (PE_101.py through PE_225.py) automate end-to-end testing of the prepaid engine.

### Common Structure

Each test case follows this structure:

1. **Configuration Section**: Test parameters
2. **Helper Functions**: Utility functions
3. **Step 1**: Create Account
4. **Step 2**: Fill Daily Load Data
5. **Step 3**: Fill Profile Instant Data
6. **Step 4**: Trigger Prepaid Ledger
7. **Step 5**: Generate Report

### Public Functions (Common to All PE Files)

#### `generate_random_number(length: int) -> str`
Generates a random number string of specified length.

**Parameters:**
- `length` (int): Length of the number string

**Returns:**
- `str`: Random number string

**Example:**
```python
account_id = generate_random_number(10)
# Returns: "1234567890" (random)
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
code = generate_random_alphanumeric(6)
# Returns: "A1B2C3" (random)
```

---

#### `generate_consumer_name() -> str`
Generates a random consumer name.

**Returns:**
- `str`: Random first and last name combination

**Example:**
```python
name = generate_consumer_name()
# Returns: "John Smith" (random)
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
# Returns: 9876543210 (random)
```

---

#### `parse_install_date(date_str: str) -> str`
Parses meter installation date from ISO format to database format.

**Parameters:**
- `date_str` (str): Date in format "2025-10-01T00:00:00" or "2025-10-01 00:00:00"

**Returns:**
- `str`: Date in format "yyyy-mm-dd HH:MM:SS"

**Example:**
```python
db_date = parse_install_date("2025-10-01T00:00:00")
# Returns: "2025-10-01 00:00:00"
```

---

#### `get_month_end_date(start_date_str: str) -> str`
Calculates the first day of the next month (month end + 1 day).

**Parameters:**
- `start_date_str` (str): Start date in format "yyyy-mm-dd HH:MM:SS"

**Returns:**
- `str`: First day of next month in same format

**Example:**
```python
end_date = get_month_end_date("2025-10-01 00:00:00")
# Returns: "2025-11-01 00:00:00"
```

---

#### `create_account() -> Dict[str, Any] | None`
Creates a new account via the account API.

**Returns:**
- `Dict[str, Any]`: Account data dictionary with keys:
  - `accountId`: Generated account ID
  - `meterSrno`: Meter serial number
  - `meterInstalldate`: Meter installation date
  - `badgeNumber`: Badge number
  - `payload`: Full request payload
- `None`: If account creation fails

**Example:**
```python
account_data = create_account()
if account_data:
    print(f"Account created: {account_data['accountId']}")
```

---

#### `fill_daily_load_data(account_data: Dict[str, Any])`
Fills daily load data into the database for the account.

**Parameters:**
- `account_data` (Dict): Account data from `create_account()`

**Process:**
- Connects to PostgreSQL database
- Generates daily load records for each day in the month
- Inserts data into `dailyload_vee_validated` table

**Example:**
```python
fill_daily_load_data(account_data)
```

---

#### `fill_profile_instant_data(account_data: Dict[str, Any])`
Fills profile instant data into the database for the account.

**Parameters:**
- `account_data` (Dict): Account data from `create_account()`

**Process:**
- Connects to PostgreSQL database
- Generates profile instant records
- Inserts data into `profile_instant_vee` table

**Example:**
```python
fill_profile_instant_data(account_data)
```

---

#### `trigger_prepaid_ledger(account_id: str)`
Triggers the prepaid ledger calculation API.

**Parameters:**
- `account_id` (str): Account ID to trigger ledger for

**Returns:**
- API response status

**Example:**
```python
trigger_prepaid_ledger("1234567890")
```

---

#### `fetch_daily_load_data(meter_srno: str) -> pd.DataFrame`
Fetches daily load data from the MDMS API.

**Parameters:**
- `meter_srno` (str): Meter serial number

**Returns:**
- `pd.DataFrame`: Daily load data

**Example:**
```python
df = fetch_daily_load_data("PO12345678")
```

---

#### `fetch_profile_instant_data(meter_srno: str) -> pd.DataFrame`
Fetches profile instant data from the MDMS API.

**Parameters:**
- `meter_srno` (str): Meter serial number

**Returns:**
- `pd.DataFrame`: Profile instant data

**Example:**
```python
df = fetch_profile_instant_data("PO12345678")
```

---

#### `generate_excel_report(account_data: Dict[str, Any])`
Generates a comprehensive Excel report with all test data and results.

**Parameters:**
- `account_data` (Dict): Account data from `create_account()`

**Output:**
- Excel file named `Report_PE_{test_number}.xlsx` with sheets:
  - Consumer Details
  - Daily Load Data
  - Profile Instant Data
  - Prepaid Ledger Data

**Example:**
```python
generate_excel_report(account_data)
# Creates: Report_PE_101.xlsx
```

---

#### `main()`
Main entry point that runs the complete test case workflow.

**Process:**
1. Creates account
2. Fills daily load data
3. Fills profile instant data
4. Triggers prepaid ledger
5. Generates Excel report

**Usage:**
```bash
python Test_Plan/PE_101.py
```

---

## Usage Examples

### Example 1: Extract Consumer Details

```python
from account import process_all_reports, save_to_csv

# Process all Excel reports
df = process_all_reports()

# Save to CSV
save_to_csv(df, "Consumer_details.csv")
```

---

### Example 2: Download Ledger Data

```python
from Download_Ledger import fetch_and_save_data

# Download ledger data for all consumers in CSV
fetch_and_save_data()
# Creates: Prepaid_Ledger_Report.xlsx
```

---

### Example 3: Validate Formula

```python
from Formula.Formula_101 import PrepaidLedgerComparison

# Create comparator
comparator = PrepaidLedgerComparison()

# Run complete validation
comparator.run_comparison()
# Creates: Formula_101.xlsx
# Logs to: logs/Formula_101.log
```

---

### Example 4: Run Test Case

```python
# Run a test case
import sys
sys.path.append('Test_Plan')
from PE_101 import main

main()
# Creates: Report_PE_101.xlsx
# Logs to: logs/PE_101.log
```

---

### Example 5: Complete Workflow

```python
# Step 1: Extract consumer details
from account import main as extract_main
extract_main()

# Step 2: Download ledger data
from Download_Ledger import fetch_and_save_data
fetch_and_save_data()

# Step 3: Validate formulas
from Formula.Formula_101 import PrepaidLedgerComparison
comparator = PrepaidLedgerComparison()
comparator.run_comparison()
```

---

## Configuration

### Database Configuration

All test cases use PostgreSQL database:

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

**Account API:**
- URL: `https://integration1.stage.gomatimvvnl.in/initial_master_sync/`
- Authentication: Bearer token

**Ledger API:**
- Base URL: `https://engine-web.stage.gomatimvvnl.in/daily_prepaid_ledger/`

**MDMS API:**
- Base URL: `https://mdms-api.stage.gomatimvvnl.in/db-service`

### Logging Configuration

All modules use Python's `logging` module:
- Log files are saved in `logs/` directory
- Format: `%(asctime)s - %(levelname)s - %(message)s`
- Level: `INFO`

### Output Files

- `Consumer_details.csv`: Extracted consumer details
- `Prepaid_Ledger_Report.xlsx`: Downloaded ledger data
- `Formula_*.xlsx`: Formula validation reports
- `Report_PE_*.xlsx`: Test case reports

---

## Error Handling

### Common Exceptions

1. **FileNotFoundError**: When required files don't exist
2. **ValueError**: When data format is unexpected
3. **requests.exceptions.RequestException**: When API calls fail
4. **psycopg2.Error**: When database operations fail

### Error Logging

All errors are logged to:
- Console (stdout)
- Log files in `logs/` directory

---

## Dependencies

### Required Python Packages

```
pandas
openpyxl
requests
psycopg2
numpy
```

### Installation

```bash
pip install pandas openpyxl requests psycopg2-binary numpy
```

---

## Notes

1. All date/time values use UTC timezone
2. Excel sheet names are limited to 31 characters
3. API timeouts are set to 30 seconds
4. Floating-point comparisons use tolerance of 0.01
5. Account IDs are 10-digit random numbers
6. Meter serial numbers follow pattern: `PO{last_8_digits_of_account_id}`

---

## Support

For issues or questions, refer to:
- Log files in `logs/` directory
- Excel reports for detailed data
- Test case documentation in each PE_*.py file header
