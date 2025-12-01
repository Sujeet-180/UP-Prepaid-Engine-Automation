# Public API & Usage Guide

This document is auto-generated and lists every public-facing class, function, and script entry point in the repository. Use it as a quick reference for available utilities, their responsibilities, and typical invocation patterns.

## Module `Download_Ledger`

- Path: `Download_Ledger.py`
- CLI entrypoint: `python Download_Ledger.py`

No docstring provided.

**Example**
```python
from Download_Ledger import read_consumer_details

result = read_consumer_details(...)
```

### Functions
#### `read_consumer_details()`
Read account IDs, meter numbers, and Report IDs from CSV file.

#### `fetch_and_save_data()`
Fetch data from API for all consumers in CSV and save to Excel.

---

## Module `Formula.Formula_101`

- Path: `Formula/Formula_101.py`
- CLI entrypoint: `python Formula/Formula_101.py`

No docstring provided.

**Example**
```python
from Formula.Formula_101 import main

result = main(...)
```

### Classes
#### `PrepaidLedgerComparison` (bases: object)
No docstring provided.

Methods:
- `__init__(self)`
  - No docstring provided.
- `fetch_prepaid_ledger_data(self) -> pd.DataFrame`
  - Fetch prepaid ledger data from API
- `calculate_expected_values(self, df: pd.DataFrame) -> pd.DataFrame`
  - Calculate expected values based on our formulas
- `compare_values(self, df: pd.DataFrame) -> pd.DataFrame`
  - Compare calculated vs expected values and generate status
- `generate_comparison_report(self, df: pd.DataFrame, filename: str='Formula_101.xlsx')`
  - Generate comprehensive Excel report with comparison
- `run_comparison(self)`
  - Run the complete comparison process

### Functions
#### `main()`
Main function to run the comparison

---

## Module `Formula.Formula_102`

- Path: `Formula/Formula_102.py`
- CLI entrypoint: `python Formula/Formula_102.py`

No docstring provided.

**Example**
```python
from Formula.Formula_102 import main

result = main(...)
```

### Classes
#### `PrepaidLedgerComparison` (bases: object)
No docstring provided.

Methods:
- `__init__(self)`
  - No docstring provided.
- `fetch_prepaid_ledger_data(self) -> pd.DataFrame`
  - Fetch prepaid ledger data from API
- `calculate_expected_values(self, df: pd.DataFrame) -> pd.DataFrame`
  - Calculate expected values based on our formulas
- `compare_values(self, df: pd.DataFrame) -> pd.DataFrame`
  - Compare calculated vs expected values and generate status
- `generate_comparison_report(self, df: pd.DataFrame, filename: str='Formula_102.xlsx')`
  - Generate comprehensive Excel report with comparison
- `run_comparison(self)`
  - Run the complete comparison process

### Functions
#### `main()`
Main function to run the comparison

---

## Module `Formula.Formula_103`

- Path: `Formula/Formula_103.py`
- CLI entrypoint: `python Formula/Formula_103.py`

No docstring provided.

**Example**
```python
from Formula.Formula_103 import main

result = main(...)
```

### Classes
#### `PrepaidLedgerComparison` (bases: object)
No docstring provided.

Methods:
- `__init__(self)`
  - No docstring provided.
- `fetch_prepaid_ledger_data(self) -> pd.DataFrame`
  - Fetch prepaid ledger data from API
- `calculate_expected_values(self, df: pd.DataFrame) -> pd.DataFrame`
  - Calculate expected values based on our formulas
- `compare_values(self, df: pd.DataFrame) -> pd.DataFrame`
  - Compare calculated vs expected values and generate status
- `generate_comparison_report(self, df: pd.DataFrame, filename: str='Formula_103.xlsx')`
  - Generate comprehensive Excel report with comparison
- `run_comparison(self)`
  - Run the complete comparison process

### Functions
#### `main()`
Main function to run the comparison

---

## Module `Test_Plan.Incremental_Trigger`

- Path: `Test_Plan/Incremental_Trigger.py`
- CLI entrypoint: `python Test_Plan/Incremental_Trigger.py`

Incremental_Trigger.py - Trigger incremental_task API

**Example**
```python
from Test_Plan.Incremental_Trigger import trigger_incremental_task

result = trigger_incremental_task(...)
```

### Functions
#### `trigger_incremental_task()`
Trigger the incremental_task API

Returns:
    bool: True if API call was successful (status 200), False otherwise

---

## Module `Test_Plan.PE_101`

- Path: `Test_Plan/PE_101.py`
- CLI entrypoint: `python Test_Plan/PE_101.py`

PE_101.py - Test Case
Test Case ID: PE_101
Test Case Description: To verify prepaid ledger calculation for ST = 10 (normal 10A), With Consumption = up to 100 kWh and MD = upto 75%.

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_101 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_102`

- Path: `Test_Plan/PE_102.py`
- CLI entrypoint: `python Test_Plan/PE_102.py`

PE_102.py - Test Case
Test Case ID: PE_102
Test Case Description: To verify prepaid ledger calculation for ST = 10 (normal 10A), With Consumption = up to 100 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_102 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_103`

- Path: `Test_Plan/PE_103.py`
- CLI entrypoint: `python Test_Plan/PE_103.py`

PE_103.py - Test Case
Test Case ID: PE_103
Test Case Description: To verify prepaid ledger calculation for ST = 10 (lifeline switch), With Consumption = up to 400 kWh and MD = below 75%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_103 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_104`

- Path: `Test_Plan/PE_104.py`
- CLI entrypoint: `python Test_Plan/PE_104.py`

PE_104.py - Test Case
Test Case ID: PE_104
Test Case Description: To verify prepaid ledger calculation for ST = 10 (lifeline switch), With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_104 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_105`

