# UP-Prepaid-Engine-Automation

Automation testing framework for UP Prepaid Engine validation.

## 📚 Documentation

- **[API Documentation](API_DOCUMENTATION.md)** - Comprehensive documentation for all public APIs, functions, and components
- **[Quick Reference Guide](QUICK_REFERENCE.md)** - Quick reference for common tasks and functions

## Project Structure

- `account.py` - Extract Consumer Details from Excel Reports
- `Download_Ledger.py` - Download ledger functionality
- `Formula/` - Contains formula validation scripts (Formula_101.py, Formula_102.py, Formula_103.py)
- `Test_Plan/` - Contains test cases (PE_101.py through PE_225.py)
- `logs/` - Log files
- `Result_File/` - Result files from test executions

## Getting Started

### Prerequisites

```bash
pip install pandas openpyxl requests psycopg2-binary numpy
```

### Quick Start

1. **Extract Consumer Details:**
   ```bash
   python account.py
   ```

2. **Download Ledger Data:**
   ```bash
   python Download_Ledger.py
   ```

3. **Validate Formulas:**
   ```bash
   python Formula/Formula_101.py
   ```

4. **Run Test Cases:**
   ```bash
   python Test_Plan/PE_101.py
   ```

## Usage

See [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for detailed usage instructions and examples.

### Common Workflows

**Extract and Download:**
```bash
python account.py
python Download_Ledger.py
```

**Validate Formula:**
```bash
python Formula/Formula_101.py
```

**Run Test Case:**
```bash
python Test_Plan/PE_101.py
```

## Features

- ✅ Extract consumer details from Excel reports
- ✅ Download prepaid ledger data from APIs
- ✅ Validate billing formulas (Formula 101, 102, 103)
- ✅ Automated test case execution (PE_101 through PE_225)
- ✅ Comprehensive Excel report generation
- ✅ Detailed logging and error handling

## Output Files

- `Consumer_details.csv` - Consolidated consumer details
- `Prepaid_Ledger_Report.xlsx` - Ledger data for all consumers
- `Formula_*.xlsx` - Formula validation reports
- `Report_PE_*.xlsx` - Test case reports
- `logs/*.log` - Log files

## Support

For detailed API documentation, see [API_DOCUMENTATION.md](API_DOCUMENTATION.md)
For quick reference, see [QUICK_REFERENCE.md](QUICK_REFERENCE.md)

