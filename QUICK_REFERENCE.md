# Quick Reference Guide

## Common Tasks

### Extract Consumer Details from Reports
```bash
python account.py
```
**Output:** `Consumer_details.csv`

---

### Download Ledger Data
```bash
python Download_Ledger.py
```
**Prerequisites:** `Consumer_details.csv` must exist
**Output:** `Prepaid_Ledger_Report.xlsx`

---

### Validate Formula 101
```bash
python Formula/Formula_101.py
```
**Output:** `Formula_101.xlsx`, `logs/Formula_101.log`

---

### Validate Formula 102
```bash
python Formula/Formula_102.py
```
**Output:** `Formula_102.xlsx`, `logs/Formula_102.log`

---

### Validate Formula 103
```bash
python Formula/Formula_103.py
```
**Output:** `Formula_103.xlsx`, `logs/Formula_103.log`

---

### Run Test Case PE_101
```bash
python Test_Plan/PE_101.py
```
**Output:** `Report_PE_101.xlsx`, `logs/PE_101.log`

---

## Function Quick Reference

### account.py

| Function | Purpose | Returns |
|----------|---------|---------|
| `get_report_identifier(filename)` | Extract report ID from filename | str |
| `extract_consumer_details(excel_file)` | Extract consumer data from Excel | DataFrame |
| `process_all_reports()` | Process all Report_PE_*.xlsx files | DataFrame |
| `save_to_csv(df, output_file)` | Save DataFrame to CSV | None |
| `main()` | Run complete extraction workflow | None |

---

### Download_Ledger.py

| Function | Purpose | Returns |
|----------|---------|---------|
| `read_consumer_details()` | Read consumer data from CSV | List[Tuple] |
| `fetch_and_save_data()` | Download and save ledger data | None |

---

### Formula Classes

| Method | Purpose | Returns |
|--------|---------|---------|
| `fetch_prepaid_ledger_data()` | Get data from API | DataFrame |
| `calculate_expected_values(df)` | Calculate expected values | DataFrame |
| `compare_values(df)` | Compare actual vs expected | DataFrame |
| `generate_comparison_report(df, filename)` | Generate Excel report | None |
| `run_comparison()` | Run complete validation | None |

---

### Test Case Functions (PE_*.py)

| Function | Purpose | Returns |
|----------|---------|---------|
| `generate_random_number(length)` | Generate random number | str |
| `generate_random_alphanumeric(length)` | Generate random alphanumeric | str |
| `generate_consumer_name()` | Generate random name | str |
| `generate_email(name)` | Generate email from name | str |
| `generate_mobile_number()` | Generate mobile number | int |
| `parse_install_date(date_str)` | Parse date format | str |
| `get_month_end_date(start_date)` | Get next month start | str |
| `create_account()` | Create account via API | Dict or None |
| `fill_daily_load_data(account_data)` | Fill daily load data | None |
| `fill_profile_instant_data(account_data)` | Fill profile instant data | None |
| `trigger_prepaid_ledger(account_id)` | Trigger ledger calculation | None |
| `fetch_daily_load_data(meter_srno)` | Fetch daily load data | DataFrame |
| `fetch_profile_instant_data(meter_srno)` | Fetch profile instant data | DataFrame |
| `generate_excel_report(account_data)` | Generate test report | None |
| `main()` | Run complete test case | None |

---

## Configuration Constants

### account.py
- `RESULT_FOLDER = "Result_File"`
- `SHEET_NAME = "Consumer Details"`
- `OUTPUT_CSV = "Consumer_details.csv"`

### Download_Ledger.py
- `API_URL = "https://engine-web.stage.gomatimvvnl.in/daily_prepaid_ledger/"`
- `CSV_FILE = "Consumer_details.csv"`