- Path: `Test_Plan/PE_105.py`
- CLI entrypoint: `python Test_Plan/PE_105.py`

PE_105.py - Test Case
Test Case ID: PE_105
Test Case Description: To verify prepaid ledger calculation for ST = 10 (lifeline switch - less than 3 days of the month)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_105 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_106`

- Path: `Test_Plan/PE_106.py`
- CLI entrypoint: `python Test_Plan/PE_106.py`

PE_106.py - Test Case
Test Case ID: PE_106
Test Case Description: To verify prepaid ledger calculation for ST = 10 (lifeline switch 3 month scanarios)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_106 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `get_three_months_later_date(start_date_str: str) -> str`
Calculate the date 3 months later from the given start date.

#### `get_month_boundaries(start_date_str: str)`
Calculate the end dates for each of the 3 months (last day of each calendar month).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_107`

- Path: `Test_Plan/PE_107.py`
- CLI entrypoint: `python Test_Plan/PE_107.py`

PE_107.py - Test Case
Test Case ID: PE_107
Test Case Description: To verify prepaid ledger calculation for ST = 10 (lifeline switch 4 month scanarios)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_107 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `get_four_months_later_date(start_date_str: str) -> str`
Calculate the date 4 months later from the given start date.

#### `get_month_boundaries(start_date_str: str)`
Calculate the end dates for each of the 4 months.

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_108`

- Path: `Test_Plan/PE_108.py`
- CLI entrypoint: `python Test_Plan/PE_108.py`

PE_108.py - Test Case
Test Case ID: PE_108
Test Case Description: To verify prepaid ledger calculation for ST = 10 (normal 10B), With Consumption = up to 400 kWh and MD = below 75%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_108 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_109`

- Path: `Test_Plan/PE_109.py`
- CLI entrypoint: `python Test_Plan/PE_109.py`

PE_109.py - Test Case
Test Case ID: PE_109
Test Case Description: To verify prepaid ledger calculation for ST = 10 (normal 10B), With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_109 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_110`

- Path: `Test_Plan/PE_110.py`
- CLI entrypoint: `python Test_Plan/PE_110.py`

PE_110.py - Test Case
Test Case ID: PE_110
Test Case Description: To verify prepaid ledger calculation for ST = 10 (normal 10A with green energy)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_110 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_111`

- Path: `Test_Plan/PE_111.py`
- CLI entrypoint: `python Test_Plan/PE_111.py`

PE_111.py - Test Case
Test Case ID: PE_111
Test Case Description: To verify prepaid ledger calculation for ST = 10 (lifeline switch with green energy)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_111 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_112`

- Path: `Test_Plan/PE_112.py`
- CLI entrypoint: `python Test_Plan/PE_112.py`

PE_112.py - Test Case
Test Case ID: PE_112
Test Case Description: To verify prepaid ledger calculation for ST = 10 (normal 10A with meter installation in mid of the month)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_112 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_113`

- Path: `Test_Plan/PE_113.py`
- CLI entrypoint: `python Test_Plan/PE_113.py`

PE_113.py - Test Case
Test Case ID: PE_113
Test Case Description: To verify prepaid ledger calculation for ST = 10 (kVA to kW Conversion)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_113 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_114`

- Path: `Test_Plan/PE_114.py`
- CLI entrypoint: `python Test_Plan/PE_114.py`

PE_114.py - Test Case
Test Case ID: PE_114
Test Case Description: To verify prepaid ledger calculation for ST = 10 (BHP to kW Conversion)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_114 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_115`

- Path: `Test_Plan/PE_115.py`
- CLI entrypoint: `python Test_Plan/PE_115.py`

PE_115.py - Test Case
Test Case ID: PE_115
Test Case Description: To verify prepaid ledger calculation for ST = 10 (normal 10A with FPPAS)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_115 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_116`

- Path: `Test_Plan/PE_116.py`
- CLI entrypoint: `python Test_Plan/PE_116.py`

PE_116.py - Test Case
Test Case ID: PE_116
Test Case Description: To verify prepaid ledger calculation for ST = 10 (lifeline switch with FPPAS)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_116 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_117`

- Path: `Test_Plan/PE_117.py`
- CLI entrypoint: `python Test_Plan/PE_117.py`

PE_117.py - Test Case
Test Case ID: PE_117
Test Case Description: To verify prepaid ledger calculation for ST = 10 with PF Surcharge

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_117 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_118`

- Path: `Test_Plan/PE_118.py`
- CLI entrypoint: `python Test_Plan/PE_118.py`

PE_118.py - Test Case
Test Case ID: PE_118
Test Case Description: To verify prepaid ledger calculation for ST = 10 with PF Surcharge

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_118 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_119`

- Path: `Test_Plan/PE_119.py`
- CLI entrypoint: `python Test_Plan/PE_119.py`

PE_119.py - Test Case
Test Case ID: PE_119
Test Case Description: To verify prepaid ledger calculation for ST = 17 (normal 17A), With Consumption = up to 100 kWh and MD = upto 75%.

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_119 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_120`

- Path: `Test_Plan/PE_120.py`
- CLI entrypoint: `python Test_Plan/PE_120.py`

PE_120.py - Test Case
Test Case ID: PE_120
Test Case Description: To verify prepaid ledger calculation for ST = 17 (normal 17A), With Consumption = up to 100 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_120 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_121`

- Path: `Test_Plan/PE_121.py`
- CLI entrypoint: `python Test_Plan/PE_121.py`

