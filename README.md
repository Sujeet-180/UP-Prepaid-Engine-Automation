# UP Prepaid Engine Automation Framework

A comprehensive automation testing framework for validating UP Prepaid Engine calculations, including energy consumption charges, fixed charges, electricity duty, rebates, and balance management.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Modules](#core-modules)
- [Formula Validation](#formula-validation)
- [Test Plans](#test-plans)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## Overview

This framework automates the testing and validation of prepaid electricity ledger calculations for the Uttar Pradesh electricity distribution system. It provides:

- **Test Case Execution**: Automated test case creation and execution (PE_101 through PE_225)
- **Formula Validation**: Validation of complex billing formulas (Formula_101, Formula_102, Formula_103)
- **Data Management**: Consumer data extraction and ledger data download
- **Reporting**: Comprehensive Excel reports and detailed logging

---

## Features

✅ **Automated Test Case Execution**
- Create test accounts with random data
- Generate daily load and max demand data
- Trigger prepaid ledger calculations
- Generate detailed Excel reports

✅ **Formula Validation**
- Basic flat-rate calculations (Formula_101)
- Max demand penalties and adjustments (Formula_102)
- Tiered rates with lifeline switch (Formula_103)
- Actual vs Expected comparison with tolerance

✅ **Data Processing**
- Extract consumer details from Excel reports
- Download ledger data from API
- CSV export for bulk operations
- Error tracking and logging

✅ **Comprehensive Reporting**
- Excel reports with multiple sheets
- Detailed logs for debugging
- Pass/fail status with mismatch analysis
- Progress tracking

---

## Project Structure

```
UP-Prepaid-Engine-Automation/
├── account.py                    # Extract consumer details from Excel reports
├── Download_Ledger.py            # Download ledger data from API
│
├── Formula/                      # Formula validation scripts
│   ├── Formula_101.py           # Basic flat-rate validation
│   ├── Formula_102.py           # Max demand validation
│   ├── Formula_103.py           # Tiered rate validation
│   └── ...
│
├── Test_Plan/                    # Test case execution scripts
│   ├── PE_101.py                # Test: ST=10, ≤100kWh, ≤75%MD
│   ├── PE_102.py                # Test: ST=10, varying MD
│   ├── ...
│   ├── PE_225.py
│   └── Incremental_Trigger.py   # Batch processing trigger
│
├── docs/                         # Documentation
│   ├── API_DOCUMENTATION.md     # Comprehensive API docs
│   ├── FORMULA_GUIDE.md         # Formula validation guide
│   ├── TEST_PLAN_GUIDE.md       # Test plan guide
│   └── EXAMPLES.md              # Usage examples
│
├── logs/                         # Log files (auto-generated)
│   ├── PE_101.log
│   ├── Formula_101.log
│   └── ...
│
├── Result_File/                  # Test execution results (auto-generated)
│   ├── Report_PE_101.xlsx
│   ├── Report_PE_102.xlsx
│   └── ...
│
├── Consumer_details.csv          # Extracted consumer data (generated)
├── Prepaid_Ledger_Report.xlsx   # Downloaded ledger data (generated)
└── README.md                     # This file
```

---

## Installation

### Prerequisites

- **Python**: 3.7 or higher
- **PostgreSQL**: Access to MDMS database (for test execution)
- **Network**: Access to stage APIs

### Required Python Packages

```bash
pip install pandas numpy requests psycopg2-binary openpyxl
```

Or use a requirements file:

```bash
pip install -r requirements.txt
```

### requirements.txt

```
pandas>=1.3.0
numpy>=1.20.0
requests>=2.26.0
psycopg2-binary>=2.9.0
openpyxl>=3.0.0
```

### Database Setup (for Test Plans)

Ensure you have access to the MDMS PostgreSQL database:

```python
DB_CONFIG = {
    'host': 'db_mdms.stage.mvvnl.internal',
    'database': 'validation_rules',
    'user': 'postgres',
    'password': '***',
    'port': 5432
}
```

---

## Quick Start

### 1. Extract Consumer Details

Extract consumer information from test reports:

```bash
# Place Report_PE_*.xlsx files in Result_File/ folder
python account.py
```

**Output**: `Consumer_details.csv`

### 2. Download Ledger Data

Download prepaid ledger data for consumers:

```bash
# Ensure Consumer_details.csv exists
python Download_Ledger.py
```

**Output**: `Prepaid_Ledger_Report.xlsx` with sheets per consumer

### 3. Run Formula Validation

Validate ledger calculations:

```bash
# Basic validation
python Formula/Formula_101.py

# Advanced validation with MD
python Formula/Formula_102.py

# Complete validation with tiers
python Formula/Formula_103.py
```

**Output**: `Formula_10X.xlsx` with comparison results

### 4. Execute Test Case

Run complete test case (create account, generate data, trigger, report):

```bash
python Test_Plan/PE_101.py
```

**Output**: 
- `logs/PE_101.log` - Detailed execution log
- `Result_File/Report_PE_101.xlsx` - Test report

### 5. Batch Processing

Trigger incremental processing for multiple accounts:

```bash
python Test_Plan/Incremental_Trigger.py
```

---

## Core Modules

### account.py

Extract consumer details from Excel reports into CSV format.

**Usage:**
```python
python account.py
```

**What it does:**
1. Scans `Result_File/` for `Report_PE_*.xlsx` files
2. Extracts "Consumer Details" sheet from each file
3. Consolidates data into `Consumer_details.csv`

**Required Columns:**
- accountId, meterSrno, supplyTypecode
- sanctionedLoad, loadUnit, meterInstalldate
- greenEnergyflag, prepaidOpeningbalance

**Example Output:**
```csv
Report_ID,accountId,meterSrno,supplyTypecode,sanctionedLoad,...
Report_PE_101,1234567890,PO34567890,10,1.0,...
Report_PE_102,2345678901,PO45678901,10,2.0,...
```

### Download_Ledger.py

Download prepaid ledger data from API for multiple consumers.

**Usage:**
```python
python Download_Ledger.py
```

**What it does:**
1. Reads `Consumer_details.csv`
2. Calls prepaid ledger API for each consumer
3. Creates Excel file with sheet per consumer
4. Logs errors to "Errors" sheet

**Output:**
- `Prepaid_Ledger_Report.xlsx`
  - One sheet per consumer (named by Report_ID)
  - "Errors" sheet (if any failures)
  - Summary sheet (if no data)

**Features:**
- 30-second timeout per request
- Comprehensive error logging with API responses
- Progress tracking
- Preserves leading zeros in IDs

---

## Formula Validation

### Formula_101.py - Basic Validation

**Scenario:** ST=10, Consumption ≤ 100 kWh, MD ≤ 75%

**Formulas:**
- Daily EC = consumption × 3.0
- Daily FC = (0.75 × 1 × 50) / 31
- Daily ED = (EC + FC) × 0.05
- Daily Rebate = (EC + FC) × 0.02
- Daily Final = (EC + FC + ED) - Rebate

**Usage:**
```python
python Formula/Formula_101.py
```

**Output:** `Formula_101.xlsx` with actual vs expected comparison

### Formula_102.py - Advanced Validation

**Scenario:** Variable MD with penalties and adjustments

**Additional Features:**
- Variable FC based on max demand percentage
- Fixed charge adjustments
- Excess demand penalty (EDP)
- Dynamic recalculation

**Usage:**
```python
python Formula/Formula_102.py
```

### Formula_103.py - Complete Validation

**Scenario:** Tiered rates with lifeline switch

**Additional Features:**
- 5 tiered EC rates (3.0, 5.5, 5.5, 6.0, 6.5)
- 2 FC rates (50, 110)
- Lifeline switch mechanism at 100 kWh
- EC and FC switch charges over 3 days

**Usage:**
```python
python Formula/Formula_103.py
```

**See [Formula Guide](docs/FORMULA_GUIDE.md) for detailed formula documentation.**

---

## Test Plans

### PE_101.py - Basic Test Case

**Test Scenario:** ST=10, ≤100 kWh, ≤75% MD

**Configuration:**
```python
SUPPLY_TYPECODE = "10"
SANCTIONED_LOAD = 1  # kW
END_WH = 100000      # 100 kWh total
MD_W = 750           # 0.75 kW max demand
PREPAID_OPENING_BALANCE = 4000
```

**Execution Steps:**
1. **Create Account** - Generate random account with specified config
2. **Fill Daily Load** - Insert daily consumption data (31 days)
3. **Fill Profile Instant** - Insert max demand data (31 days)
4. **Trigger Ledger API** - Calculate prepaid ledger
5. **Generate Report** - Create Excel report with all data

**Usage:**
```bash
python Test_Plan/PE_101.py
```

**Output:**
- `logs/PE_101.log` - Complete execution log
- `Result_File/Report_PE_101.xlsx` - 4-sheet report
  - Summary
  - Consumer Details
  - Daily Load
  - Profile Instant

**Sheets Detail:**

**Summary Sheet:**
| Test Case ID | Description | Account ID | Meter Number | Status |
|--------------|-------------|------------|--------------|--------|
| PE_101 | Basic test... | 1234567890 | PO34567890 | Completed |

**Consumer Details Sheet:**
| Parameter | Value |
|-----------|-------|
| accountId | 1234567890 |
| meterSrno | PO34567890 |
| sanctionedLoad | 1.0 |
| ... | ... |

### Other Test Cases

- **PE_102 - PE_125**: Variations with different supply types and load patterns
- **PE_126 - PE_150**: Advanced scenarios with green energy
- **PE_151 - PE_175**: Net metering scenarios
- **PE_176 - PE_200**: Seasonal variations
- **PE_201 - PE_225**: Edge cases and stress tests

**See [Test Plan Guide](docs/TEST_PLAN_GUIDE.md) for all test cases.**

---

## Configuration

### API Endpoints

Update endpoints in respective files if needed:

```python
# account.py & Download_Ledger.py
API_URL = "https://engine-web.stage.gomatimvvnl.in/daily_prepaid_ledger/"

# Test_Plan/*.py
ACCOUNT_API_URL = "https://integration1.stage.gomatimvvnl.in/initial_master_sync/"
LEDGER_API_BASE = "https://engine-web.stage.gomatimvvnl.in"
MDMS_API_BASE = "https://mdms-api.stage.gomatimvvnl.in/db-service"
```

### Database Configuration

Update database credentials in Test_Plan files:

```python
DB_CONFIG = {
    'host': 'db_mdms.stage.mvvnl.internal',
    'database': 'validation_rules',
    'user': 'postgres',
    'password': 'your_password',
    'port': 5432
}
```

### Formula Parameters

Adjust formula parameters in Formula files:

```python
# Formula_101.py
contracted_load = 1  # kW
fc_rate = 50         # Rs per kW
ed_rate = 0.05       # 5%
rebate_rate = 0.02   # 2%
ec_rate = 3          # Rs per kWh
```

---

## Documentation

Comprehensive documentation is available in the `docs/` folder:

- **[API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md)** - Complete API reference
- **[FORMULA_GUIDE.md](docs/FORMULA_GUIDE.md)** - Formula validation guide
- **[TEST_PLAN_GUIDE.md](docs/TEST_PLAN_GUIDE.md)** - Test plan execution guide
- **[EXAMPLES.md](docs/EXAMPLES.md)** - Usage examples and recipes

---

## Troubleshooting

### Common Issues

#### 1. "Consumer_details.csv not found"

**Solution:** Run `account.py` first to generate the CSV:
```bash
python account.py
```

#### 2. "No Excel files found in Result_File folder"

**Solution:** Ensure Excel reports are in `Result_File/` directory with pattern `Report_PE_*.xlsx`

#### 3. Database Connection Error

**Solution:** 
- Check network access to database server
- Verify credentials in `DB_CONFIG`
- Ensure PostgreSQL is running
- Check firewall rules

#### 4. API Timeout Errors

**Solution:**
- Check network connectivity to API servers
- Increase timeout in code (default 30s)
- Verify API endpoints are accessible
- Check API authentication tokens

#### 5. Missing Python Packages

**Solution:**
```bash
pip install pandas numpy requests psycopg2-binary openpyxl
```

#### 6. Excel File Permission Error

**Solution:** Close the Excel file before running the script

#### 7. "Sheet 'Consumer Details' not found"

**Solution:** Ensure Excel files have the correct sheet structure (generated by Test Plans)

### Debug Mode

Enable detailed logging:

```python
logging.basicConfig(level=logging.DEBUG)
```

### Log Files

Check log files in `logs/` directory for detailed error messages:

```bash
cat logs/PE_101.log
cat logs/Formula_101.log
```

---

## Best Practices

### 1. Test Execution Order

```bash
# Step 1: Run test case to generate data
python Test_Plan/PE_101.py

# Step 2: Extract consumer details
python account.py

# Step 3: Download ledger data
python Download_Ledger.py

# Step 4: Validate formulas
python Formula/Formula_101.py
```

### 2. Batch Test Execution

```bash
# Run multiple tests
for i in {101..110}; do
    python Test_Plan/PE_${i}.py
done

# Trigger batch processing
python Test_Plan/Incremental_Trigger.py
```

### 3. Verification Workflow

```bash
# 1. Run test
python Test_Plan/PE_101.py

# 2. Validate calculations
python Formula/Formula_101.py

# 3. Check logs
cat logs/PE_101.log | grep -i error
cat logs/Formula_101.log | grep -i "Test Case Result"
```

### 4. Data Cleanup

```bash
# Clean up generated files
rm Consumer_details.csv
rm Prepaid_Ledger_Report.xlsx
rm Formula_*.xlsx
rm -rf logs/*
rm -rf Result_File/*
```

---

## Examples

### Example 1: Run Complete Workflow

```bash
#!/bin/bash
# complete_test.sh

echo "Step 1: Execute test case"
python Test_Plan/PE_101.py

echo "Step 2: Extract consumer details"
python account.py

echo "Step 3: Download ledger data"
python Download_Ledger.py

echo "Step 4: Validate formulas"
python Formula/Formula_101.py

echo "Complete! Check logs/ and Result_File/ for outputs"
```

### Example 2: Programmatic Usage

```python
# custom_test.py
from Test_Plan.PE_101 import create_account, fill_daily_load_data

# Create account
account_data = create_account()
if account_data:
    print(f"Account created: {account_data['accountId']}")
    
    # Fill data
    fill_daily_load_data(account_data)
```

### Example 3: Custom Formula Validation

```python
# custom_validation.py
from Formula.Formula_101 import PrepaidLedgerComparison

# Create custom comparator
comparator = PrepaidLedgerComparison()

# Override configuration
comparator.ec_rate = 3.5
comparator.fc_rate = 60

# Run validation
comparator.run_comparison()
```

**See [EXAMPLES.md](docs/EXAMPLES.md) for more examples.**

---

## Contributing

### Adding New Test Cases

1. Copy `Test_Plan/PE_101.py` to new file (e.g., `PE_226.py`)
2. Update configuration parameters
3. Update test case ID and description
4. Run and verify

### Adding New Formulas

1. Copy `Formula/Formula_101.py` to new file
2. Implement custom `calculate_expected_values()` method
3. Update comparison columns
4. Run and verify

### Code Style

- Follow PEP 8 guidelines
- Add docstrings to all functions
- Use type hints where appropriate
- Include comprehensive error handling
- Add logging statements

---

## License

Copyright © 2025 UP MVVNL. All rights reserved.

---

## Support

For issues, questions, or contributions:
- Check logs in `logs/` directory
- Review [API Documentation](docs/API_DOCUMENTATION.md)
- Check [Troubleshooting](#troubleshooting) section

---

## Changelog

### Version 1.0 (December 2025)
- Initial release
- Core modules: account.py, Download_Ledger.py
- Formula validation: Formula_101, 102, 103
- Test plans: PE_101 through PE_225
- Comprehensive documentation

---

## Acknowledgments

Built for UP MVVNL prepaid engine validation and testing.

