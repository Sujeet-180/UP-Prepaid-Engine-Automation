# Test Plan Execution Guide

## Table of Contents
- [Overview](#overview)
- [Test Plan Architecture](#test-plan-architecture)
- [PE_101: Basic Test Case](#pe_101-basic-test-case)
- [Test Execution Workflow](#test-execution-workflow)
- [Database Operations](#database-operations)
- [API Integration](#api-integration)
- [Excel Report Generation](#excel-report-generation)
- [All Test Cases Reference](#all-test-cases-reference)
- [Incremental Trigger](#incremental-trigger)
- [Troubleshooting](#troubleshooting)

---

## Overview

Test Plan modules automate the complete lifecycle of prepaid engine testing:

1. **Account Creation** - Generate test accounts via API
2. **Data Generation** - Create daily load and max demand data
3. **API Triggering** - Execute ledger calculation
4. **Report Generation** - Create comprehensive Excel reports

### Test Plan Naming Convention

- **PE_XXX.py** - Test cases (PE = Prepaid Engine)
- **XXX** - 3-digit test case number (101-225)

### Test Case Structure

All test cases follow this structure:

```python
1. Configuration Section
   - Supply type, load, dates, etc.
   
2. Helper Functions
   - Data generation utilities
   
3. Main Functions
   - create_account()
   - fill_daily_load_data()
   - fill_profile_instant_data()
   - trigger_prepaid_ledger()
   - generate_excel_report()
   
4. Main Execution
   - main() function orchestrating all steps
```

---

## Test Plan Architecture

### Execution Flow

```
┌─────────────────────────────────┐
│  1. Create Account (API)        │
│     - Generate random data      │
│     - Call account creation API │
└────────────┬────────────────────┘
             │
             ↓
┌─────────────────────────────────┐
│  2. Fill Daily Load (Database)  │
│     - Generate 31 days data     │
│     - Insert into PostgreSQL    │
└────────────┬────────────────────┘
             │
             ↓
┌─────────────────────────────────┐
│  3. Fill Profile Instant (DB)   │
│     - Generate MD data          │
│     - Insert into PostgreSQL    │
└────────────┬────────────────────┘
             │
             ↓
┌─────────────────────────────────┐
│  4. Trigger Ledger (API)        │
│     - Call calculation API      │
│     - Wait for processing       │
└────────────┬────────────────────┘
             │
             ↓
┌─────────────────────────────────┐
│  5. Generate Report (Excel)     │
│     - Fetch data from APIs      │
│     - Create multi-sheet report │
└─────────────────────────────────┘
```

### Dependencies

**Python Packages:**
- `requests` - API calls
- `pandas` - Data manipulation
- `psycopg2` - PostgreSQL connectivity
- `openpyxl` - Excel file generation
- `logging` - Detailed logging

**External Services:**
- **Integration API** - Account creation
- **MDMS Database** - Data storage
- **Engine Web API** - Ledger calculation
- **MDMS API** - Data retrieval

---

## PE_101: Basic Test Case

### Test Scenario

**Test Case ID:** PE_101  
**Description:** Verify prepaid ledger calculation for ST=10 (normal 10A), with Consumption ≤ 100 kWh and MD ≤ 75%

### Configuration

```python
# Fixed Parameters
SUPPLY_TYPECODE = "10"
SANCTIONED_LOAD = 1              # kW
LOAD_UNIT = "KW"
METER_INSTALL_DATE = "2025-11-01T00:00:00"
NET_METER_FLAG = "N"
GREEN_ENERGY_FLAG = "N"
POWER_LOOM_COUNT = 0
PREPAID_OPENING_BALANCE = 4000   # Rs
PARAM1 = "0"
PREPAID_POSTPAID_FLAG = "1"      # Prepaid
ED_APPLICABLE = "1"              # Yes

# Daily Load Configuration
END_WH = 100000                  # 100 kWh total for the month
MD_W = 750                       # 0.75 kW max demand (75% of load)
```

### Expected Behavior

- **Daily Consumption**: ~3.2 kWh per day (100/31)
- **Max Demand**: Progressive from 0 to 750W
- **Fixed Charge**: Based on 75% of contracted load
- **Balance**: Decreases daily by final charge

---

## Test Execution Workflow

### Step 1: Create Account

**Function:** `create_account() -> Dict`

**Process:**
1. Generate 10-digit account ID
2. Generate meter serial number (PO + last 8 digits)
3. Generate random consumer details (name, email, mobile)
4. Construct API payload
5. Call account creation API
6. Return account data

**API Call:**
```python
POST https://integration1.stage.gomatimvvnl.in/initial_master_sync/

Headers:
  Content-Type: application/json
  Authorization: Bearer {token}

Payload: {
  "accountId": "1234567890",
  "meterSrno": "PO34567890",
  "sanctionedLoad": 1.0,
  "supplyTypecode": "10",
  ...
}
```

**Output:**
```python
{
    'accountId': '1234567890',
    'meterSrno': 'PO34567890',
    'meterInstalldate': '2025-11-01T00:00:00',
    'badgeNumber': 'GPMPO34567890',
    'payload': {...}
}
```

**Example:**
```python
account_data = create_account()
if account_data:
    print(f"Account ID: {account_data['accountId']}")
    print(f"Meter No: {account_data['meterSrno']}")
```

---

### Step 2: Fill Daily Load Data

**Function:** `fill_daily_load_data(account_data) -> bool`

**Process:**
1. Parse meter install date to get start/end dates
2. Calculate total days (typically 31)
3. Generate progressive consumption data
4. Insert into `dailyload_vee_validated` table

**Data Generation Algorithm:**

```python
# Calculate daily increments
total_days = 31
target_wh = 100000

current_wh = 0
for day in range(total_days):
    if day == total_days - 1:
        # Last day: ensure exact target
        current_wh = target_wh
    else:
        # Calculate remaining and distribute with variability
        remaining_wh = target_wh - current_wh
        remaining_days = total_days - day - 1
        avg_increment = remaining_wh / remaining_days
        
        # Add variability (0.3 to 1.7 of average)
        min_increment = avg_increment * 0.3
        max_increment = min(avg_increment * 1.7, remaining_wh)
        increment = random.randint(min_increment, max_increment)
        current_wh += increment
    
    # VAh calculated from Wh with 0.90 PF
    current_vah = current_wh / 0.90
```

**Database Record:**
```python
{
    'device_identifier': 'PO34567890',
    'data_timestamp': '2025-10-31 18:30:00',  # UTC-5:30
    'import_Wh': 3226,
    'import_VAh': 3584,
    'export_Wh': 24,
    'export_VAh': 27,
    'data_type': 'DLFV',
    'is_valid': True,
    'is_estimated': False,
    ...
}
```

**Features:**
- Natural consumption patterns with random variation
- Ensures final cumulative equals target
- Handles power factor (0.90) for VAh
- Bulk insert for efficiency
- Progress logging

**Example Output:**
```
Day 1/31: 2025-10-31 - Wh: 2845, VAh: 3161.11
Day 10/31: 2025-11-09 - Wh: 29123, VAh: 32358.89
Day 20/31: 2025-11-19 - Wh: 67541, VAh: 75045.56
Day 31/31: 2025-11-30 - Wh: 100000, VAh: 111111.11
Generated 31 daily load records
Successfully inserted 31 daily load records into dailyload_vee_validated
```

---

### Step 3: Fill Profile Instant Data

**Function:** `fill_profile_instant_data(account_data) -> bool`

**Process:**
1. Parse meter install date
2. Generate progressive max demand data
3. Insert into `profile_instant_vee` table

**Data Generation:**

```python
MD_W = 750  # Target max demand in watts
MD_VA = 750 / 0.90  # Apparent power

for day in range(total_days):
    # Progressive MD from 0 to target
    progress_ratio = day / (total_days - 1)
    current_md_w = int(MD_W * progress_ratio)
    current_md_va = int(MD_VA * progress_ratio)
```

**Database Record:**
```python
{
    'device_identifier': 'PO34567890',
    'data_timestamp': '2025-10-31 18:30:00',
    'MD_W': 24,
    'MD_VA': 27,
    'MD_W_datetime': '2025-10-31 18:30:00',
    'voltage': 230,
    'frequency': 50.0,
    'PF': 1,
    'is_valid': True,
    ...
}
```

**Features:**
- Linear progression from 0 to target MD
- Handles power factor for apparent power
- Complete meter metadata
- Bulk insert operation

**Example Output:**
```
Day 1/31: 2025-10-31 - MD_W: 24, MD_VA: 27
Day 10/31: 2025-11-09 - MD_W: 242, MD_VA: 269
Day 20/31: 2025-11-19 - MD_W: 483, MD_VA: 537
Day 31/31: 2025-11-30 - MD_W: 750, MD_VA: 833
Generated 31 profile instant records
Successfully inserted 31 profile instant records into profile_instant_vee
```

---

### Step 4: Trigger Prepaid Ledger

**Function:** `trigger_prepaid_ledger(account_id) -> bool`

**Process:**
1. Get yesterday's date (YYYY-MM-DD 00:00:00)
2. URL encode the date
3. Call daily_ledger_task API
4. Check response status

**API Call:**
```python
GET https://engine-web.stage.gomatimvvnl.in/trigger_task/daily_ledger_task/{date}?wallet_balance_sync_flag=False&account_id={account_id}

Headers:
  accept: application/json
```

**Example:**
```python
date_str = "2024-11-30 00:00:00"
date_encoded = "2024-11-30%2000%3A00%3A00"
account_id = "1234567890"

url = f"{LEDGER_API_BASE}/trigger_task/daily_ledger_task/{date_encoded}?wallet_balance_sync_flag=False&account_id={account_id}"

response = requests.get(url, headers={'accept': 'application/json'})
```

**Response:**
```json
{
    "status": "success",
    "message": "Ledger calculation triggered",
    "account_id": "1234567890"
}
```

**Features:**
- Uses yesterday's date for processing
- URL encoding for special characters
- Error handling and logging
- Returns success/failure

---

### Step 5: Generate Excel Report

**Function:** `generate_excel_report(account_data) -> bool`

**Process:**
1. Create `Result_File` directory
2. Fetch data from MDMS APIs
3. Create Excel workbook with 4 sheets
4. Format and style sheets
5. Save report

#### Sheet 1: Summary

```python
| Test Case ID | Test Case Description | Account ID | Meter Number | Badge Number | Status |
|--------------|----------------------|------------|--------------|--------------|---------|
| PE_101 | Basic test... | 1234567890 | PO34567890 | GPMPO34567890 | Completed |
```

**Features:**
- High-level test information
- Color-coded header (blue)
- Auto-adjusted column widths

#### Sheet 2: Consumer Details

```python
| Parameter | Value |
|-----------|-------|
| accountId | 1234567890 |
| meterSrno | PO34567890 |
| sanctionedLoad | 1.0 |
| supplyTypecode | 10 |
| prepaidOpeningbalance | 4000.0 |
| ... | ... |
```

**Features:**
- Key-value format
- Complete account creation payload
- All configuration parameters

#### Sheet 3: Daily Load

**Data Source:** `POST https://mdms-api.stage.gomatimvvnl.in/db-service/dailyloads`

```python
| dailyload_datetime | badge_number | import_Wh | import_VAh | export_Wh | export_VAh |
|--------------------|--------------|-----------|------------|-----------|------------|
| 2025-10-31 00:00:00 | PO34567890 | 2845 | 3161 | 24 | 27 |
| 2025-11-01 00:00:00 | PO34567890 | 6123 | 6803 | 48 | 53 |
| ... | ... | ... | ... | ... | ... |
```

**Features:**
- Filtered fields only
- All 31 days of data
- Sorted by date

#### Sheet 4: Profile Instant

**Data Source:** `POST https://mdms-api.stage.gomatimvvnl.in/db-service/profileinstant`

```python
| data_timestamp | badge_number | MD_W | MD_VA | voltage | frequency |
|----------------|--------------|------|-------|---------|-----------|
| 2025-10-31 00:00:00 | PO34567890 | 24 | 27 | 230 | 50.0 |
| 2025-11-01 00:00:00 | PO34567890 | 48 | 53 | 230 | 50.0 |
| ... | ... | ... | ... | ... | ... |
```

**Features:**
- Max demand data for all days
- Voltage and frequency info
- Sorted by timestamp

**Output File:** `Result_File/Report_PE_101.xlsx`

---

## Database Operations

### Connection Configuration

```python
DB_CONFIG = {
    'host': 'db_mdms.stage.mvvnl.internal',
    'database': 'validation_rules',
    'user': 'postgres',
    'password': 'LBjsKJkd937042!!',
    'port': 5432
}
```

### Tables Used

#### 1. dailyload_vee_validated

**Purpose:** Store daily cumulative consumption data

**Key Columns:**
- `device_identifier` - Meter serial number
- `data_timestamp` - Date and time (UTC-5:30)
- `import_Wh` - Cumulative import energy
- `import_VAh` - Cumulative import apparent energy
- `export_Wh` - Cumulative export energy
- `export_VAh` - Cumulative export apparent energy
- `meter_type` - "1-ph" or "3-ph"
- `is_valid`, `is_estimated`, `is_edited` - Data flags

**Insert Pattern:**
```python
insert_query = """
    INSERT INTO dailyload_vee_validated (
        device_identifier, data_timestamp, dcu_serial,
        import_Wh, import_VAh, export_Wh, export_VAh,
        data_source, data_type, is_valid, meter_type, ...
    ) VALUES (
        %(device_identifier)s, %(data_timestamp)s, %(dcu_serial)s,
        %(import_Wh)s, %(import_VAh)s, %(export_Wh)s, %(export_VAh)s,
        %(data_source)s, %(data_type)s, %(is_valid)s, %(meter_type)s, ...
    )
"""
cursor.executemany(insert_query, data_list)
```

#### 2. profile_instant_vee

**Purpose:** Store max demand and instantaneous meter readings

**Key Columns:**
- `device_identifier` - Meter serial number
- `data_timestamp` - Date and time
- `MD_W` - Max demand in watts
- `MD_VA` - Max demand in VA
- `MD_W_datetime`, `MD_VA_datetime` - When MD occurred
- `voltage`, `frequency`, `PF` - Power quality parameters
- `is_valid`, `is_estimated`, `is_edited` - Data flags

**Insert Pattern:**
```python
insert_query = """
    INSERT INTO profile_instant_vee (
        device_identifier, data_timestamp, MD_W, MD_VA,
        voltage, frequency, PF, is_valid, meter_type, ...
    ) VALUES (
        %(device_identifier)s, %(data_timestamp)s, %(MD_W)s, %(MD_VA)s,
        %(voltage)s, %(frequency)s, %(PF)s, %(is_valid)s, %(meter_type)s, ...
    )
"""
cursor.executemany(insert_query, data_list)
```

### Best Practices

1. **Use Bulk Insert:**
```python
# Good: Batch insert
cursor.executemany(query, data_list)

# Bad: Individual inserts
for data in data_list:
    cursor.execute(query, data)
```

2. **Transaction Management:**
```python
try:
    cursor.executemany(query, data_list)
    connection.commit()
except Exception as e:
    connection.rollback()
    logger.error(f"Error: {e}")
finally:
    connection.close()
```

3. **UTC Offset:**
```python
# Subtract 5:30 for database storage
start_date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
start_date_utc = start_date - timedelta(hours=5, minutes=30)
```

---

## API Integration

### 1. Account Creation API

**Endpoint:** `POST https://integration1.stage.gomatimvvnl.in/initial_master_sync/`

**Authentication:**
```python
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
}
```

**Payload Structure:**
```python
{
    "requestId": "12345678",
    "accountId": "1234567890",
    "consumerName": "John Smith",
    "address1": "Lucknow",
    "mobileNumber": 9876543210,
    "email": "johnsmith123@example.com",
    "supplyTypecode": "10",
    "meterSrno": "PO34567890",
    "sanctionedLoad": 1.0,
    "loadUnit": "KW",
    "meterInstalldate": "2025-11-01T00:00:00",
    "prepaidOpeningbalance": 4000.0,
    "edApplicable": "1",
    ...
}
```

**Response:**
```python
Status: 200 OK
Body: {"status": "success", "message": "Account created"}
```

### 2. Daily Ledger Trigger API

**Endpoint:** `GET https://engine-web.stage.gomatimvvnl.in/trigger_task/daily_ledger_task/{date}`

**Parameters:**
- `date` (path) - URL-encoded date string
- `wallet_balance_sync_flag` (query) - Boolean, usually False
- `account_id` (query) - Account ID to process

**Example:**
```python
date_encoded = "2024-11-30%2000%3A00%3A00"
url = f"{base}/trigger_task/daily_ledger_task/{date_encoded}?wallet_balance_sync_flag=False&account_id=1234567890"

response = requests.get(url, headers={'accept': 'application/json'})
```

### 3. MDMS Data Fetch APIs

**Daily Load API:**
```python
POST https://mdms-api.stage.gomatimvvnl.in/db-service/dailyloads

Payload: {
    "badge_numbers": ["PO34567890"],
    "page": 1,
    "limit": 100
}

Response: {
    "data": [
        {
            "badge_number": "PO34567890",
            "dailyload_datetime": "2025-10-31T00:00:00",
            "import_Wh": 3226,
            ...
        },
        ...
    ],
    "total": 31
}
```

**Profile Instant API:**
```python
POST https://mdms-api.stage.gomatimvvnl.in/db-service/profileinstant

Payload: {
    "badge_numbers": ["PO34567890"],
    "page": 1,
    "limit": 100
}

Response: {
    "data": [
        {
            "badge_number": "PO34567890",
            "data_timestamp": "2025-10-31T00:00:00",
            "MD_W": 24,
            ...
        },
        ...
    ],
    "total": 31
}
```

---

## Excel Report Generation

### Formatting

**Header Style:**
```python
header_fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
header_font = Font(bold=True, color="FFFFFF")

for cell in sheet[1]:
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center")
```

**Auto-Adjust Column Width:**
```python
for column in sheet.columns:
    max_length = 0
    column_letter = column[0].column_letter
    
    for cell in column:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(str(cell.value))
        except:
            pass
    
    adjusted_width = min(max_length + 2, 50)
    sheet.column_dimensions[column_letter].width = adjusted_width
```

### Data Filtering

**Daily Load - Extract Only Required Fields:**
```python
required_fields = [
    "dailyload_datetime",
    "badge_number",
    "meter_serial_number",
    "data_source",
    "data_type",
    "export_Wh",
    "import_Wh",
    "export_VAh",
    "import_VAh"
]

daily_load_filtered = []
for record in daily_load_data:
    filtered_record = {
        field: record.get(field, "")
        for field in required_fields
    }
    daily_load_filtered.append(filtered_record)
```

### Writing Data

```python
# Write headers
headers = list(df.columns)
sheet.append(headers)

# Write data rows
for row in df.itertuples(index=False):
    sheet.append(list(row))
```

---

## All Test Cases Reference

### Test Case Categories

#### PE_101 - PE_125: Basic Scenarios
- ST=10 (Normal 10A single-phase)
- Various consumption and MD patterns
- Flat rates and simple calculations

**Example:**
- **PE_101**: ≤100 kWh, ≤75% MD
- **PE_102**: ≤100 kWh, 75-100% MD
- **PE_103**: >100 kWh, tiered rates
- **PE_104**: >100 kWh, >100% MD, with EDP

#### PE_126 - PE_150: Green Energy
- Green energy flag = "Y"
- Solar/renewable integration
- Net energy calculations

#### PE_151 - PE_175: Net Metering
- Net meter flag = "Y"
- Import/export balance
- Bidirectional energy flow

#### PE_176 - PE_200: Seasonal Variations
- Off-season benefits
- Load variations
- Seasonal rate changes

#### PE_201 - PE_225: Edge Cases
- Zero consumption
- Negative balance
- Maximum limits
- Data anomalies

### Creating New Test Cases

**Template:**
```python
# Copy PE_101.py to PE_XXX.py
cp Test_Plan/PE_101.py Test_Plan/PE_226.py

# Update configuration
SUPPLY_TYPECODE = "20"  # Change as needed
END_WH = 150000         # Change target consumption
MD_W = 1200             # Change target MD

# Update test case info
test_case_id = "PE_226"
test_case_description = "Your description here"

# Update output filenames
excel_file = "Report_PE_226.xlsx"
log_file = "logs/PE_226.log"
```

---

## Incremental Trigger

### Purpose

Batch process multiple accounts that have pending ledger calculations.

### Module: Incremental_Trigger.py

**Function:** `trigger_incremental_task() -> bool`

**API Call:**
```python
GET https://engine-web.stage.gomatimvvnl.in/trigger_task/incremental_task/

Headers:
  accept: application/json
```

**When to Use:**
1. After running multiple test cases (PE_101, PE_102, etc.)
2. When accounts have data but no calculated ledger
3. For batch processing scheduled tasks

**Usage:**
```bash
# Standalone
python Test_Plan/Incremental_Trigger.py

# Programmatic
from Test_Plan.Incremental_Trigger import trigger_incremental_task
result = trigger_incremental_task()
```

**Workflow:**
```bash
# 1. Run multiple test cases
python Test_Plan/PE_101.py
python Test_Plan/PE_102.py
python Test_Plan/PE_103.py

# 2. Trigger batch processing
python Test_Plan/Incremental_Trigger.py
```

---

## Troubleshooting

### Common Issues

#### 1. Account Creation Fails

**Error:** "Account creation failed with status 400/500"

**Causes:**
- Invalid payload structure
- Missing required fields
- Duplicate account ID
- Network timeout

**Solutions:**
```python
# Check payload structure
print(json.dumps(payload, indent=2))

# Verify required fields
required = ['accountId', 'meterSrno', 'sanctionedLoad', ...]
missing = [f for f in required if f not in payload]
if missing:
    print(f"Missing fields: {missing}")

# Check for duplicates
# Generate new account ID and retry

# Increase timeout
response = requests.post(url, json=payload, timeout=60)
```

#### 2. Database Connection Error

**Error:** "could not connect to server"

**Causes:**
- Wrong credentials
- Network not accessible
- PostgreSQL server down
- Firewall blocking connection

**Solutions:**
```python
# Test connection
import psycopg2
try:
    conn = psycopg2.connect(**DB_CONFIG)
    print("Connection successful")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")

# Check network
# ping db_mdms.stage.mvvnl.internal

# Verify credentials
# Check DB_CONFIG values
```

#### 3. Data Insert Fails

**Error:** "duplicate key value violates unique constraint"

**Causes:**
- Data already exists for this meter/date
- Running test multiple times
- Previous test not cleaned up

**Solutions:**
```python
# Delete existing data before insert
delete_query = """
    DELETE FROM dailyload_vee_validated
    WHERE device_identifier = %s
    AND data_timestamp >= %s
    AND data_timestamp < %s
"""
cursor.execute(delete_query, (meter_srno, start_date, end_date))
connection.commit()

# Then insert new data
```

#### 4. API Timeout

**Error:** "requests.exceptions.Timeout"

**Causes:**
- API server slow
- Network latency
- Large data processing

**Solutions:**
```python
# Increase timeout
response = requests.get(url, timeout=120)

# Add retry logic
from time import sleep
max_retries = 3
for attempt in range(max_retries):
    try:
        response = requests.get(url, timeout=60)
        break
    except requests.Timeout:
        if attempt < max_retries - 1:
            sleep(10)
            continue
        raise
```

#### 5. Excel Report Error

**Error:** "No data available" in Excel sheets

**Causes:**
- APIs not returning data
- Wrong meter serial number
- Data not processed yet

**Solutions:**
```python
# Wait for processing
import time
time.sleep(30)  # Wait 30 seconds before fetching

# Verify meter number
print(f"Fetching data for: {meter_srno}")

# Check API response
response = requests.post(api_url, json=payload)
print(f"Status: {response.status_code}")
print(f"Data: {response.json()}")

# Verify data exists in database
query = "SELECT COUNT(*) FROM dailyload_vee_validated WHERE device_identifier = %s"
cursor.execute(query, (meter_srno,))
count = cursor.fetchone()[0]
print(f"Records found: {count}")
```

### Debug Mode

Enable detailed logging:

```python
# In test file
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/PE_101_debug.log'),
        logging.StreamHandler()
    ]
)
```

### Manual Verification

**Check Database:**
```sql
-- Check daily load data
SELECT * FROM dailyload_vee_validated
WHERE device_identifier = 'PO34567890'
ORDER BY data_timestamp;

-- Check profile instant data
SELECT * FROM profile_instant_vee
WHERE device_identifier = 'PO34567890'
ORDER BY data_timestamp;

-- Check for duplicates
SELECT data_timestamp, COUNT(*)
FROM dailyload_vee_validated
WHERE device_identifier = 'PO34567890'
GROUP BY data_timestamp
HAVING COUNT(*) > 1;
```

**Check API:**
```bash
# Account creation
curl -X POST "https://integration1.stage.gomatimvvnl.in/initial_master_sync/" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{"accountId": "1234567890", ...}'

# Ledger trigger
curl "https://engine-web.stage.gomatimvvnl.in/trigger_task/daily_ledger_task/2024-11-30%2000%3A00%3A00?account_id=1234567890"

# Data fetch
curl -X POST "https://mdms-api.stage.gomatimvvnl.in/db-service/dailyloads" \
  -H "Content-Type: application/json" \
  -d '{"badge_numbers": ["PO34567890"], "page": 1, "limit": 100}'
```

---

## Best Practices

### 1. Run Tests Sequentially

```bash
# Don't run tests in parallel
# They share database resources

# Good
python Test_Plan/PE_101.py
python Test_Plan/PE_102.py

# Bad (parallel)
python Test_Plan/PE_101.py & python Test_Plan/PE_102.py &
```

### 2. Clean Up After Tests

```python
# Add cleanup function
def cleanup_test_data(meter_srno, start_date, end_date):
    """Clean up test data from database"""
    connection = psycopg2.connect(**DB_CONFIG)
    cursor = connection.cursor()
    
    # Delete daily load
    cursor.execute("""
        DELETE FROM dailyload_vee_validated
        WHERE device_identifier = %s
        AND data_timestamp >= %s
        AND data_timestamp < %s
    """, (meter_srno, start_date, end_date))
    
    # Delete profile instant
    cursor.execute("""
        DELETE FROM profile_instant_vee
        WHERE device_identifier = %s
        AND data_timestamp >= %s
        AND data_timestamp < %s
    """, (meter_srno, start_date, end_date))
    
    connection.commit()
    connection.close()
```

### 3. Use Logging Effectively

```python
# Log key information
logger.info(f"Starting test: {test_case_id}")
logger.info(f"Account ID: {account_id}")
logger.info(f"Date range: {start_date} to {end_date}")

# Log progress
logger.info(f"Step 1/5: Creating account...")
logger.info(f"Step 2/5: Filling daily load data...")

# Log results
logger.info(f"Test completed successfully")
logger.info(f"Report: {excel_file}")
```

### 4. Verify Each Step

```python
def main():
    # Step 1
    account_data = create_account()
    if not account_data:
        logger.error("Step 1 failed")
        return  # Don't continue
    
    # Step 2
    if not fill_daily_load_data(account_data):
        logger.error("Step 2 failed")
        return
    
    # Continue...
```

### 5. Save Test Configuration

```python
# Save test parameters to JSON
test_config = {
    'test_case_id': 'PE_101',
    'account_id': account_id,
    'meter_srno': meter_srno,
    'supply_type': SUPPLY_TYPECODE,
    'sanctioned_load': SANCTIONED_LOAD,
    'end_wh': END_WH,
    'md_w': MD_W,
    'start_date': start_date,
    'end_date': end_date
}

with open(f'Result_File/config_PE_101.json', 'w') as f:
    json.dump(test_config, f, indent=2)
```

---

## Summary

Test Plan modules provide:
- ✅ Automated account creation
- ✅ Synthetic data generation
- ✅ Database integration
- ✅ API orchestration
- ✅ Comprehensive reporting

**Key Points:**
- Run sequentially, not in parallel
- Check logs after each step
- Verify data in database and APIs
- Clean up test data when done
- Use logging for debugging

For more information:
- See [API Documentation](API_DOCUMENTATION.md) for API details
- See [Formula Guide](FORMULA_GUIDE.md) for validation
- See [Examples](EXAMPLES.md) for code samples

