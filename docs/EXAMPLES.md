# Examples and Usage Recipes

## Table of Contents
- [Overview](#overview)
- [Quick Start Examples](#quick-start-examples)
- [Core Module Examples](#core-module-examples)
- [Formula Validation Examples](#formula-validation-examples)
- [Test Plan Examples](#test-plan-examples)
- [Advanced Recipes](#advanced-recipes)
- [Automation Scripts](#automation-scripts)
- [Integration Examples](#integration-examples)
- [Custom Extensions](#custom-extensions)

---

## Overview

This guide provides practical examples and recipes for common tasks in the UP Prepaid Engine Automation Framework.

### Example Categories

- 🚀 **Quick Start** - Get up and running fast
- 📊 **Core Modules** - Extract and download data
- 🧮 **Formula Validation** - Validate calculations
- 🧪 **Test Plans** - Execute test cases
- 🎯 **Advanced** - Complex workflows
- 🤖 **Automation** - Batch processing scripts
- 🔧 **Custom** - Extend functionality

---

## Quick Start Examples

### Example 1: Complete Workflow

Run a complete test cycle from start to finish.

```bash
#!/bin/bash
# complete_workflow.sh

echo "=========================================="
echo "UP Prepaid Engine - Complete Test Workflow"
echo "=========================================="

# Step 1: Execute Test Case
echo -e "\n[Step 1/4] Executing Test Case PE_101..."
python Test_Plan/PE_101.py
if [ $? -ne 0 ]; then
    echo "ERROR: Test execution failed!"
    exit 1
fi

# Wait for processing
echo "Waiting 30 seconds for data processing..."
sleep 30

# Step 2: Extract Consumer Details
echo -e "\n[Step 2/4] Extracting Consumer Details..."
python account.py
if [ $? -ne 0 ]; then
    echo "ERROR: Consumer extraction failed!"
    exit 1
fi

# Step 3: Download Ledger Data
echo -e "\n[Step 3/4] Downloading Ledger Data..."
python Download_Ledger.py
if [ $? -ne 0 ]; then
    echo "ERROR: Ledger download failed!"
    exit 1
fi

# Step 4: Validate Formulas
echo -e "\n[Step 4/4] Validating Formulas..."
python Formula/Formula_101.py
if [ $? -ne 0 ]; then
    echo "ERROR: Formula validation failed!"
    exit 1
fi

echo -e "\n=========================================="
echo "✅ All steps completed successfully!"
echo "=========================================="
echo "Results:"
echo "  - Test Report: Result_File/Report_PE_101.xlsx"
echo "  - Consumer Data: Consumer_details.csv"
echo "  - Ledger Data: Prepaid_Ledger_Report.xlsx"
echo "  - Validation: Formula_101.xlsx"
echo "  - Logs: logs/"
echo "=========================================="
```

**Usage:**
```bash
chmod +x complete_workflow.sh
./complete_workflow.sh
```

---

### Example 2: Verify Installation

Check that all dependencies are installed and accessible.

```python
#!/usr/bin/env python3
"""
verify_installation.py - Verify framework setup
"""

import sys

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7+ required")
        return False
    
    print("✅ Python version OK")
    return True

def check_packages():
    """Check required packages"""
    packages = {
        'pandas': 'Data manipulation',
        'numpy': 'Numerical operations',
        'requests': 'HTTP requests',
        'psycopg2': 'PostgreSQL connector',
        'openpyxl': 'Excel file handling'
    }
    
    print("\nChecking Python packages:")
    all_ok = True
    
    for package, description in packages.items():
        try:
            __import__(package)
            print(f"✅ {package:15} - {description}")
        except ImportError:
            print(f"❌ {package:15} - {description} (NOT INSTALLED)")
            all_ok = False
    
    return all_ok

def check_folders():
    """Check required folders"""
    import os
    
    folders = ['Formula', 'Test_Plan', 'logs', 'Result_File']
    
    print("\nChecking folders:")
    all_ok = True
    
    for folder in folders:
        if os.path.exists(folder):
            print(f"✅ {folder}")
        else:
            print(f"⚠️  {folder} (will be created automatically)")
    
    return all_ok

def check_database():
    """Check database connectivity"""
    print("\nChecking database connection:")
    
    try:
        import psycopg2
        
        DB_CONFIG = {
            'host': 'db_mdms.stage.mvvnl.internal',
            'database': 'validation_rules',
            'user': 'postgres',
            'password': 'LBjsKJkd937042!!',
            'port': 5432
        }
        
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        cursor.close()
        conn.close()
        
        print(f"✅ Database connected")
        print(f"   {version[0][:50]}...")
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def main():
    """Main verification"""
    print("="*60)
    print("UP Prepaid Engine Automation - Installation Verification")
    print("="*60)
    
    checks = [
        ("Python Version", check_python_version),
        ("Python Packages", check_packages),
        ("Folders", check_folders),
        ("Database", check_database)
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ Error checking {name}: {e}")
            results.append((name, False))
        print()
    
    # Summary
    print("="*60)
    print("Summary:")
    print("="*60)
    
    all_passed = True
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{name:20} {status}")
        if not result:
            all_passed = False
    
    print("="*60)
    
    if all_passed:
        print("✅ All checks passed! Framework is ready to use.")
        return 0
    else:
        print("❌ Some checks failed. Please install missing components.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

**Usage:**
```bash
python verify_installation.py
```

---

## Core Module Examples

### Example 3: Extract Consumer Details

```python
#!/usr/bin/env python3
"""
extract_consumers.py - Extract consumer details from reports
"""

from account import (
    process_all_reports,
    save_to_csv,
    OUTPUT_CSV
)

def main():
    """Extract and save consumer details"""
    print("Extracting consumer details from Excel reports...")
    
    # Process all reports in Result_File folder
    df = process_all_reports()
    
    if df.empty:
        print("No data found. Ensure Report_PE_*.xlsx files exist in Result_File/")
        return
    
    # Display summary
    print(f"\nExtracted {len(df)} consumer records")
    print(f"Columns: {', '.join(df.columns.tolist())}")
    
    # Save to CSV
    save_to_csv(df, OUTPUT_CSV)
    
    # Display first few records
    print(f"\nFirst 5 records:")
    print(df.head().to_string())
    
    # Check for missing data
    missing_counts = df.isnull().sum()
    if missing_counts.any():
        print(f"\nMissing data count:")
        print(missing_counts[missing_counts > 0])

if __name__ == "__main__":
    main()
```

---

### Example 4: Download Ledger for Single Consumer

```python
#!/usr/bin/env python3
"""
download_single_consumer.py - Download ledger for one consumer
"""

import requests
import pandas as pd

API_URL = "https://engine-web.stage.gomatimvvnl.in/daily_prepaid_ledger/"

def download_consumer_ledger(account_id, meter_number):
    """Download ledger for single consumer"""
    
    url = f"{API_URL}{account_id}/?meter_number={meter_number}"
    headers = {"accept": "application/json"}
    
    print(f"Fetching ledger for Account: {account_id}, Meter: {meter_number}")
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        
        if not isinstance(data, list):
            data = [data]
        
        df = pd.DataFrame(data)
        
        print(f"✅ Fetched {len(df)} records")
        
        # Save to Excel
        output_file = f"Ledger_{account_id}_{meter_number}.xlsx"
        df.to_excel(output_file, index=False)
        print(f"✅ Saved to {output_file}")
        
        # Display summary
        if 'daily_final_charge' in df.columns:
            total_charges = df['daily_final_charge'].sum()
            print(f"Total charges: {total_charges:.2f} Rs")
        
        if 'opening_balance' in df.columns and 'closing_balance' in df.columns:
            start_balance = df.iloc[0]['opening_balance']
            end_balance = df.iloc[-1]['closing_balance']
            print(f"Balance: {start_balance:.2f} → {end_balance:.2f} Rs")
        
        return df
        
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e.response.status_code}")
        if e.response.status_code == 404:
            print("Account not found")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    return None

def main():
    """Main function"""
    # Example usage
    account_id = "1234567890"
    meter_number = "PO34567890"
    
    df = download_consumer_ledger(account_id, meter_number)
    
    if df is not None:
        print("\nFirst 5 records:")
        print(df.head()[['start_date_time', 'daily_consumption', 
                         'daily_final_charge', 'closing_balance']])

if __name__ == "__main__":
    main()
```

---

## Formula Validation Examples

### Example 5: Custom Formula Validator

```python
#!/usr/bin/env python3
"""
custom_validator.py - Custom formula validation with different parameters
"""

import sys
sys.path.append('Formula')

from Formula_101 import PrepaidLedgerComparison

class CustomValidator(PrepaidLedgerComparison):
    """Custom validator with different rates"""
    
    def __init__(self, ec_rate=3.5, fc_rate=60):
        """Initialize with custom rates"""
        super().__init__()
        
        # Override rates
        self.ec_rate = ec_rate
        self.fc_rate = fc_rate
        
        print(f"Custom Validator initialized:")
        print(f"  EC Rate: {self.ec_rate} Rs/kWh")
        print(f"  FC Rate: {self.fc_rate} Rs/kW")

def main():
    """Run custom validation"""
    
    # Create validator with custom rates
    validator = CustomValidator(ec_rate=3.5, fc_rate=60)
    
    # Run validation
    validator.run_comparison()
    
    print("\nCustom validation completed!")
    print("Check Formula_101.xlsx for results")

if __name__ == "__main__":
    main()
```

---

### Example 6: Compare Multiple Scenarios

```python
#!/usr/bin/env python3
"""
compare_scenarios.py - Compare multiple rate scenarios
"""

import pandas as pd
from Formula.Formula_101 import PrepaidLedgerComparison

def validate_scenario(name, ec_rate, fc_rate, output_file):
    """Validate a single scenario"""
    print(f"\n{'='*60}")
    print(f"Scenario: {name}")
    print(f"EC Rate: {ec_rate}, FC Rate: {fc_rate}")
    print(f"{'='*60}")
    
    # Create validator
    validator = PrepaidLedgerComparison()
    validator.ec_rate = ec_rate
    validator.fc_rate = fc_rate
    
    # Fetch data
    df = validator.fetch_prepaid_ledger_data()
    if df.empty:
        print("❌ No data fetched")
        return None
    
    # Calculate expected
    df_calc = validator.calculate_expected_values(df)
    
    # Compare
    df_comp = validator.compare_values(df_calc)
    
    # Generate report
    validator.generate_comparison_report(df_comp, output_file)
    
    # Summary
    matches = len(df_comp[df_comp['Status'] == 'All Match'])
    total = len(df_comp)
    pct = (matches / total * 100) if total > 0 else 0
    
    print(f"✅ Result: {matches}/{total} days match ({pct:.2f}%)")
    
    return {
        'name': name,
        'ec_rate': ec_rate,
        'fc_rate': fc_rate,
        'matches': matches,
        'total': total,
        'percentage': pct
    }

def main():
    """Compare multiple scenarios"""
    
    scenarios = [
        ("Standard", 3.0, 50),
        ("High EC", 3.5, 50),
        ("High FC", 3.0, 60),
        ("Both High", 3.5, 60),
    ]
    
    results = []
    
    for i, (name, ec, fc) in enumerate(scenarios):
        output = f"Scenario_{i+1}_{name.replace(' ', '_')}.xlsx"
        result = validate_scenario(name, ec, fc, output)
        if result:
            results.append(result)
    
    # Summary table
    print(f"\n{'='*60}")
    print("COMPARISON SUMMARY")
    print(f"{'='*60}")
    
    df_results = pd.DataFrame(results)
    print(df_results.to_string(index=False))
    
    # Save summary
    df_results.to_csv("scenario_comparison.csv", index=False)
    print(f"\n✅ Summary saved to scenario_comparison.csv")

if __name__ == "__main__":
    main()
```

---

## Test Plan Examples

### Example 7: Create Custom Test Case

```python
#!/usr/bin/env python3
"""
custom_test_case.py - Create a custom test case with specific parameters
"""

from Test_Plan.PE_101 import (
    create_account,
    fill_daily_load_data,
    fill_profile_instant_data,
    trigger_prepaid_ledger,
    generate_excel_report,
    logger
)

# Custom configuration
CUSTOM_CONFIG = {
    'SUPPLY_TYPECODE': '20',
    'SANCTIONED_LOAD': 2,
    'END_WH': 150000,  # 150 kWh
    'MD_W': 1500,      # 1.5 kW
    'PREPAID_OPENING_BALANCE': 6000
}

def run_custom_test():
    """Run custom test case"""
    
    logger.info("="*60)
    logger.info("Custom Test Case - ST=20, 150kWh, 1.5kW MD")
    logger.info("="*60)
    
    # Step 1: Create account with custom config
    logger.info("Step 1: Creating account with custom parameters...")
    # Note: You'd need to modify create_account to accept parameters
    # For now, manually modify the constants in PE_101.py
    
    account_data = create_account()
    if not account_data:
        logger.error("Account creation failed")
        return False
    
    # Step 2-5: Standard workflow
    if not fill_daily_load_data(account_data):
        return False
    
    if not fill_profile_instant_data(account_data):
        return False
    
    if not trigger_prepaid_ledger(account_data['accountId']):
        return False
    
    if not generate_excel_report(account_data):
        return False
    
    logger.info("✅ Custom test completed successfully!")
    return True

if __name__ == "__main__":
    success = run_custom_test()
    exit(0 if success else 1)
```

---

### Example 8: Parallel Test Execution (Sequential)

```python
#!/usr/bin/env python3
"""
run_multiple_tests.py - Run multiple test cases sequentially
"""

import subprocess
import time
from datetime import datetime

def run_test(test_name):
    """Run a single test case"""
    print(f"\n{'='*60}")
    print(f"Running {test_name}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")
    
    start_time = time.time()
    
    try:
        result = subprocess.run(
            ['python', f'Test_Plan/{test_name}.py'],
            capture_output=True,
            text=True,
            timeout=600  # 10 minutes max
        )
        
        elapsed = time.time() - start_time
        
        if result.returncode == 0:
            print(f"✅ {test_name} PASSED ({elapsed:.1f}s)")
            return True
        else:
            print(f"❌ {test_name} FAILED ({elapsed:.1f}s)")
            print(f"Error: {result.stderr[:200]}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"❌ {test_name} TIMEOUT (>600s)")
        return False
    except Exception as e:
        print(f"❌ {test_name} ERROR: {e}")
        return False

def main():
    """Run multiple tests"""
    
    tests = [
        'PE_101',
        'PE_102',
        'PE_103',
        'PE_104',
        'PE_105'
    ]
    
    print("="*60)
    print(f"Running {len(tests)} test cases")
    print("="*60)
    
    results = {}
    overall_start = time.time()
    
    for test in tests:
        results[test] = run_test(test)
        
        # Wait between tests
        if test != tests[-1]:
            print("\nWaiting 10 seconds before next test...")
            time.sleep(10)
    
    # Summary
    overall_elapsed = time.time() - overall_start
    
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    
    passed = sum(1 for r in results.values() if r)
    failed = len(results) - passed
    
    for test, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test}: {status}")
    
    print(f"\nTotal: {passed} passed, {failed} failed")
    print(f"Time: {overall_elapsed:.1f}s")
    print(f"{'='*60}")
    
    return failed == 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
```

---

## Advanced Recipes

### Example 9: Automated Daily Test Runner

```python
#!/usr/bin/env python3
"""
daily_test_runner.py - Automated daily test execution with reporting
"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import subprocess
import pandas as pd

class DailyTestRunner:
    """Automated daily test runner"""
    
    def __init__(self, tests, email_config=None):
        self.tests = tests
        self.email_config = email_config
        self.results = []
        self.timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    def run_tests(self):
        """Run all tests"""
        print(f"Daily Test Run - {self.timestamp}")
        print("="*60)
        
        for test_id in self.tests:
            result = self._run_single_test(test_id)
            self.results.append(result)
        
        return self.results
    
    def _run_single_test(self, test_id):
        """Run single test"""
        start_time = datetime.now()
        
        try:
            result = subprocess.run(
                ['python', f'Test_Plan/{test_id}.py'],
                capture_output=True,
                text=True,
                timeout=600
            )
            
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            return {
                'test_id': test_id,
                'status': 'PASS' if result.returncode == 0 else 'FAIL',
                'duration': duration,
                'timestamp': start_time.strftime('%Y-%m-%d %H:%M:%S'),
                'error': result.stderr if result.returncode != 0 else None
            }
        except Exception as e:
            return {
                'test_id': test_id,
                'status': 'ERROR',
                'duration': 0,
                'timestamp': start_time.strftime('%Y-%m-%d %H:%M:%S'),
                'error': str(e)
            }
    
    def generate_report(self):
        """Generate test report"""
        df = pd.DataFrame(self.results)
        
        # Save to CSV
        report_file = f"daily_test_report_{self.timestamp}.csv"
        df.to_csv(report_file, index=False)
        
        # Print summary
        passed = len(df[df['status'] == 'PASS'])
        failed = len(df[df['status'] == 'FAIL'])
        errors = len(df[df['status'] == 'ERROR'])
        total_duration = df['duration'].sum()
        
        summary = f"""
Daily Test Report - {self.timestamp}
{'='*60}
Total Tests: {len(df)}
Passed: {passed}
Failed: {failed}
Errors: {errors}
Total Duration: {total_duration:.1f}s
{'='*60}

Details:
{df.to_string()}

Report saved to: {report_file}
"""
        
        print(summary)
        
        return summary, report_file
    
    def send_email_report(self, summary, report_file):
        """Send email report"""
        if not self.email_config:
            print("Email config not provided, skipping email")
            return
        
        msg = MIMEMultipart()
        msg['From'] = self.email_config['from']
        msg['To'] = self.email_config['to']
        msg['Subject'] = f"Daily Test Report - {self.timestamp}"
        
        msg.attach(MIMEText(summary, 'plain'))
        
        # Attach CSV
        with open(report_file, 'r') as f:
            attachment = MIMEText(f.read())
            attachment.add_header('Content-Disposition', 'attachment', 
                                filename=report_file)
            msg.attach(attachment)
        
        # Send
        try:
            server = smtplib.SMTP(self.email_config['smtp_host'], 
                                 self.email_config['smtp_port'])
            server.starttls()
            server.login(self.email_config['username'], 
                        self.email_config['password'])
            server.send_message(msg)
            server.quit()
            print("✅ Email sent successfully")
        except Exception as e:
            print(f"❌ Email failed: {e}")

def main():
    """Main function"""
    
    # Configure tests
    tests = ['PE_101', 'PE_102', 'PE_103']
    
    # Configure email (optional)
    email_config = {
        'from': 'automation@example.com',
        'to': 'team@example.com',
        'smtp_host': 'smtp.gmail.com',
        'smtp_port': 587,
        'username': 'your_username',
        'password': 'your_password'
    }
    
    # Run tests
    runner = DailyTestRunner(tests, email_config=None)  # Disable email
    runner.run_tests()
    
    # Generate report
    summary, report_file = runner.generate_report()
    
    # Send email (if configured)
    # runner.send_email_report(summary, report_file)

if __name__ == "__main__":
    main()
```

---

### Example 10: Data Cleanup Utility

```python
#!/usr/bin/env python3
"""
cleanup_utility.py - Clean up test data from database and files
"""

import psycopg2
import os
import glob
from datetime import datetime, timedelta

DB_CONFIG = {
    'host': 'db_mdms.stage.mvvnl.internal',
    'database': 'validation_rules',
    'user': 'postgres',
    'password': 'LBjsKJkd937042!!',
    'port': 5432
}

class CleanupUtility:
    """Utility to clean up test data"""
    
    def __init__(self, dry_run=True):
        self.dry_run = dry_run
        self.conn = None
    
    def connect_db(self):
        """Connect to database"""
        try:
            self.conn = psycopg2.connect(**DB_CONFIG)
            print("✅ Database connected")
            return True
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            return False
    
    def cleanup_database(self, meter_srno, start_date, end_date):
        """Clean up database records"""
        if not self.conn:
            print("❌ Database not connected")
            return
        
        cursor = self.conn.cursor()
        
        # Daily load
        query1 = """
            DELETE FROM dailyload_vee_validated
            WHERE device_identifier = %s
            AND data_timestamp >= %s
            AND data_timestamp < %s
        """
        
        # Profile instant
        query2 = """
            DELETE FROM profile_instant_vee
            WHERE device_identifier = %s
            AND data_timestamp >= %s
            AND data_timestamp < %s
        """
        
        try:
            if self.dry_run:
                # Just count
                cursor.execute(
                    "SELECT COUNT(*) FROM dailyload_vee_validated WHERE device_identifier = %s",
                    (meter_srno,)
                )
                count1 = cursor.fetchone()[0]
                
                cursor.execute(
                    "SELECT COUNT(*) FROM profile_instant_vee WHERE device_identifier = %s",
                    (meter_srno,)
                )
                count2 = cursor.fetchone()[0]
                
                print(f"[DRY RUN] Would delete:")
                print(f"  Daily load: {count1} records")
                print(f"  Profile instant: {count2} records")
            else:
                cursor.execute(query1, (meter_srno, start_date, end_date))
                count1 = cursor.rowcount
                
                cursor.execute(query2, (meter_srno, start_date, end_date))
                count2 = cursor.rowcount
                
                self.conn.commit()
                
                print(f"✅ Deleted from database:")
                print(f"  Daily load: {count1} records")
                print(f"  Profile instant: {count2} records")
        
        except Exception as e:
            print(f"❌ Database cleanup failed: {e}")
            self.conn.rollback()
        finally:
            cursor.close()
    
    def cleanup_files(self, pattern):
        """Clean up files matching pattern"""
        files = glob.glob(pattern)
        
        if not files:
            print(f"No files found matching: {pattern}")
            return
        
        print(f"\nFound {len(files)} file(s) matching: {pattern}")
        
        for f in files:
            if self.dry_run:
                print(f"[DRY RUN] Would delete: {f}")
            else:
                try:
                    os.remove(f)
                    print(f"✅ Deleted: {f}")
                except Exception as e:
                    print(f"❌ Failed to delete {f}: {e}")
    
    def cleanup_logs(self, days_old=7):
        """Clean up old log files"""
        cutoff_date = datetime.now() - timedelta(days=days_old)
        
        log_files = glob.glob("logs/*.log")
        deleted = 0
        
        for log_file in log_files:
            try:
                file_time = datetime.fromtimestamp(os.path.getmtime(log_file))
                
                if file_time < cutoff_date:
                    if self.dry_run:
                        print(f"[DRY RUN] Would delete old log: {log_file}")
                    else:
                        os.remove(log_file)
                        print(f"✅ Deleted old log: {log_file}")
                    deleted += 1
            except Exception as e:
                print(f"❌ Error processing {log_file}: {e}")
        
        print(f"\nCleaned up {deleted} log file(s) older than {days_old} days")
    
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()
            print("✅ Database disconnected")

def main():
    """Main cleanup"""
    import sys
    
    # Check if dry run
    dry_run = '--execute' not in sys.argv
    
    print("="*60)
    print("Cleanup Utility")
    print("="*60)
    
    if dry_run:
        print("Running in DRY RUN mode (use --execute to actually delete)")
    else:
        print("WARNING: Running in EXECUTE mode - data will be deleted!")
        response = input("Continue? (yes/no): ")
        if response.lower() != 'yes':
            print("Aborted")
            return
    
    print()
    
    cleanup = CleanupUtility(dry_run=dry_run)
    
    # Connect to database
    if cleanup.connect_db():
        # Example: Clean specific meter data
        meter_srno = "PO34567890"
        start_date = "2025-10-01 00:00:00"
        end_date = "2025-11-01 00:00:00"
        
        cleanup.cleanup_database(meter_srno, start_date, end_date)
    
    # Clean up files
    print("\nCleaning up files:")
    cleanup.cleanup_files("Formula_*.xlsx")
    cleanup.cleanup_files("Scenario_*.xlsx")
    cleanup.cleanup_files("Ledger_*.xlsx")
    
    # Clean up old logs
    print("\nCleaning up old logs:")
    cleanup.cleanup_logs(days_old=7)
    
    # Close
    cleanup.close()
    
    print("\n" + "="*60)
    print("Cleanup completed")
    print("="*60)

if __name__ == "__main__":
    main()
```

**Usage:**
```bash
# Dry run (default)
python cleanup_utility.py

# Actually execute
python cleanup_utility.py --execute
```

---

## Automation Scripts

### Example 11: Scheduled Test Runner (Cron)

```bash
#!/bin/bash
# scheduled_test.sh - Run daily automated tests

# Set working directory
cd /path/to/UP-Prepaid-Engine-Automation

# Activate virtual environment (if using)
# source venv/bin/activate

# Log file
LOG_FILE="logs/scheduled_$(date +%Y%m%d_%H%M%S).log"

# Run tests
echo "Starting scheduled test run at $(date)" | tee -a $LOG_FILE

python Test_Plan/PE_101.py 2>&1 | tee -a $LOG_FILE
python Test_Plan/PE_102.py 2>&1 | tee -a $LOG_FILE

# Extract consumer details
python account.py 2>&1 | tee -a $LOG_FILE

# Download ledger
python Download_Ledger.py 2>&1 | tee -a $LOG_FILE

# Validate formulas
python Formula/Formula_101.py 2>&1 | tee -a $LOG_FILE
python Formula/Formula_102.py 2>&1 | tee -a $LOG_FILE

echo "Completed at $(date)" | tee -a $LOG_FILE

# Send notification (optional)
# mail -s "Test Run Complete" admin@example.com < $LOG_FILE
```

**Crontab entry (daily at 2 AM):**
```cron
0 2 * * * /path/to/scheduled_test.sh
```

---

## Integration Examples

### Example 12: REST API Wrapper

```python
#!/usr/bin/env python3
"""
api_wrapper.py - REST API wrapper for automation framework
"""

from flask import Flask, jsonify, request
import subprocess
import threading

app = Flask(__name__)

# Store running tests
running_tests = {}

@app.route('/api/test/run', methods=['POST'])
def run_test():
    """Run a test case"""
    data = request.json
    test_id = data.get('test_id')
    
    if not test_id:
        return jsonify({'error': 'test_id required'}), 400
    
    # Check if already running
    if test_id in running_tests:
        return jsonify({'error': 'Test already running'}), 409
    
    # Run in background thread
    def run():
        result = subprocess.run(
            ['python', f'Test_Plan/{test_id}.py'],
            capture_output=True,
            text=True
        )
        running_tests[test_id] = {
            'status': 'completed',
            'exit_code': result.returncode,
            'stdout': result.stdout[:1000],
            'stderr': result.stderr[:1000]
        }
    
    running_tests[test_id] = {'status': 'running'}
    thread = threading.Thread(target=run)
    thread.start()
    
    return jsonify({
        'message': 'Test started',
        'test_id': test_id
    })

@app.route('/api/test/status/<test_id>', methods=['GET'])
def test_status(test_id):
    """Get test status"""
    if test_id not in running_tests:
        return jsonify({'error': 'Test not found'}), 404
    
    return jsonify(running_tests[test_id])

@app.route('/api/formula/validate', methods=['POST'])
def validate_formula():
    """Run formula validation"""
    data = request.json
    formula_id = data.get('formula_id', 'Formula_101')
    
    result = subprocess.run(
        ['python', f'Formula/{formula_id}.py'],
        capture_output=True,
        text=True
    )
    
    return jsonify({
        'exit_code': result.returncode,
        'status': 'PASS' if result.returncode == 0 else 'FAIL'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

**Usage:**
```bash
# Start API server
python api_wrapper.py

# Run test
curl -X POST http://localhost:5000/api/test/run \
  -H "Content-Type: application/json" \
  -d '{"test_id": "PE_101"}'

# Check status
curl http://localhost:5000/api/test/status/PE_101

# Validate formula
curl -X POST http://localhost:5000/api/formula/validate \
  -H "Content-Type: application/json" \
  -d '{"formula_id": "Formula_101"}'
```

---

## Custom Extensions

### Example 13: Custom Reporter

```python
#!/usr/bin/env python3
"""
custom_reporter.py - Generate custom HTML reports
"""

import pandas as pd
from pathlib import Path

class HTMLReporter:
    """Generate HTML test reports"""
    
    def __init__(self, title="Test Report"):
        self.title = title
        self.sections = []
    
    def add_section(self, heading, content):
        """Add a section to the report"""
        self.sections.append({
            'heading': heading,
            'content': content
        })
    
    def add_dataframe(self, heading, df):
        """Add a pandas DataFrame as a table"""
        html_table = df.to_html(index=False, classes='data-table')
        self.add_section(heading, html_table)
    
    def generate(self, output_file):
        """Generate HTML report"""
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{self.title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #366092;
            border-bottom: 3px solid #366092;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #555;
            margin-top: 30px;
        }}
        .data-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        .data-table th {{
            background-color: #366092;
            color: white;
            padding: 10px;
            text-align: left;
        }}
        .data-table td {{
            padding: 8px;
            border-bottom: 1px solid #ddd;
        }}
        .data-table tr:hover {{
            background-color: #f5f5f5;
        }}
        .pass {{
            color: green;
            font-weight: bold;
        }}
        .fail {{
            color: red;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{self.title}</h1>
"""
        
        for section in self.sections:
            html += f"""
        <h2>{section['heading']}</h2>
        {section['content']}
"""
        
        html += """
    </div>
</body>
</html>
"""
        
        with open(output_file, 'w') as f:
            f.write(html)
        
        print(f"✅ Report generated: {output_file}")

def main():
    """Generate sample report"""
    
    # Create reporter
    reporter = HTMLReporter("Prepaid Engine Test Report")
    
    # Add test results
    test_results = pd.DataFrame({
        'Test ID': ['PE_101', 'PE_102', 'PE_103'],
        'Description': ['Basic validation', 'Advanced validation', 'Complete validation'],
        'Status': ['PASS', 'PASS', 'FAIL'],
        'Duration': ['45s', '52s', '61s']
    })
    
    reporter.add_dataframe("Test Results", test_results)
    
    # Add formula validation
    formula_results = pd.DataFrame({
        'Formula': ['Formula_101', 'Formula_102', 'Formula_103'],
        'Total Records': [31, 31, 31],
        'Matched': [31, 30, 28],
        'Success Rate': ['100%', '96.8%', '90.3%']
    })
    
    reporter.add_dataframe("Formula Validation", formula_results)
    
    # Generate report
    reporter.generate('test_report.html')

if __name__ == "__main__":
    main()
```

---

## Summary

This guide provides practical examples for:

✅ **Quick Start** - Get running fast with complete workflows  
✅ **Core Modules** - Extract and download prepaid ledger data  
✅ **Formula Validation** - Validate calculations with custom parameters  
✅ **Test Plans** - Execute and customize test cases  
✅ **Advanced** - Automated runners, cleanup utilities  
✅ **Automation** - Scheduled execution, batch processing  
✅ **Integration** - REST API wrappers  
✅ **Extensions** - Custom reporters and tools  

### Next Steps

- Review [API Documentation](API_DOCUMENTATION.md) for detailed reference
- See [Formula Guide](FORMULA_GUIDE.md) for validation formulas
- Check [Test Plan Guide](TEST_PLAN_GUIDE.md) for test execution
- Refer to main [README](../README.md) for overview

### Contributing

Have a useful recipe or example? Contributions welcome!

1. Fork the repository
2. Add your example to this guide
3. Test thoroughly
4. Submit pull request

---

**Happy Automating! 🚀**
