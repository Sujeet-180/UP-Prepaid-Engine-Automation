#!/usr/bin/env python3
"""
verify_installation.py - Verify framework setup and dependencies
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
            print(f"   Install with: pip install {package}")
            all_ok = False
    
    return all_ok

def check_folders():
    """Check required folders"""
    import os
    
    folders = {
        'Formula': 'Formula validation scripts',
        'Test_Plan': 'Test case scripts',
        'docs': 'Documentation',
        'logs': 'Log files (auto-created)',
        'Result_File': 'Test results (auto-created)'
    }
    
    print("\nChecking folders:")
    all_ok = True
    
    for folder, description in folders.items():
        if os.path.exists(folder):
            print(f"✅ {folder:15} - {description}")
        else:
            if folder in ['logs', 'Result_File']:
                print(f"⚠️  {folder:15} - {description} (will be created automatically)")
            else:
                print(f"❌ {folder:15} - {description} (MISSING)")
                all_ok = False
    
    return all_ok

def check_files():
    """Check key files exist"""
    import os
    
    files = {
        'account.py': 'Consumer detail extractor',
        'Download_Ledger.py': 'Ledger downloader',
        'README.md': 'Main documentation',
        'requirements.txt': 'Python dependencies',
        'Formula/Formula_101.py': 'Basic formula validation',
        'Test_Plan/PE_101.py': 'Basic test case'
    }
    
    print("\nChecking key files:")
    all_ok = True
    
    for file, description in files.items():
        if os.path.exists(file):
            print(f"✅ {file:30} - {description}")
        else:
            print(f"❌ {file:30} - {description} (MISSING)")
            all_ok = False
    
    return all_ok

def check_database():
    """Check database connectivity (optional)"""
    print("\nChecking database connection:")
    
    try:
        import psycopg2
        
        # Note: Update these credentials as needed
        DB_CONFIG = {
            'host': 'db_mdms.stage.mvvnl.internal',
            'database': 'validation_rules',
            'user': 'postgres',
            'password': 'LBjsKJkd937042!!',
            'port': 5432
        }
        
        print("Attempting database connection...")
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        cursor.close()
        conn.close()
        
        print(f"✅ Database connected successfully")
        print(f"   PostgreSQL version: {version[0][:60]}...")
        return True
    except ImportError:
        print("⚠️  psycopg2 not installed (database features disabled)")
        return True  # Not a critical failure
    except Exception as e:
        print(f"⚠️  Database connection failed: {str(e)[:100]}")
        print("   This is optional - tests can still run")
        return True  # Not a critical failure

def check_api_connectivity():
    """Check API connectivity (optional)"""
    print("\nChecking API connectivity:")
    
    try:
        import requests
        
        # Test basic connectivity to stage API
        api_base = "https://engine-web.stage.gomatimvvnl.in"
        
        print(f"Testing connection to {api_base}...")
        response = requests.get(api_base, timeout=10)
        
        print(f"✅ API server reachable (Status: {response.status_code})")
        return True
    except ImportError:
        print("⚠️  requests not installed (API features disabled)")
        return True  # Not a critical failure
    except Exception as e:
        print(f"⚠️  API connection failed: {str(e)[:100]}")
        print("   Check network connectivity and VPN if required")
        return True  # Not a critical failure

def main():
    """Main verification"""
    print("="*70)
    print("UP Prepaid Engine Automation Framework - Installation Verification")
    print("="*70)
    print()
    
    checks = [
        ("Python Version", check_python_version),
        ("Python Packages", check_packages),
        ("Project Folders", check_folders),
        ("Project Files", check_files),
        ("Database Connectivity", check_database),
        ("API Connectivity", check_api_connectivity)
    ]
    
    results = []
    critical_failed = False
    
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
            
            # Critical checks that must pass
            if name in ["Python Version", "Python Packages", "Project Files"]:
                if not result:
                    critical_failed = True
        except Exception as e:
            print(f"❌ Error checking {name}: {e}")
            results.append((name, False))
            if name in ["Python Version", "Python Packages", "Project Files"]:
                critical_failed = True
        print()
    
    # Summary
    print("="*70)
    print("VERIFICATION SUMMARY")
    print("="*70)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{name:30} {status}")
    
    print("="*70)
    
    if critical_failed:
        print("\n❌ CRITICAL CHECKS FAILED")
        print("\nFramework is NOT ready to use.")
        print("\nAction Required:")
        print("1. Install missing Python packages:")
        print("   pip install -r requirements.txt")
        print("2. Ensure all project files are present")
        print("3. Run this verification again")
        return 1
    else:
        print("\n✅ ALL CRITICAL CHECKS PASSED")
        print("\nFramework is ready to use!")
        print("\nNote: Optional checks (Database, API) can be configured later.")
        print("\nNext Steps:")
        print("1. Review QUICK_START.md for usage")
        print("2. Run your first test: python Test_Plan/PE_101.py")
        print("3. Check logs/ folder for execution details")
        return 0

if __name__ == "__main__":
    sys.exit(main())