### Formula Files
- `contracted_load`: Contracted load in kW
- `fc_rate`: Fixed charge rate per kW
- `ed_rate`: Electricity duty rate (e.g., 0.05)
- `rebate_rate`: Rebate rate (e.g., 0.02)
- `opening_balance`: Opening balance
- `ec_rate`: Energy charge rate per kWh
- `days_in_month`: Number of days in month

### Test Cases
- `SUPPLY_TYPECODE`: Supply type code
- `SANCTIONED_LOAD`: Sanctioned load
- `PREPAID_OPENING_BALANCE`: Opening balance
- `END_WH`: End watt-hour value
- `MD_W`: Max demand in watts

---

## Output Files

| File | Source | Description |
|------|--------|-------------|
| `Consumer_details.csv` | account.py | Consolidated consumer details |
| `Prepaid_Ledger_Report.xlsx` | Download_Ledger.py | Ledger data for all consumers |
| `Formula_101.xlsx` | Formula_101.py | Formula 101 validation report |
| `Formula_102.xlsx` | Formula_102.py | Formula 102 validation report |
| `Formula_103.xlsx` | Formula_103.py | Formula 103 validation report |
| `Report_PE_*.xlsx` | PE_*.py | Test case reports |
| `logs/*.log` | All modules | Log files |

---

## Common Workflows

### Workflow 1: Extract and Download
```python
# Step 1: Extract consumer details
python account.py

# Step 2: Download ledger data
python Download_Ledger.py
```

### Workflow 2: Validate Formula
```python
# Run formula validation
python Formula/Formula_101.py
```

### Workflow 3: Run Test Case
```python
# Run specific test case
python Test_Plan/PE_101.py
```

### Workflow 4: Complete Validation
```python
# 1. Extract details
python account.py

# 2. Download ledgers
python Download_Ledger.py

# 3. Validate formulas
python Formula/Formula_101.py
python Formula/Formula_102.py
python Formula/Formula_103.py
```

---

## Troubleshooting

### Issue: CSV file not found
**Solution:** Run `account.py` first to generate `Consumer_details.csv`

### Issue: API timeout
**Solution:** Check network connection, API may be slow

### Issue: Database connection error
**Solution:** Verify database credentials and network access

### Issue: Excel file not created
**Solution:** Check `openpyxl` is installed: `pip install openpyxl`

### Issue: Formula validation fails
**Solution:** Check log files in `logs/` directory for details

---

## API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/initial_master_sync/` | POST | Create account |
| `/daily_prepaid_ledger/{account_id}/?meter_number={meter}` | GET | Get ledger data |
| `/db-service/dailyloads` | GET | Get daily load data |
| `/db-service/profileinstant` | GET | Get profile instant data |

---

## Database Tables

| Table | Purpose |
|-------|---------|
| `dailyload_vee_validated` | Daily load data |
| `profile_instant_vee` | Profile instant data |

---

## Log Files

All modules create log files in `logs/` directory:
- `account.py` → No specific log file (prints to console)
- `Download_Ledger.py` → No specific log file (prints to console)
- `Formula_101.py` → `logs/Formula_101.log`
- `Formula_102.py` → `logs/Formula_102.log`
- `Formula_103.py` → `logs/Formula_103.log`
- `PE_*.py` → `logs/PE_*.log`

---

## Data Formats

### Date Formats
- **Input:** `"2025-10-01T00:00:00"` (ISO format)
- **Database:** `"2025-10-01 00:00:00"` (SQL format)
- **API:** ISO 8601 format with UTC timezone

### Account ID Format
- **Format:** 10-digit number
- **Example:** `"1234567890"`

### Meter Serial Number Format
- **Format:** `PO{last_8_digits_of_account_id}`
- **Example:** Account `1234567890` → Meter `PO234567890`

---

## Tips

1. **Always check logs** for detailed error messages
2. **Verify prerequisites** before running scripts (CSV files, database access)
3. **Review Excel reports** for detailed data and error information
4. **Use tolerance** of 0.01 for floating-point comparisons
5. **Check API status** if downloads fail
6. **Verify database connection** before running test cases