PE_121.py - Test Case
Test Case ID: PE_121   
Test Case Description: To verify prepaid ledger calculation for ST = 17 (lifeline switch), With Consumption = up to 400 kWh and MD = below 75%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_121 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_122`

- Path: `Test_Plan/PE_122.py`
- CLI entrypoint: `python Test_Plan/PE_122.py`

PE_122.py - Test Case
Test Case ID: PE_122
Test Case Description: To verify prepaid ledger calculation for ST = 17 (lifeline switch), With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_122 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_123`

- Path: `Test_Plan/PE_123.py`
- CLI entrypoint: `python Test_Plan/PE_123.py`

PE_123.py - Test Case
Test Case ID: PE_123
Test Case Description: To verify prepaid ledger calculation for ST = 17 (lifeline switch - less than 3 days of the month)

Step 1: Create account with specified parameters
Step 2: Fill daily load data    
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_123 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_124`

- Path: `Test_Plan/PE_124.py`
- CLI entrypoint: `python Test_Plan/PE_124.py`

PE_124.py - Test Case
Test Case ID: PE_124
Test Case Description: To verify prepaid ledger calculation for ST = 17 (lifeline switch 3 month scanarios)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_124 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `get_three_months_later_date(start_date_str: str) -> str`
Calculate the date 3 months later from the given start date.

#### `get_month_boundaries(start_date_str: str)`
Calculate the end dates for each of the 3 months (last day of each calendar month).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_125`

- Path: `Test_Plan/PE_125.py`
- CLI entrypoint: `python Test_Plan/PE_125.py`

PE_125.py - Test Case
Test Case ID: PE_125
Test Case Description: To verify prepaid ledger calculation for ST = 17 (lifeline switch 4 month scanarios)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_125 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `get_four_months_later_date(start_date_str: str) -> str`
Calculate the date 4 months later from the given start date.

#### `get_month_boundaries(start_date_str: str)`
Calculate the end dates for each of the 4 months.

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_126`

- Path: `Test_Plan/PE_126.py`
- CLI entrypoint: `python Test_Plan/PE_126.py`

PE_126.py - Test Case
Test Case ID: PE_126
Test Case Description: To verify prepaid ledger calculation for ST = 17 (normal 17B), With Consumption = up to 400 kWh and MD = below 75%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_126 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_127`

- Path: `Test_Plan/PE_127.py`
- CLI entrypoint: `python Test_Plan/PE_127.py`

PE_127.py - Test Case
Test Case ID: PE_127
Test Case Description: To verify prepaid ledger calculation for ST = 17 (normal 17B), With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_127 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_128`

- Path: `Test_Plan/PE_128.py`
- CLI entrypoint: `python Test_Plan/PE_128.py`

PE_128.py - Test Case
Test Case ID: PE_128
Test Case Description: To verify prepaid ledger calculation for ST = 17 (normal 17A with green energy)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_128 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_129`

- Path: `Test_Plan/PE_129.py`
- CLI entrypoint: `python Test_Plan/PE_129.py`

PE_129.py - Test Case
Test Case ID: PE_129
Test Case Description: To verify prepaid ledger calculation for ST = 17 (lifeline switch with green energy)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_129 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_130`

- Path: `Test_Plan/PE_130.py`
- CLI entrypoint: `python Test_Plan/PE_130.py`

PE_130.py - Test Case
Test Case ID: PE_130
Test Case Description: To verify prepaid ledger calculation for ST = 17 (normal 17A with meter installation in mid of the month)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_130 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_131`

- Path: `Test_Plan/PE_131.py`
- CLI entrypoint: `python Test_Plan/PE_131.py`

PE_131.py - Test Case
Test Case ID: PE_131
Test Case Description: To verify prepaid ledger calculation for ST = 17 (kVA to kW Conversion)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_131 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_132`

- Path: `Test_Plan/PE_132.py`
- CLI entrypoint: `python Test_Plan/PE_132.py`

PE_132.py - Test Case
Test Case ID: PE_132
Test Case Description: To verify prepaid ledger calculation for ST = 17 (BHP to kW Conversion)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_132 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_133`

- Path: `Test_Plan/PE_133.py`
- CLI entrypoint: `python Test_Plan/PE_133.py`

PE_133.py - Test Case
Test Case ID: PE_133
Test Case Description: To verify prepaid ledger calculation for ST = 17 (normal 10A with FPPAS)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_133 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_134`

- Path: `Test_Plan/PE_134.py`
- CLI entrypoint: `python Test_Plan/PE_134.py`

PE_134.py - Test Case
Test Case ID: PE_134
Test Case Description: To verify prepaid ledger calculation for ST = 17 (lifeline switch with FPPAS)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_134 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_135`

- Path: `Test_Plan/PE_135.py`
- CLI entrypoint: `python Test_Plan/PE_135.py`

PE_135.py - Test Case
Test Case ID: PE_135
Test Case Description: To verify prepaid ledger calculation for ST = 17 with PF Surcharge

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_135 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_136`

- Path: `Test_Plan/PE_136.py`
- CLI entrypoint: `python Test_Plan/PE_136.py`

PE_136.py - Test Case
Test Case ID: PE_136
Test Case Description: To verify prepaid ledger calculation for ST = 17 with PF Surcharge

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_136 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_137`

- Path: `Test_Plan/PE_137.py`
- CLI entrypoint: `python Test_Plan/PE_137.py`

PE_137.py - Test Case
Test Case ID: PE_137
Test Case Description: To verify prepaid ledger calculation for ST = 11 With Consumption = up to 400 kVAh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_137 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_138`

- Path: `Test_Plan/PE_138.py`
- CLI entrypoint: `python Test_Plan/PE_138.py`

PE_138.py - Test Case
Test Case ID: PE_138
Test Case Description: To verify prepaid ledger calculation for ST = 11 with green energy

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_138 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_139`

