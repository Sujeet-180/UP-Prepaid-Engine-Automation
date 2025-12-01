# UP Prepaid Engine Automation

Comprehensive automation testing framework for UP Prepaid Engine billing validation. This framework provides tools for creating test accounts, generating test data, triggering billing calculations, and validating the results against expected formulas.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Documentation](#documentation)
- [API Reference](#api-reference)
- [Contributing](#contributing)

## ✨ Features

- **Automated Test Case Execution**: 125+ test cases covering various billing scenarios
- **Formula Validation**: Validate prepaid ledger calculations against expected formulas
- **Data Extraction**: Extract consumer details from Excel reports
- **Ledger Download**: Download and consolidate ledger data from APIs
- **Comprehensive Logging**: Detailed logs for debugging and audit trails
- **Excel Reports**: Professional Excel reports with multiple sheets

## 📁 Project Structure

```
UP-Prepaid-Engine-Automation/
├── account.py              # Consumer details extraction tool
├── Download_Ledger.py      # Ledger data download utility
├── requirements.txt        # Python dependencies
├── Formula/                # Formula validation scripts
│   ├── Formula_101.py      # Basic prepaid ledger comparison
│   ├── Formula_102.py      # Advanced with max demand penalty
│   └── Formula_103.py      # Tiered rates with life line switch
├── Test_Plan/              # Test case scripts
│   ├── PE_101.py           # Test case 101
│   ├── PE_102.py           # Test case 102
│   ├── ...                 # Test cases 103-224
│   ├── PE_225.py           # Test case 225
│   └── Incremental_Trigger.py  # Incremental task trigger
├── docs/                   # Documentation
│   ├── API_REFERENCE.md    # Complete API documentation
│   ├── USER_GUIDE.md       # User guide with examples
│   └── TEST_CASE_CATALOG.md # All test cases documented
├── logs/                   # Log files (auto-created)
└── Result_File/            # Test result Excel files (auto-created)
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Network access to stage environment APIs and database

### Steps

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd UP-Prepaid-Engine-Automation
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create required directories:**
   ```bash
   mkdir -p logs Result_File
   ```

## 🏃 Quick Start

### Run a Test Case

```bash
python Test_Plan/PE_101.py
```

This will:
1. Create a test consumer account
2. Generate daily load data
3. Generate profile instant data
4. Trigger prepaid ledger calculation
5. Generate an Excel report

### Extract Consumer Details

```bash
python account.py
```

Creates `Consumer_details.csv` from all test reports.

### Download Ledger Data

```bash
python Download_Ledger.py
```

Downloads ledger data for all consumers and saves to `Prepaid_Ledger_Report.xlsx`.

### Validate Formulas

```bash
python Formula/Formula_101.py
```

Compares API values with expected calculations.

## 📖 Usage

### Running Multiple Test Cases

```bash
# Run test cases PE_101 through PE_110
for i in {101..110}; do
    python Test_Plan/PE_$i.py
done
```

### Complete Workflow

```bash
# Step 1: Run test cases
python Test_Plan/PE_101.py
python Test_Plan/PE_102.py

# Step 2: Trigger incremental processing
python Test_Plan/Incremental_Trigger.py

# Step 3: Extract consumer details
python account.py

# Step 4: Download ledger data
python Download_Ledger.py

# Step 5: Validate calculations
python Formula/Formula_101.py
```

### Viewing Results

- **Test Reports**: `Result_File/Report_PE_*.xlsx`
- **Logs**: `logs/PE_*.log`
- **Consumer CSV**: `Consumer_details.csv`
- **Ledger Report**: `Prepaid_Ledger_Report.xlsx`
- **Formula Reports**: `Formula_*.xlsx`

## 📚 Documentation

Detailed documentation is available in the `docs/` folder:

| Document | Description |
|----------|-------------|
| [API_REFERENCE.md](docs/API_REFERENCE.md) | Complete API documentation with all functions, parameters, and examples |
| [USER_GUIDE.md](docs/USER_GUIDE.md) | Step-by-step usage guide with troubleshooting |
| [TEST_CASE_CATALOG.md](docs/TEST_CASE_CATALOG.md) | Catalog of all 125+ test cases with descriptions |

## 🔧 API Reference

### Core Modules

#### account.py

Extracts consumer details from Excel reports.

```python
from account import extract_consumer_details, process_all_reports

# Extract from single file
df = extract_consumer_details("Result_File/Report_PE_101.xlsx")

# Process all reports
combined_df = process_all_reports()
```

#### Download_Ledger.py

Downloads prepaid ledger data from APIs.

```python
from Download_Ledger import read_consumer_details, fetch_and_save_data

# Read consumer list
consumers = read_consumer_details()

# Fetch and save all data
fetch_and_save_data()
```

### Formula Validation

```python
from Formula.Formula_101 import PrepaidLedgerComparison

# Run validation
comparator = PrepaidLedgerComparison()
comparator.run_comparison()
```

### Test Case Functions

```python
from Test_Plan.PE_101 import (
    create_account,
    fill_daily_load_data,
    fill_profile_instant_data,
    trigger_prepaid_ledger,
    generate_excel_report
)

# Create account
account_data = create_account()

# Fill test data
fill_daily_load_data(account_data)
fill_profile_instant_data(account_data)

# Trigger billing
trigger_prepaid_ledger(account_data['accountId'])

# Generate report
generate_excel_report(account_data)
```

## 🔌 API Endpoints

| Service | Base URL |
|---------|----------|
| Integration API | `https://integration1.stage.gomatimvvnl.in` |
| Engine API | `https://engine-web.stage.gomatimvvnl.in` |
| MDMS API | `https://mdms-api.stage.gomatimvvnl.in/db-service` |

## 📊 Test Case Categories

| Category | Test IDs | Description |
|----------|----------|-------------|
| Basic Scenarios | PE_101 - PE_110 | Standard billing calculations |
| Max Demand | PE_111 - PE_120 | Fixed charge adjustments and EDP |
| Life Line Switch | PE_121 - PE_135 | Tariff switching scenarios |
| Supply Types | PE_136 - PE_155 | Different tariff structures |
| Balance Scenarios | PE_156 - PE_170 | Wallet and balance handling |
| Electricity Duty | PE_171 - PE_180 | ED calculation scenarios |
| Rebate | PE_181 - PE_190 | Rebate calculation scenarios |
| Date/Time | PE_191 - PE_200 | Date-based calculations |
| Edge Cases | PE_201 - PE_215 | Boundary conditions |
| Integration | PE_216 - PE_225 | End-to-end scenarios |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add new test cases following the existing pattern
4. Update documentation as needed
5. Submit a pull request

## 📝 License

[Add license information here]

## 📞 Support

For issues or questions:
1. Check the logs in `logs/` directory
2. Review documentation in `docs/` folder
3. Verify API connectivity and credentials

---

*UP Prepaid Engine Automation Framework v1.0*
