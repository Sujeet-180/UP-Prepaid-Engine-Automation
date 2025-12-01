import requests
import pandas as pd
import os
import sys
import json
from datetime import datetime

# Ensure openpyxl is installed for Excel writing
try:
    import openpyxl
except ImportError:
    print("ERROR: openpyxl module is not installed. Install it using: pip install openpyxl")
    exit()

# API Base URL
API_URL = "https://engine-web.stage.gomatimvvnl.in/daily_prepaid_ledger/"

# CSV file path
CSV_FILE = "Consumer_details.csv"

# Required fields for Excel
REQUIRED_FIELDS = [
    "start_date_time", 
    "end_date_time", 
    "account_id", 
    "meter_number", 
    "applied_supply_type_code", 
    "daily_consumption", 
    "cumm_daily_consumption_mtd", 
    "daily_consumption_in_rupees", 
    "cumm_daily_consumption_rupees_mtd",
    "remaining_ec_life_line_switch_charge",
    "cumm_ec_life_line_switch_charge_deducted", 
    "max_demand", 
    "daily_max_demand_penalty", 
    "cumm_daily_max_demand_penalty_mtd", 
    "daily_fixed_charge_adjustment", 
    "cumm_daily_fixed_charge_adjustment_mtd", 
    "daily_fixed_charges", 
    "cumm_daily_fixed_charges_mtd", 
    "remaining_fc_life_line_switch_charge",
    "cumm_fc_life_line_switch_charge_deducted",
    "daily_ec_final_charge", 
    "cumm_ec_final_charges_mtd", 
    "daily_fc_final_charge", 
    "cumm_fc_final_charges_mtd", 
    "daily_ec_plus_fc_charge", 
    "cumm_daily_ec_plus_fc_charge_mtd", 
    # "daily_flat_rate_subsidy", 
    # "cumm_daily_flat_rate_subsidy_mtd", 
    # "daily_ec_plus_fc_post_subsidy", 
    # "cumm_daily_ec_plus_fc_post_subsidy_mtd", 
    # "daily_mmc_charge", 
    # "cumm_mmc_mtd", 
    # "weekly_cumm_ec_charge_mtd", 
    # "weekly_cumm_fc_charge_mtd", 
    # "weekly_cumm_mmc_charge_mtd", 
    # "last_week_cumm_net_payable_mtd", 
    # "daily_net_payable", 
    # "cumm_net_payable_mtd", 
    "daily_ed_charge", 
    "cumm_ed_charges_mtd", 
    "daily_final_rebate", 
    "cumm_daily_final_rebate_mtd", 
    "daily_green_energy_consumption_in_rupees",
    "cumm_daily_green_energy_consumption_rupees_mtd",
    # "daily_late_payment_surcharge", 
    # "cumm_daily_late_payment_surcharge_mtd", 
    # "daily_flat_rate_charges", 
    # "cumm_daily_flat_rate_charges_mtd", 
    "daily_final_charge", 
    "cumm_daily_final_charge_mtd", 
    "opening_balance", 
    "closing_balance"
]


def read_consumer_details():
    """Read account IDs, meter numbers, and Report IDs from CSV file."""
    try:
        # Read CSV with accountId and meterSrno as strings to preserve leading zeros
        df = pd.read_csv(CSV_FILE, dtype={'accountId': str, 'meterSrno': str, 'Report_ID': str})
        
        # Check if required columns exist
        if 'accountId' not in df.columns or 'meterSrno' not in df.columns:
            print(f"ERROR: CSV file must contain 'accountId' and 'meterSrno' columns.")
            print(f"Available columns: {list(df.columns)}")
            return []
        
        # Check if Report_ID column exists
        if 'Report_ID' not in df.columns:
            print(f"WARNING: 'Report_ID' column not found. Will use accountId_meterSrno for sheet names.")
            df['Report_ID'] = df['accountId'].astype(str) + '_' + df['meterSrno'].astype(str)
        
        # Filter out rows with empty accountId or meterSrno
        df_filtered = df.dropna(subset=['accountId', 'meterSrno'])
        df_filtered = df_filtered[df_filtered['accountId'].str.strip() != '']
        df_filtered = df_filtered[df_filtered['meterSrno'].str.strip() != '']
        
        # Get account IDs, meter numbers, and Report IDs (already strings, just strip whitespace)
        account_ids = df_filtered['accountId'].str.strip().tolist()
        meter_numbers = df_filtered['meterSrno'].str.strip().tolist()
        report_ids = df_filtered['Report_ID'].str.strip().tolist()
        
        if not account_ids:
            print("WARNING: No valid accountId and meterSrno data found in CSV file.")
            return []
        
        return list(zip(report_ids, account_ids, meter_numbers))
    except FileNotFoundError:
        print(f"ERROR: CSV file '{CSV_FILE}' not found in the current directory.")
        return []
    except Exception as e:
        print(f"ERROR: Failed to read CSV file: {e}")
        return []