- Path: `Test_Plan/PE_139.py`
- CLI entrypoint: `python Test_Plan/PE_139.py`

PE_139.py - Test Case
Test Case ID: PE_139
Test Case Description: To verify prepaid ledger calculation for ST = 11 (kW to kVA Conversion)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_139 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_140`

- Path: `Test_Plan/PE_140.py`
- CLI entrypoint: `python Test_Plan/PE_140.py`

PE_140.py - Test Case
Test Case ID: PE_140
Test Case Description: To verify prepaid ledger calculation for ST = 11 (BHP to kVA Conversion)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_140 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_141`

- Path: `Test_Plan/PE_141.py`
- CLI entrypoint: `python Test_Plan/PE_141.py`

PE_141.py - Test Case
Test Case ID: PE_141
Test Case Description: To verify prepaid ledger calculation for ST = 12 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_141 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_142`

- Path: `Test_Plan/PE_142.py`
- CLI entrypoint: `python Test_Plan/PE_142.py`

PE_142.py - Test Case
Test Case ID: PE_142
Test Case Description: To verify prepaid ledger calculation for ST = 14 With Consumption = up to 400 kVAh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_142 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_143`

- Path: `Test_Plan/PE_143.py`
- CLI entrypoint: `python Test_Plan/PE_143.py`

PE_143.py - Test Case
Test Case ID: PE_143
Test Case Description: To verify prepaid ledger calculation for ST = 15 With Consumption = up to 400 kVAh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_143 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_144`

- Path: `Test_Plan/PE_144.py`
- CLI entrypoint: `python Test_Plan/PE_144.py`

PE_144.py - Test Case
Test Case ID: PE_144
Test Case Description: To verify prepaid ledger calculation for ST = 18 With Consumption = up to 400 kVAh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_144 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_145`

- Path: `Test_Plan/PE_145.py`
- CLI entrypoint: `python Test_Plan/PE_145.py`

PE_145.py - Test Case
Test Case ID: PE_145
Test Case Description: To verify prepaid ledger calculation for ST = 19 With Consumption = up to 400 kVAh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_145 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_146`

- Path: `Test_Plan/PE_146.py`
- CLI entrypoint: `python Test_Plan/PE_146.py`

PE_146.py - Test Case
Test Case ID: PE_146
Test Case Description: To verify prepaid ledger calculation for ST = 20 (Minimum Monthly Charge - Season 1 where Sanction load Below 4kW)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_146 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_147`

- Path: `Test_Plan/PE_147.py`
- CLI entrypoint: `python Test_Plan/PE_147.py`

PE_147.py - Test Case
Test Case ID: PE_147
Test Case Description: To verify prepaid ledger calculation for ST = 20 (Minimum Monthly Charge - Season 1 where Sanction load Below 4kW with FPPAS)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_147 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_148`

- Path: `Test_Plan/PE_148.py`
- CLI entrypoint: `python Test_Plan/PE_148.py`

PE_148.py - Test Case
Test Case ID: PE_148
Test Case Description: To verify prepaid ledger calculation for ST = 20 (Minimum Monthly Charge - Season 2 where Sanction load Below 4kW)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_148 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_149`

- Path: `Test_Plan/PE_149.py`
- CLI entrypoint: `python Test_Plan/PE_149.py`

PE_149.py - Test Case
Test Case ID: PE_149
Test Case Description: To verify prepaid ledger calculation for ST = 20 (Minimum Monthly Charge - Season 1 where Sanction load Above 4kW)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_149 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_150`

- Path: `Test_Plan/PE_150.py`
- CLI entrypoint: `python Test_Plan/PE_150.py`

PE_150.py - Test Case
Test Case ID: PE_150
Test Case Description: To verify prepaid ledger calculation for ST = 20 (Minimum Monthly Charge - Season 2 where Sanction load Above 4kW)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_150 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_151`

- Path: `Test_Plan/PE_151.py`
- CLI entrypoint: `python Test_Plan/PE_151.py`

PE_151.py - Test Case
Test Case ID: PE_151
Test Case Description: To verify prepaid ledger calculation for ST = 22 (Minimum Monthly Charge - Season 1 where Sanction load Below 4kW)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_151 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_152`

- Path: `Test_Plan/PE_152.py`
- CLI entrypoint: `python Test_Plan/PE_152.py`

PE_152.py - Test Case
Test Case ID: PE_152
Test Case Description: To verify prepaid ledger calculation for ST = 22 (Minimum Monthly Charge - Season 2 where Sanction load Below 4kW)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_152 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_153`

- Path: `Test_Plan/PE_153.py`
- CLI entrypoint: `python Test_Plan/PE_153.py`

PE_153.py - Test Case
Test Case ID: PE_153
Test Case Description: To verify prepaid ledger calculation for ST = 22 (Minimum Monthly Charge - Season 1 where Sanction load Above 4kW)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_153 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_154`

- Path: `Test_Plan/PE_154.py`
- CLI entrypoint: `python Test_Plan/PE_154.py`

PE_154.py - Test Case
Test Case ID: PE_154
Test Case Description: To verify prepaid ledger calculation for ST = 22 (Minimum Monthly Charge - Season 2 where Sanction load Above 4kW)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_154 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_155`

- Path: `Test_Plan/PE_155.py`
- CLI entrypoint: `python Test_Plan/PE_155.py`

