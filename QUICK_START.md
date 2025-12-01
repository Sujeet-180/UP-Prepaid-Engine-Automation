# Quick Start Guide

Get up and running with the UP Prepaid Engine Automation Framework in 5 minutes!

## 1. Installation (2 minutes)

```bash
# Clone the repository (or navigate to your workspace)
cd UP-Prepaid-Engine-Automation

# Install Python dependencies
pip install -r requirements.txt

# Verify installation
python verify_installation.py
```

## 2. Run Your First Test (1 minute)

```bash
# Execute a basic test case
python Test_Plan/PE_101.py
```

**Output:** 
- Log file: `logs/PE_101.log`
- Excel report: `Result_File/Report_PE_101.xlsx`

## 3. Extract Consumer Details (30 seconds)

```bash
# Extract consumer details from test reports
python account.py
```

**Output:** `Consumer_details.csv`

## 4. Download Ledger Data (30 seconds)

```bash
# Download prepaid ledger data from API
python Download_Ledger.py
```

**Output:** `Prepaid_Ledger_Report.xlsx`

## 5. Validate Formulas (1 minute)

```bash
# Run formula validation
python Formula/Formula_101.py
```

**Output:** 
- Validation report: `Formula_101.xlsx`
- Log file: `logs/Formula_101.log`

---

## What You Just Did

✅ Created a test account with random data  
✅ Generated 31 days of consumption and max demand data  
✅ Triggered prepaid ledger calculation  
✅ Generated comprehensive Excel report  
✅ Extracted consumer details to CSV  
✅ Downloaded ledger data from API  
✅ Validated ledger calculations with formulas  

---

## Next Steps

### Run More Tests

```bash
# Basic scenarios
python Test_Plan/PE_102.py
python Test_Plan/PE_103.py

# Advanced validations
python Formula/Formula_102.py  # With max demand penalties
python Formula/Formula_103.py  # With tiered rates
```

### Batch Processing

```bash
# Trigger incremental processing
python Test_Plan/Incremental_Trigger.py
```

### Explore Results

- **Test Reports:** `Result_File/Report_PE_*.xlsx`
  - Summary sheet
  - Consumer details
  - Daily load data
  - Profile instant data

- **Validation Reports:** `Formula_*.xlsx`
  - Actual vs Expected comparison
  - Pass/Fail status per day
  - Detailed mismatch analysis

- **Logs:** `logs/`
  - Step-by-step execution details
  - Calculation breakdowns
  - Error messages and warnings

---

## Common Workflows

### Workflow 1: Complete Test Cycle

```bash
# 1. Run test
python Test_Plan/PE_101.py

# 2. Extract consumer details
python account.py

# 3. Download ledger
python Download_Ledger.py

# 4. Validate
python Formula/Formula_101.py
```

### Workflow 2: Multiple Tests

```bash
# Run multiple test cases
for i in {101..105}; do
    python Test_Plan/PE_${i}.py
    sleep 10  # Wait between tests
done

# Batch process
python Test_Plan/Incremental_Trigger.py

# Extract all consumer details
python account.py

# Download all ledgers
python Download_Ledger.py
```

### Workflow 3: Validation Only

```bash
# If you already have data, just validate
python Formula/Formula_101.py
python Formula/Formula_102.py
python Formula/Formula_103.py
```

---

## Project Structure

```
UP-Prepaid-Engine-Automation/
├── account.py                    # Extract consumer details
├── Download_Ledger.py            # Download ledger data
│
├── Formula/                      # Formula validation
│   ├── Formula_101.py           # Basic
│   ├── Formula_102.py           # Advanced
│   └── Formula_103.py           # Complete
│
├── Test_Plan/                    # Test cases
│   ├── PE_101.py                # Basic test
│   ├── PE_102.py                # Advanced test
│   └── ...                      # More tests
│
├── docs/                         # Documentation
│   ├── API_DOCUMENTATION.md     # API reference
│   ├── FORMULA_GUIDE.md         # Formula details
│   ├── TEST_PLAN_GUIDE.md       # Test execution
│   └── EXAMPLES.md              # Code examples
│
├── logs/                         # Auto-generated logs
├── Result_File/                  # Auto-generated reports
└── README.md                     # Main documentation
```