def fetch_and_save_data():
    """Fetch data from API for all consumers in CSV and save to Excel."""
    # Read consumer details from CSV
    consumer_data = read_consumer_details()
    
    if not consumer_data:
        print("ERROR: No valid consumer data found in CSV file.")
        return
    
    print(f"Found {len(consumer_data)} consumer(s) to process...")
    
    # Generate output file name with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"Prepaid_Ledger_Report.xlsx"
    
    has_data = False
    success_count = 0
    error_count = 0
    error_list = []  # List to store error details

    try:
        with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
            for report_id, account_id, meter_number in consumer_data:
                url = f"{API_URL}{account_id}/?meter_number={meter_number}"
                headers = {"accept": "application/json"}

                try:
                    print(f"Processing {report_id} (Account: {account_id}, Meter: {meter_number})...")
                    sys.stdout.flush()
                    response = requests.get(url, headers=headers, timeout=30)
                    response.raise_for_status()
                    data = response.json()
                    
                    if not isinstance(data, list):
                        data = [data]
                    
                    filtered_data = [{key: item.get(key, None) for key in REQUIRED_FIELDS} for item in data]
                    df = pd.DataFrame(filtered_data)
                    
                    if not df.empty:
                        # Use Report_ID for sheet name (Excel sheet names are limited to 31 characters)
                        sheet_name = str(report_id)[:31]
                        df.to_excel(writer, sheet_name=sheet_name, index=False)
                        has_data = True
                        success_count += 1
                        print(f"  [OK] Data fetched successfully")
                    else:
                        error_count += 1
                        error_list.append({
                            'Report_ID': report_id,
                            'Account_ID': account_id,
                            'Meter_Number': meter_number,
                            'Error_Type': 'No Data',
                            'Error_Message': 'API returned empty data',
                            'Status_Code': '200',
                            'API_Response': json.dumps(data, indent=2) if data else 'Empty response'
                        })
                        print(f"  [WARNING] No data returned")
                    sys.stdout.flush()
                
                except requests.exceptions.HTTPError as e:
                    error_count += 1
                    # Try to get the API response body
                    api_response = ""
                    try:
                        if e.response is not None:
                            api_response = e.response.text
                            # Try to parse as JSON for better formatting
                            try:
                                json_response = e.response.json()
                                api_response = json.dumps(json_response, indent=2)
                            except:
                                # If not JSON, use text as is (truncate if too long)
                                if len(api_response) > 1000:
                                    api_response = api_response[:1000] + "... (truncated)"
                    except:
                        api_response = "Unable to retrieve response"
                    
                    error_msg = f"HTTP {e.response.status_code}: {str(e)}"
                    if e.response.status_code == 404:
                        error_msg = "Account not found (404)"
                    
                    error_list.append({
                        'Report_ID': report_id,
                        'Account_ID': account_id,
                        'Meter_Number': meter_number,
                        'Error_Type': 'HTTP Error',
                        'Error_Message': error_msg,
                        'Status_Code': str(e.response.status_code),
                        'API_Response': api_response
                    })
                    # Don't print errors to console, they'll be in Excel
                    sys.stdout.flush()
                except requests.exceptions.Timeout:
                    error_count += 1
                    error_list.append({
                        'Report_ID': report_id,
                        'Account_ID': account_id,
                        'Meter_Number': meter_number,
                        'Error_Type': 'Timeout',
                        'Error_Message': 'Request timeout after 30 seconds',
                        'Status_Code': 'N/A',
                        'API_Response': 'N/A - Request timed out before response'
                    })
                    sys.stdout.flush()
                except requests.exceptions.RequestException as e:
                    error_count += 1
                    error_list.append({
                        'Report_ID': report_id,
                        'Account_ID': account_id,
                        'Meter_Number': meter_number,
                        'Error_Type': 'Request Error',
                        'Error_Message': str(e),
                        'Status_Code': 'N/A',
                        'API_Response': 'N/A - Request failed before response'
                    })
                    sys.stdout.flush()
                except Exception as e:
                    error_count += 1
                    error_list.append({
                        'Report_ID': report_id,
                        'Account_ID': account_id,
                        'Meter_Number': meter_number,
                        'Error_Type': 'Unexpected Error',
                        'Error_Message': str(e),
                        'Status_Code': 'N/A',
                        'API_Response': 'N/A - Unexpected error occurred'
                    })
                    sys.stdout.flush()
            
            # Add errors sheet if there are any errors
            if error_list:
                error_df = pd.DataFrame(error_list)
                error_df.to_excel(writer, sheet_name='Errors', index=False)
                has_data = True
            
            # If no data was found, create a summary sheet to avoid "no visible sheets" error
            if not has_data:
                summary_df = pd.DataFrame({
                    'Status': ['No data found'],
                    'Message': [f'Processed {len(consumer_data)} consumer(s) but no data was retrieved.'],
                    'Total Processed': [len(consumer_data)],
                    'Successful': [success_count],
                    'Errors': [error_count]
                })
                summary_df.to_excel(writer, sheet_name='Summary', index=False)
                has_data = True  # Set to True so file is created
        
        print("\n" + "="*50)
        if has_data:
            print(f"SUCCESS: Excel file saved successfully!")
            print(f"Location: {os.path.abspath(file_path)}")
            print(f"Total processed: {len(consumer_data)}")
            print(f"Successful: {success_count}")
            if error_count > 0:
                print(f"Errors: {error_count} (see 'Errors' sheet in Excel file)")
            else:
                print(f"Errors: {error_count}")
        else:
            print("WARNING: No valid data found. Excel file not created.")
    
    except Exception as e:
        print(f"\n[ERROR] Failed to create Excel file: {e}")
        # If file was partially created, try to remove it
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"Removed incomplete file: {file_path}")
            except:
                pass


if __name__ == "__main__":
    print("Starting ledger data download...")
    print("="*50)
    fetch_and_save_data()