PE_155.py - Test Case
Test Case ID: PE_155
Test Case Description: To verify prepaid ledger calculation for ST = 24 (Minimum Monthly Charge - Season 1 where Sanction load Below 4kW)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_155 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_156`

- Path: `Test_Plan/PE_156.py`
- CLI entrypoint: `python Test_Plan/PE_156.py`

PE_156.py - Test Case
Test Case ID: PE_156
Test Case Description: To verify prepaid ledger calculation for ST = 24 (Minimum Monthly Charge - Season 2 where Sanction load Below 4kW)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_156 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_157`

- Path: `Test_Plan/PE_157.py`
- CLI entrypoint: `python Test_Plan/PE_157.py`

PE_157.py - Test Case
Test Case ID: PE_157
Test Case Description: To verify prepaid ledger calculation for ST = 24 (Minimum Monthly Charge - Season 1 where Sanction load Above 4kW)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_157 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_158`

- Path: `Test_Plan/PE_158.py`
- CLI entrypoint: `python Test_Plan/PE_158.py`

PE_158.py - Test Case
Test Case ID: PE_158
Test Case Description: To verify prepaid ledger calculation for ST = 24 (Minimum Monthly Charge - Season 2 where Sanction load Above 4kW)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_158 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_159`

- Path: `Test_Plan/PE_159.py`
- CLI entrypoint: `python Test_Plan/PE_159.py`

PE_159.py - Test Case
Test Case ID: PE_159
Test Case Description: To verify prepaid ledger calculation for ST = 24B With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_159 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_160`

- Path: `Test_Plan/PE_160.py`
- CLI entrypoint: `python Test_Plan/PE_160.py`

PE_160.py - Test Case
Test Case ID: PE_160
Test Case Description: To verify prepaid ledger calculation for ST = 24C With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_160 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_161`

- Path: `Test_Plan/PE_161.py`
- CLI entrypoint: `python Test_Plan/PE_161.py`

PE_161.py - Test Case
Test Case ID: PE_161
Test Case Description: To verify prepaid ledger calculation for ST = 24D With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_161 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_162`

- Path: `Test_Plan/PE_162.py`
- CLI entrypoint: `python Test_Plan/PE_162.py`

PE_162.py - Test Case
Test Case ID: PE_162
Test Case Description: To verify prepaid ledger calculation for ST = 25 (Powerlooom Below 5kW - Urban)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_162 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_163`

- Path: `Test_Plan/PE_163.py`
- CLI entrypoint: `python Test_Plan/PE_163.py`

PE_163.py - Test Case
Test Case ID: PE_163
Test Case Description: To verify prepaid ledger calculation for ST = 26 (Powerlooom Below 5kW - Rural)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_163 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_164`

- Path: `Test_Plan/PE_164.py`
- CLI entrypoint: `python Test_Plan/PE_164.py`

PE_164.py - Test Case
Test Case ID: PE_164
Test Case Description: To verify prepaid ledger calculation for ST = 27 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_164 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_165`

- Path: `Test_Plan/PE_165.py`
- CLI entrypoint: `python Test_Plan/PE_165.py`

PE_165.py - Test Case
Test Case ID: PE_165
Test Case Description: To verify prepaid ledger calculation for ST = 28 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_165 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_166`

- Path: `Test_Plan/PE_166.py`
- CLI entrypoint: `python Test_Plan/PE_166.py`

PE_166.py - Test Case
Test Case ID: PE_166
Test Case Description: To verify prepaid ledger calculation for ST = 33 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_166 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_167`

- Path: `Test_Plan/PE_167.py`
- CLI entrypoint: `python Test_Plan/PE_167.py`

PE_167.py - Test Case
Test Case ID: PE_167
Test Case Description: To verify prepaid ledger calculation for ST = 34 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_167 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_168`

- Path: `Test_Plan/PE_168.py`
- CLI entrypoint: `python Test_Plan/PE_168.py`

PE_168.py - Test Case
Test Case ID: PE_168
Test Case Description: To verify prepaid ledger calculation for ST = 35 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_168 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_169`

- Path: `Test_Plan/PE_169.py`
- CLI entrypoint: `python Test_Plan/PE_169.py`

PE_169.py - Test Case
Test Case ID: PE_169
Test Case Description: To verify prepaid ledger calculation for ST = 36 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_169 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_170`

- Path: `Test_Plan/PE_170.py`
- CLI entrypoint: `python Test_Plan/PE_170.py`

PE_170.py - Test Case
Test Case ID: PE_170
Test Case Description: To verify prepaid ledger calculation for ST = 37 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_170 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_171`

- Path: `Test_Plan/PE_171.py`
- CLI entrypoint: `python Test_Plan/PE_171.py`

PE_171.py - Test Case
Test Case ID: PE_171
Test Case Description: To verify prepaid ledger calculation for ST = 38 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_171 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_172`

- Path: `Test_Plan/PE_172.py`
- CLI entrypoint: `python Test_Plan/PE_172.py`

PE_172.py - Test Case
Test Case ID: PE_172
Test Case Description: To verify prepaid ledger calculation for ST = 40 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_172 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_173`

- Path: `Test_Plan/PE_173.py`
- CLI entrypoint: `python Test_Plan/PE_173.py`

PE_173.py - Test Case
Test Case ID: PE_173
Test Case Description: To verify prepaid ledger calculation for ST = 40A With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_173 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_174`

- Path: `Test_Plan/PE_174.py`
- CLI entrypoint: `python Test_Plan/PE_174.py`

PE_174.py - Test Case
Test Case ID: PE_174
Test Case Description: To verify prepaid ledger calculation for ST = 41 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_174 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_175`

- Path: `Test_Plan/PE_175.py`
- CLI entrypoint: `python Test_Plan/PE_175.py`