---

## Configuration

### API Endpoints

Edit these in respective files:

```python
# account.py, Download_Ledger.py
API_URL = "https://engine-web.stage.gomatimvvnl.in/daily_prepaid_ledger/"

# Test_Plan/*.py
ACCOUNT_API_URL = "https://integration1.stage.gomatimvvnl.in/initial_master_sync/"
MDMS_API_BASE = "https://mdms-api.stage.gomatimvvnl.in/db-service"
```

### Database

Edit in Test_Plan files:

```python
DB_CONFIG = {
    'host': 'db_mdms.stage.mvvnl.internal',
    'database': 'validation_rules',
    'user': 'postgres',
    'password': '***',
    'port': 5432
}
```

### Test Parameters

Edit in Test_Plan files:

```python
# PE_101.py
SUPPLY_TYPECODE = "10"
SANCTIONED_LOAD = 1
END_WH = 100000  # 100 kWh
MD_W = 750       # 0.75 kW
PREPAID_OPENING_BALANCE = 4000
```

---

## Troubleshooting

### Issue: "Module not found"

```bash
pip install -r requirements.txt
```

### Issue: "Consumer_details.csv not found"

```bash
# Run account.py first
python account.py
```

### Issue: "Database connection failed"

- Check network access to database server
- Verify credentials in `DB_CONFIG`
- Ensure PostgreSQL is running

### Issue: "API timeout"

- Check network connectivity
- Increase timeout in code (default 30s)
- Verify API endpoints are accessible

### Issue: "No data in Excel reports"

- Wait 30-60 seconds after test execution
- Verify meter number is correct
- Check API response manually

---

## Getting Help

📚 **Documentation**
- [README.md](README.md) - Complete guide
- [API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md) - API reference
- [FORMULA_GUIDE.md](docs/FORMULA_GUIDE.md) - Formula details
- [TEST_PLAN_GUIDE.md](docs/TEST_PLAN_GUIDE.md) - Test execution
- [EXAMPLES.md](docs/EXAMPLES.md) - Code examples

🔍 **Logs**
- Check `logs/` directory for detailed execution logs
- Each module creates its own log file

💡 **Tips**
- Run tests sequentially, not in parallel
- Wait between test executions
- Check logs for error messages
- Verify each step before proceeding

---

## Tips & Best Practices

### 1. Always Check Logs

```bash
# View log in real-time
tail -f logs/PE_101.log

# Check for errors
grep -i error logs/PE_101.log

# Check test result
grep "Test Case Result" logs/Formula_101.log
```

### 2. Verify Each Step

After each step, verify the output:
- ✅ Account created? Check log
- ✅ Data inserted? Check database
- ✅ API triggered? Check response
- ✅ Report generated? Check Result_File/

### 3. Clean Up Regularly

```bash
# Clean up old logs (older than 7 days)
find logs/ -name "*.log" -mtime +7 -delete

# Clean up test reports
rm -rf Result_File/Report_PE_*.xlsx

# Clean up validation files
rm Formula_*.xlsx
```

### 4. Use Automation Scripts

See [EXAMPLES.md](docs/EXAMPLES.md) for:
- Batch test runners
- Scheduled execution
- Cleanup utilities
- Custom reporters

---

## What's Next?

### Learn More

1. **Read the docs** - [README.md](README.md)
2. **Understand formulas** - [FORMULA_GUIDE.md](docs/FORMULA_GUIDE.md)
3. **Explore APIs** - [API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md)
4. **Try examples** - [EXAMPLES.md](docs/EXAMPLES.md)

### Create Custom Tests

1. Copy `Test_Plan/PE_101.py` to new file
2. Update configuration parameters
3. Update test case ID and description
4. Run and verify

### Extend Functionality

1. Add custom formula validation
2. Create batch processing scripts
3. Build REST API wrapper
4. Generate HTML reports

---

## Summary

You now know how to:
- ✅ Run test cases
- ✅ Extract consumer details
- ✅ Download ledger data
- ✅ Validate formulas
- ✅ Generate reports
- ✅ Troubleshoot issues

**Happy Testing! 🚀**

For complete documentation, see [README.md](README.md)
