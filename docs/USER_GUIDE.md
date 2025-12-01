# UP Prepaid Engine Automation - User Guide

## Quick Start

This guide will help you get started with the UP Prepaid Engine Automation framework quickly.

### Prerequisites

Before using this framework, ensure you have:

1. **Python 3.8+** installed
2. **Required packages** installed:
   ```bash
   pip install pandas openpyxl requests psycopg2-binary numpy
   ```
3. **Network access** to:
   - `https://integration1.stage.gomatimvvnl.in`
   - `https://engine-web.stage.gomatimvvnl.in`
   - `https://mdms-api.stage.gomatimvvnl.in`
   - Database: `db_mdms.stage.mvvnl.internal:5432`

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd UP-Prepaid-Engine-Automation

# Create required directories
mkdir -p logs Result_File
```

---

## Usage Examples

### 1. Running a Test Case

Test cases validate the prepaid engine billing calculations by creating accounts, generating test data, and triggering the billing engine.

#### Run a Single Test Case

```bash
# Run PE_101 test case
python Test_Plan/PE_101.py
```

**Expected Output:**
```
================================================================================
PE_101 Test Plan - Starting Complete Process
================================================================================
Initiating Step 1: Account Creation
Generated Account ID: 4829176304
Generated Meter Serial No: PO29176304
Account created successfully!
Step 1 completed successfully
...
================================================================================
PE_101 Test Plan - All Steps Completed Successfully!
================================================================================
Account ID: 4829176304
Meter Serial No: PO29176304
Meter Install Date: 2025-11-01T00:00:00
Excel Report: Result_File/Report_PE_101.xlsx
================================================================================
```

#### Run Multiple Test Cases

```bash
# Run test cases PE_101 through PE_105
for i in {101..105}; do
    python Test_Plan/PE_$i.py
done
```

---

### 2. Extracting Consumer Details

After running test cases, extract all consumer details into a single CSV file.

```bash
python account.py
```

**Expected Output:**
```
============================================================
Consumer Details Extraction Tool
============================================================
Found 5 Excel file(s) to process...
Processing: Report_PE_101.xlsx...
  - Extracted 1 record(s)
Processing: Report_PE_102.xlsx...
  - Extracted 1 record(s)
...
Total records extracted: 5

Data saved successfully to 'Consumer_details.csv'
Columns: Report_ID, accountId, meterSrno, supplyTypecode, sanctionedLoad, loadUnit, meterInstalldate, greenEnergyflag, prepaidOpeningbalance
```

**Output File (`Consumer_details.csv`):**
```csv
Report_ID,accountId,meterSrno,supplyTypecode,sanctionedLoad,loadUnit,meterInstalldate,greenEnergyflag,prepaidOpeningbalance
Report_PE_101,4829176304,PO29176304,10,1.0,KW,2025-11-01T00:00:00,N,4000.0
Report_PE_102,5918273645,PO18273645,10,1.0,KW,2025-11-01T00:00:00,N,4000.0
```

---

### 3. Downloading Ledger Data

Download prepaid ledger data for all consumers in the CSV file.

```bash
python Download_Ledger.py
```

**Expected Output:**
```
Starting ledger data download...
==================================================
Found 5 consumer(s) to process...
Processing Report_PE_101 (Account: 4829176304, Meter: PO29176304)...
  [OK] Data fetched successfully
Processing Report_PE_102 (Account: 5918273645, Meter: PO18273645)...
  [OK] Data fetched successfully