PE_175.py - Test Case
Test Case ID: PE_175
Test Case Description: To verify prepaid ledger calculation for ST = 41A With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_175 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_176`

- Path: `Test_Plan/PE_176.py`
- CLI entrypoint: `python Test_Plan/PE_176.py`

PE_176.py - Test Case
Test Case ID: PE_176
Test Case Description: To verify prepaid ledger calculation for ST = 42 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_176 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_177`

- Path: `Test_Plan/PE_177.py`
- CLI entrypoint: `python Test_Plan/PE_177.py`

PE_177.py - Test Case
Test Case ID: PE_177
Test Case Description: To verify prepaid ledger calculation for ST = 42A With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_177 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_178`

- Path: `Test_Plan/PE_178.py`
- CLI entrypoint: `python Test_Plan/PE_178.py`

PE_178.py - Test Case
Test Case ID: PE_178
Test Case Description: To verify prepaid ledger calculation for ST = 43 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_178 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_179`

- Path: `Test_Plan/PE_179.py`
- CLI entrypoint: `python Test_Plan/PE_179.py`

PE_179.py - Test Case
Test Case ID: PE_179
Test Case Description: To verify prepaid ledger calculation for ST = 44 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_179 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_180`

- Path: `Test_Plan/PE_180.py`
- CLI entrypoint: `python Test_Plan/PE_180.py`

PE_180.py - Test Case
Test Case ID: PE_180
Test Case Description: To verify prepaid ledger calculation for ST = 45 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_180 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_181`

- Path: `Test_Plan/PE_181.py`
- CLI entrypoint: `python Test_Plan/PE_181.py`

PE_181.py - Test Case
Test Case ID: PE_181
Test Case Description: To verify prepaid ledger calculation for ST = 46 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_181 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_182`

- Path: `Test_Plan/PE_182.py`
- CLI entrypoint: `python Test_Plan/PE_182.py`

PE_182.py - Test Case
Test Case ID: PE_182
Test Case Description: To verify prepaid ledger calculation for ST = 47 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_182 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_183`

- Path: `Test_Plan/PE_183.py`
- CLI entrypoint: `python Test_Plan/PE_183.py`

PE_183.py - Test Case
Test Case ID: PE_183
Test Case Description: To verify prepaid ledger calculation for ST = 48 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_183 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_184`

- Path: `Test_Plan/PE_184.py`
- CLI entrypoint: `python Test_Plan/PE_184.py`

PE_184.py - Test Case
Test Case ID: PE_184
Test Case Description: To verify prepaid ledger calculation for ST = 51 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_184 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_185`

- Path: `Test_Plan/PE_185.py`
- CLI entrypoint: `python Test_Plan/PE_185.py`

PE_185.py - Test Case
Test Case ID: PE_185
Test Case Description: To verify prepaid ledger calculation for ST = 52 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_185 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_186`

- Path: `Test_Plan/PE_186.py`
- CLI entrypoint: `python Test_Plan/PE_186.py`

PE_186.py - Test Case
Test Case ID: PE_186
Test Case Description: To verify prepaid ledger calculation for ST = 53 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_186 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_187`

- Path: `Test_Plan/PE_187.py`
- CLI entrypoint: `python Test_Plan/PE_187.py`

PE_187.py - Test Case
Test Case ID: PE_187
Test Case Description: To verify prepaid ledger calculation for ST = 54 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_187 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_188`

- Path: `Test_Plan/PE_188.py`
- CLI entrypoint: `python Test_Plan/PE_188.py`

PE_188.py - Test Case
Test Case ID: PE_188
Test Case Description: To verify prepaid ledger calculation for ST = 55 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_188 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_189`

- Path: `Test_Plan/PE_189.py`
- CLI entrypoint: `python Test_Plan/PE_189.py`

PE_189.py - Test Case
Test Case ID: PE_189
Test Case Description: To verify prepaid ledger calculation for ST = 56 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_189 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_190`

- Path: `Test_Plan/PE_190.py`
- CLI entrypoint: `python Test_Plan/PE_190.py`

PE_190.py - Test Case
Test Case ID: PE_190
Test Case Description: To verify prepaid ledger calculation for ST = 57 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_190 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_191`

- Path: `Test_Plan/PE_191.py`
- CLI entrypoint: `python Test_Plan/PE_191.py`

PE_191.py - Test Case
Test Case ID: PE_191
Test Case Description: To verify prepaid ledger calculation for ST = 58 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_191 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_192`

- Path: `Test_Plan/PE_192.py`
- CLI entrypoint: `python Test_Plan/PE_192.py`

PE_192.py - Test Case
Test Case ID: PE_192
Test Case Description: To verify prepaid ledger calculation for ST = 60 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_192 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_193`

- Path: `Test_Plan/PE_193.py`
- CLI entrypoint: `python Test_Plan/PE_193.py`

PE_193.py - Test Case
Test Case ID: PE_193
Test Case Description: To verify prepaid ledger calculation for ST = 60 (seasonal benefits) With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_193 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_194`

- Path: `Test_Plan/PE_194.py`
- CLI entrypoint: `python Test_Plan/PE_194.py`

PE_194.py - Test Case
Test Case ID: PE_194
Test Case Description: To verify prepaid ledger calculation for ST = 61 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_194 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_195`

- Path: `Test_Plan/PE_195.py`
- CLI entrypoint: `python Test_Plan/PE_195.py`

PE_195.py - Test Case
Test Case ID: PE_195
Test Case Description: To verify prepaid ledger calculation for ST = 63 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_195 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_196`

- Path: `Test_Plan/PE_196.py`
- CLI entrypoint: `python Test_Plan/PE_196.py`

PE_196.py - Test Case
Test Case ID: PE_196
Test Case Description: To verify prepaid ledger calculation for ST = 64 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_196 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_197`