...
==================================================
SUCCESS: Excel file saved successfully!
Location: /workspace/Prepaid_Ledger_Report.xlsx
Total processed: 5
Successful: 5
Errors: 0
```

---

### 4. Validating Formula Calculations

Use formula validation scripts to verify billing calculations against expected formulas.

#### Basic Validation (Formula_101)

```bash
python Formula/Formula_101.py
```

**Log Output:**
```
2025-01-01 10:00:00 - INFO - Test Case ID : Formula_101 - Prepaid Ledger Comparison
2025-01-01 10:00:00 - INFO - Account ID: 2222550011
2025-01-01 10:00:00 - INFO - Date Range: 2025-10-01T00:00:00 to 2025-11-01T00:00:00
2025-01-01 10:00:01 - INFO - Fetched 31 records for date range...
2025-01-01 10:00:01 - INFO - **********DAY 1 - 2025-10-01************
2025-01-01 10:00:01 - INFO - Daily Consumption: 3.2258 kWh
2025-01-01 10:00:01 - INFO - Daily EC: 3.2258 x 3 = 9.6774 Rs.
2025-01-01 10:00:01 - INFO - Daily FC: (0.75 x 1 x 50) / 31 = 1.2097 Rs.
...
2025-01-01 10:00:02 - INFO - Test Case Result: PASS
2025-01-01 10:00:02 - INFO - Total Records: 31
2025-01-01 10:00:02 - INFO - Passed Records: 31
2025-01-01 10:00:02 - INFO - Failed Records: 0
2025-01-01 10:00:02 - INFO - Success Rate: 100.0000%
```

**Output File (`Formula_101.xlsx`):**
- Sheet: `Prepaid_Ledger` with actual vs expected value comparison

---

### 5. Triggering Incremental Processing

Trigger the incremental task to process any pending ledger calculations.

```bash
python Test_Plan/Incremental_Trigger.py
```

**Expected Output:**
```
2025-01-01 10:00:00 - INFO - Calling API 2: https://engine-web.stage.gomatimvvnl.in/trigger_task/incremental_task/
2025-01-01 10:00:01 - INFO - API 2 Response Status: 200
2025-01-01 10:00:01 - INFO - API 2 (incremental_task) called successfully
2025-01-01 10:00:01 - INFO - Incremental task triggered successfully
```

---

## Complete Workflow Example

Here's a complete workflow for running a full validation cycle:

```bash
#!/bin/bash
# Full validation workflow

# Step 1: Create necessary directories
mkdir -p logs Result_File

# Step 2: Run a batch of test cases
echo "Running test cases..."
for i in 101 102 103 104 105; do
    echo "Running PE_$i..."
    python Test_Plan/PE_$i.py
done

# Step 3: Trigger incremental processing
echo "Triggering incremental processing..."
python Test_Plan/Incremental_Trigger.py

# Step 4: Extract consumer details
echo "Extracting consumer details..."
python account.py

# Step 5: Download ledger data
echo "Downloading ledger data..."
python Download_Ledger.py

# Step 6: Validate formulas
echo "Validating formulas..."
python Formula/Formula_101.py