- Path: `Test_Plan/PE_197.py`
- CLI entrypoint: `python Test_Plan/PE_197.py`

PE_197.py - Test Case
Test Case ID: PE_197
Test Case Description: To verify prepaid ledger calculation for ST = 62T (ToU - season 1)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_197 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_198`

- Path: `Test_Plan/PE_198.py`
- CLI entrypoint: `python Test_Plan/PE_198.py`

PE_198.py - Test Case
Test Case ID: PE_198
Test Case Description: To verify prepaid ledger calculation for ST = 62T (ToU - season 2)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_198 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_199`

- Path: `Test_Plan/PE_199.py`
- CLI entrypoint: `python Test_Plan/PE_199.py`

PE_199.py - Test Case
Test Case ID: PE_199
Test Case Description: To verify prepaid ledger calculation for ST = 65 (Powerlooom Above 5kW - Rural)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_199 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_200`

- Path: `Test_Plan/PE_200.py`
- CLI entrypoint: `python Test_Plan/PE_200.py`

PE_200.py - Test Case
Test Case ID: PE_200
Test Case Description: To verify prepaid ledger calculation for ST = 66 (Powerlooom Above 5kW - Rural)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_200 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_201`

- Path: `Test_Plan/PE_201.py`
- CLI entrypoint: `python Test_Plan/PE_201.py`

PE_201.py - Test Case
Test Case ID: PE_201
Test Case Description: To verify prepaid ledger calculation for ST = 67 (Powerlooom Above 5kW - Urban)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_201 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_202`

- Path: `Test_Plan/PE_202.py`
- CLI entrypoint: `python Test_Plan/PE_202.py`

PE_202.py - Test Case
Test Case ID: PE_202
Test Case Description: To verify prepaid ledger calculation for ST = 68 (Powerlooom Above 5kW - Urban)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_202 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_203`

- Path: `Test_Plan/PE_203.py`
- CLI entrypoint: `python Test_Plan/PE_203.py`

PE_203.py - Test Case
Test Case ID: PE_203
Test Case Description: To verify prepaid ledger calculation for ST = 72 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_203 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_204`

- Path: `Test_Plan/PE_204.py`
- CLI entrypoint: `python Test_Plan/PE_204.py`

PE_204.py - Test Case
Test Case ID: PE_204
Test Case Description: To verify prepaid ledger calculation for ST = 73 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_204 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_205`

- Path: `Test_Plan/PE_205.py`
- CLI entrypoint: `python Test_Plan/PE_205.py`

PE_205.py - Test Case
Test Case ID: PE_205
Test Case Description: To verify prepaid ledger calculation for ST = 74 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_205 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_206`

- Path: `Test_Plan/PE_206.py`
- CLI entrypoint: `python Test_Plan/PE_206.py`

PE_206.py - Test Case
Test Case ID: PE_206
Test Case Description: To verify prepaid ledger calculation for ST = 75 With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_206 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_207`

- Path: `Test_Plan/PE_207.py`
- CLI entrypoint: `python Test_Plan/PE_207.py`

PE_207.py - Test Case
Test Case ID: PE_207
Test Case Description: To verify prepaid ledger calculation for ST = 76R With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_207 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_208`

- Path: `Test_Plan/PE_208.py`
- CLI entrypoint: `python Test_Plan/PE_208.py`

PE_208.py - Test Case
Test Case ID: PE_208
Test Case Description: To verify prepaid ledger calculation for ST = 76U With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_208 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_209`

- Path: `Test_Plan/PE_209.py`
- CLI entrypoint: `python Test_Plan/PE_209.py`

PE_209.py - Test Case
Test Case ID: PE_209
Test Case Description: To verify prepaid ledger calculation for ST = 77R With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_209 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_210`

- Path: `Test_Plan/PE_210.py`
- CLI entrypoint: `python Test_Plan/PE_210.py`

PE_210.py - Test Case
Test Case ID: PE_210
Test Case Description: To verify prepaid ledger calculation for ST = 77U With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_210 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_211`

- Path: `Test_Plan/PE_211.py`
- CLI entrypoint: `python Test_Plan/PE_211.py`

PE_211.py - Test Case
Test Case ID: PE_211
Test Case Description: To verify prepaid ledger calculation for ST = 92 (Weekly minimum charge)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_211 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_212`

- Path: `Test_Plan/PE_212.py`
- CLI entrypoint: `python Test_Plan/PE_212.py`

PE_212.py - Test Case
Test Case ID: PE_212
Test Case Description: To verify prepaid ledger calculation for ST = 93 (Weekly minimum charge)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_212 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_213`

- Path: `Test_Plan/PE_213.py`
- CLI entrypoint: `python Test_Plan/PE_213.py`

PE_213.py - Test Case
Test Case ID: PE_213
Test Case Description: To verify prepaid ledger calculation for ST = 94 (Weekly minimum charge)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_213 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_214`

- Path: `Test_Plan/PE_214.py`
- CLI entrypoint: `python Test_Plan/PE_214.py`

PE_214.py - Test Case
Test Case ID: PE_214
Test Case Description: To verify prepaid ledger calculation for ST = 95 (Weekly minimum charge)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_214 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_215`

- Path: `Test_Plan/PE_215.py`
- CLI entrypoint: `python Test_Plan/PE_215.py`

PE_215.py - Test Case
Test Case ID: PE_215
Test Case Description: To verify prepaid ledger calculation for ST = 92 (Weekly minimum charge + Temporary Consumer)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_215 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_216`

- Path: `Test_Plan/PE_216.py`
- CLI entrypoint: `python Test_Plan/PE_216.py`

PE_216.py - Test Case
Test Case ID: PE_216
Test Case Description: To verify prepaid ledger calculation for ST = 93 (Weekly minimum charge + Temporary Consumer)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_216 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_217`

- Path: `Test_Plan/PE_217.py`
- CLI entrypoint: `python Test_Plan/PE_217.py`

PE_217.py - Test Case
Test Case ID: PE_217
Test Case Description: To verify prepaid ledger calculation for ST = 94 (Weekly minimum charge + Temporary Consumer)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_217 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_218`

- Path: `Test_Plan/PE_218.py`
- CLI entrypoint: `python Test_Plan/PE_218.py`

PE_218.py - Test Case
Test Case ID: PE_218
Test Case Description: To verify prepaid ledger calculation for ST = 95 (Weekly minimum charge + Temporary Consumer)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_218 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_219`

- Path: `Test_Plan/PE_219.py`
- CLI entrypoint: `python Test_Plan/PE_219.py`

PE_219.py - Test Case
Test Case ID: PE_219
Test Case Description: To verify prepaid ledger calculation for ST = 92 (3rd year ownward EC rate increase 10%)

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_219 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_220`

- Path: `Test_Plan/PE_220.py`
- CLI entrypoint: `python Test_Plan/PE_220.py`

PE_220.py - Test Case
Test Case ID: PE_220
Test Case Description: To verify prepaid ledger calculation for ST = 11A With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_220 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_221`

- Path: `Test_Plan/PE_221.py`
- CLI entrypoint: `python Test_Plan/PE_221.py`

PE_221.py - Test Case
Test Case ID: PE_221
Test Case Description: To verify prepaid ledger calculation for ST = 11B With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_221 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_222`

- Path: `Test_Plan/PE_222.py`
- CLI entrypoint: `python Test_Plan/PE_222.py`

PE_222.py - Test Case
Test Case ID: PE_222
Test Case Description: To verify prepaid ledger calculation for ST = 11C With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_222 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_223`

- Path: `Test_Plan/PE_223.py`
- CLI entrypoint: `python Test_Plan/PE_223.py`

PE_223.py - Test Case
Test Case ID: PE_223
Test Case Description: To verify prepaid ledger calculation for ST = 11F With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_223 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_224`

- Path: `Test_Plan/PE_224.py`
- CLI entrypoint: `python Test_Plan/PE_224.py`

PE_224.py - Test Case
Test Case ID: PE_224
Test Case Description: To verify prepaid ledger calculation for ST = 11G With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_224 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `Test_Plan.PE_225`

- Path: `Test_Plan/PE_225.py`
- CLI entrypoint: `python Test_Plan/PE_225.py`

PE_225.py - Test Case
Test Case ID: PE_225
Test Case Description: To verify prepaid ledger calculation for ST = 11H With Consumption = up to 400 kWh and MD = upto 150%

Step 1: Create account with specified parameters
Step 2: Fill daily load data
Step 3: Fill profile instant data
Step 4: Trigger prepaid ledger APIs

**Example**
```python
from Test_Plan.PE_225 import generate_random_number

result = generate_random_number(...)
```

### Functions
#### `generate_random_number(length)`
Generate a random number string of specified length

#### `generate_random_alphanumeric(length)`
Generate a random alphanumeric string of specified length

#### `generate_consumer_name()`
Generate a random consumer name

#### `generate_email(consumer_name)`
Generate an email based on consumer name and 3 digit number

#### `generate_mobile_number()`
Generate a random 10-digit mobile number

#### `parse_install_date(date_str: str) -> str`
Parse meterInstalldate from format (2025-10-01T00:00:00) to (yyyy-mm-dd 00:00:00).

#### `get_month_end_date(start_date_str: str) -> str`
Calculate the first day of the next month from the given start date (month end + 1 day).

#### `create_account()`
Step 1: Create account with specified parameters

#### `fill_daily_load_data(account_data)`
Step 2: Fill daily load data

#### `fill_profile_instant_data(account_data)`
Step 3: Fill profile instant data

#### `trigger_prepaid_ledger(account_id)`
Step 4: Trigger prepaid ledger APIs

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `fetch_daily_load_data(meter_srno)`
Fetch daily load data from MDMS API

#### `fetch_profile_instant_data(meter_srno)`
Fetch profile instant data from MDMS API

#### `generate_excel_report(account_data)`
Step 5: Generate Excel report with all test data

#### `main()`
Main function to execute all steps

---

## Module `account`

- Path: `account.py`
- CLI entrypoint: `python account.py`

account.py - Extract Consumer Details from Excel Reports
Reads all Report_PE_*.xlsx files from Result_File folder,
extracts Consumer Details sheet data with specified columns,
and saves to Consumer_details.csv

**Example**
```python
from account import get_report_identifier

result = get_report_identifier(...)
```

### Functions
#### `get_report_identifier(filename: str) -> str`
Extract report identifier from filename.
Example: Report_PE_101.xlsx -> Report_PE_101

#### `extract_consumer_details(excel_file: str) -> pd.DataFrame`
Extract consumer details from a single Excel file.
The Excel sheet has a key-value structure (Parameter/Value columns).

Args:
    excel_file: Path to the Excel file

Returns:
    DataFrame with consumer details including report identifier

#### `process_all_reports() -> pd.DataFrame`
Process all Excel report files in the Result_File folder.

Returns:
    Combined DataFrame with all consumer details

#### `save_to_csv(df: pd.DataFrame, output_file: str)`
Save DataFrame to CSV file.

Args:
    df: DataFrame to save
    output_file: Output CSV filename

#### `main()`
Main function to extract and save consumer details.

---