echo "Workflow complete!"
```

---

## Understanding Test Cases

### Test Case Naming Convention

| Pattern | Description |
|---------|-------------|
| PE_101-PE_110 | Supply Type 10 (Normal 10A) scenarios |
| PE_111-PE_120 | Different consumption ranges |
| PE_121-PE_130 | Max demand penalty scenarios |
| PE_131-PE_150 | Life line switch scenarios |
| PE_151-PE_200 | Special tariff scenarios |
| PE_201-PE_225 | Edge cases and error conditions |

### Key Test Parameters

Each test case configures:

1. **Supply Type Code** - Determines the tariff structure
2. **Sanctioned Load** - Contracted load in kW
3. **Opening Balance** - Initial wallet balance
4. **End Wh** - Target energy consumption
5. **MD_W** - Target maximum demand

### Example Test Case Configuration

```python
# PE_101 Configuration (Basic Scenario)
SUPPLY_TYPECODE = "10"           # Normal 10A
SANCTIONED_LOAD = 1              # 1 kW
PREPAID_OPENING_BALANCE = 4000   # Rs. 4000
END_WH = 100000                  # 100 kWh for the month
MD_W = 750                       # 0.75 kW (75% of load)
```

---

## Reading Output Files

### Excel Report Structure

Each test case generates an Excel report with 4 sheets:

#### Sheet 1: Summary
| Column | Description |
|--------|-------------|
| Test Case ID | Unique test identifier |
| Test Case Description | What the test validates |
| Account ID | Generated account ID |
| Meter Number | Generated meter number |
| Status | Completed/Failed |

#### Sheet 2: Consumer Details
Contains all account parameters in key-value format:
```
Parameter           | Value
--------------------|------------------
accountId           | 4829176304
meterSrno           | PO29176304
supplyTypecode      | 10
sanctionedLoad      | 1.0
...
```

#### Sheet 3: Daily Load
Daily meter readings:
```
dailyload_datetime | badge_number | import_Wh | export_Wh
2025-11-01         | PO29176304   | 3225      | 24
2025-11-02         | PO29176304   | 6451      | 48
...
```

#### Sheet 4: Profile Instant
Profile instant data with max demand:
```
data_timestamp | badge_number | MD_W | MD_VA | voltage
2025-11-01     | PO29176304   | 0    | 0     | 230
2025-11-02     | PO29176304   | 25   | 27    | 230
...
```

---

## Formula Validation Reports

### Report Structure

The formula validation Excel report contains:

| Column Type | Description |
|-------------|-------------|
| Actual Values | Values from API response |
| Expected Values | Calculated values based on formulas |
| Status | "All Match" or list of mismatched columns |

### Understanding Status

- **All Match** - All values match within tolerance (±0.01)
- **Column Names Listed** - Specific columns that don't match

**Example:**
```
Status: daily_consumption_in_rupees, daily_fixed_charges
```
This means EC and FC calculations have discrepancies.

---

## Troubleshooting

### Common Issues

#### 1. Database Connection Failed

**Error:**
```
Error filling daily load data: could not connect to server
```

**Solution:**
- Verify network connectivity to database server
- Check database credentials in `DB_CONFIG`
- Ensure VPN connection if required

#### 2. API Request Failed

**Error:**
```
Account creation failed with status 401
```

**Solution:**
- Verify API authorization token is valid
- Check API endpoint accessibility
- Review request payload format

#### 3. No Excel Files Found

**Error:**
```
No Excel files found in 'Result_File' folder!
```

**Solution:**
- Run test cases first to generate reports
- Verify file naming pattern matches `Report_PE_*.xlsx`

#### 4. Module Import Error

**Error:**
```
ModuleNotFoundError: No module named 'openpyxl'
```

**Solution:**
```bash
pip install openpyxl pandas requests psycopg2-binary numpy
```

### Checking Logs

All operations are logged to the `logs/` directory:

```bash
# View recent logs
tail -f logs/PE_101.log

# View formula validation logs
tail -f logs/Formula_101.log

# View all log files
ls -la logs/
```

---

## Advanced Usage

### Custom Test Parameters

To create a test with custom parameters, modify the configuration section:

```python
# Custom configuration for a new test scenario
SUPPLY_TYPECODE = "20"           # Different supply type
SANCTIONED_LOAD = 5              # 5 kW
PREPAID_OPENING_BALANCE = 10000  # Higher balance
END_WH = 500000                  # Higher consumption
MD_W = 4500                      # 90% of load
```

### Programmatic Usage

Use the modules programmatically in your own scripts:

```python
# Import test case functions
from Test_Plan.PE_101 import create_account, fill_daily_load_data

# Create an account programmatically
account_data = create_account()
if account_data:
    print(f"Created account: {account_data['accountId']}")
    
    # Fill test data
    fill_daily_load_data(account_data)
```

### Batch Processing

```python
import os
import importlib

# Run multiple test cases
test_cases = ['PE_101', 'PE_102', 'PE_103']

for test_id in test_cases:
    module = importlib.import_module(f'Test_Plan.{test_id}')
    try:
        module.main()
        print(f"{test_id}: SUCCESS")
    except Exception as e:
        print(f"{test_id}: FAILED - {e}")
```

---

## Support

For issues or questions:

1. Check the logs in `logs/` directory
2. Review the API Reference documentation
3. Verify all prerequisites are installed
4. Check network connectivity to required services

---

*User Guide for UP Prepaid Engine Automation Framework v1.0*
