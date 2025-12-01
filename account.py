#!/usr/bin/env python3
"""
account.py - Extract Consumer Details from Excel Reports
Reads all Report_PE_*.xlsx files from Result_File folder,
extracts Consumer Details sheet data with specified columns,
and saves to Consumer_details.csv
"""

import pandas as pd
import os
import sys
from pathlib import Path

# Configuration
RESULT_FOLDER = "Result_File"
SHEET_NAME = "Consumer Details"
OUTPUT_CSV = "Consumer_details.csv"

# Required columns to extract
REQUIRED_COLUMNS = [
    "accountId",
    "meterSrno",
    "supplyTypecode",
    "sanctionedLoad",
    "loadUnit",
    "meterInstalldate",
    "greenEnergyflag",
    "prepaidOpeningbalance"
]


def get_report_identifier(filename: str) -> str:
    """
    Extract report identifier from filename.
    Example: Report_PE_101.xlsx -> Report_PE_101
    """
    return os.path.splitext(filename)[0]


def extract_consumer_details(excel_file: str) -> pd.DataFrame:
    """
    Extract consumer details from a single Excel file.
    The Excel sheet has a key-value structure (Parameter/Value columns).
    
    Args:
        excel_file: Path to the Excel file
        
    Returns:
        DataFrame with consumer details including report identifier
    """
    try:
        # Read the Consumer Details sheet
        df = pd.read_excel(excel_file, sheet_name=SHEET_NAME)
        
        # Get the report identifier from filename
        report_id = get_report_identifier(os.path.basename(excel_file))
        
        # Check if the sheet has Parameter/Value structure
        if 'Parameter' not in df.columns or 'Value' not in df.columns:
            print(f"Warning: {os.path.basename(excel_file)} - Unexpected sheet structure")
            return pd.DataFrame(columns=["Report_ID"] + REQUIRED_COLUMNS)
        
        # Convert Parameter/Value pairs to a dictionary (case-insensitive key matching)
        data_dict = {}
        for _, row in df.iterrows():
            param = str(row['Parameter']).strip()
            value = row['Value']
            # Use case-insensitive matching for parameter names
            data_dict[param.lower()] = value
        
        # Create a single row dictionary with the report identifier and required fields
        row_data = {"Report_ID": report_id}
        
        # Map of parameter names (case-insensitive) to output column names
        param_mapping = {
            'accountid': 'accountId',
            'metersrno': 'meterSrno',
            'supplytypecode': 'supplyTypecode',
            'sanctionedload': 'sanctionedLoad',
            'loadunit': 'loadUnit',
            'meterinstalldate': 'meterInstalldate',
            'greenenergyflag': 'greenEnergyflag',
            'prepaidopeningbalance': 'prepaidOpeningbalance'
        }
        
        missing_params = []
        
        # Extract required parameters (case-insensitive)
        for param_lower, col_name in param_mapping.items():
            if param_lower in data_dict:
                row_data[col_name] = data_dict[param_lower]
            else:
                # Check for exact case matches as fallback
                found = False
                for key in data_dict.keys():
                    if key.lower() == param_lower:
                        row_data[col_name] = data_dict[key]
                        found = True
                        break
                if not found:
                    row_data[col_name] = None
                    missing_params.append(col_name)
        
        # Create DataFrame with single row
        result_df = pd.DataFrame([row_data])
        
        # Print info about missing parameters for this file
        if missing_params:
            print(f"Warning: {os.path.basename(excel_file)} - Missing parameters: {', '.join(missing_params)}")
        
        return result_df
        
    except FileNotFoundError:
        print(f"Error: File not found - {excel_file}")
        return pd.DataFrame(columns=["Report_ID"] + REQUIRED_COLUMNS)
    except ValueError as e:
        if "Worksheet named" in str(e):
            print(f"Error: Sheet '{SHEET_NAME}' not found in {os.path.basename(excel_file)}")
        else:
            print(f"Error processing {os.path.basename(excel_file)}: {str(e)}")
        return pd.DataFrame(columns=["Report_ID"] + REQUIRED_COLUMNS)
    except Exception as e:
        print(f"Error processing {os.path.basename(excel_file)}: {str(e)}")
        import traceback
        traceback.print_exc()
        return pd.DataFrame(columns=["Report_ID"] + REQUIRED_COLUMNS)


def process_all_reports() -> pd.DataFrame:
    """
    Process all Excel report files in the Result_File folder.
    
    Returns:
        Combined DataFrame with all consumer details
    """
    result_folder_path = Path(RESULT_FOLDER)
    
    if not result_folder_path.exists():
        print(f"Error: Folder '{RESULT_FOLDER}' does not exist!")
        return pd.DataFrame()
    
    # Find all Excel files matching the pattern
    excel_files = list(result_folder_path.glob("Report_PE_*.xlsx"))
    
    if not excel_files:
        print(f"No Excel files found in '{RESULT_FOLDER}' folder!")
        return pd.DataFrame()
    
    print(f"Found {len(excel_files)} Excel file(s) to process...")
    sys.stdout.flush()
    
    # Process each file and collect dataframes
    all_dataframes = []
    
    for excel_file in sorted(excel_files):
        print(f"Processing: {excel_file.name}...")
        sys.stdout.flush()
        df = extract_consumer_details(str(excel_file))
        
        if not df.empty:
            all_dataframes.append(df)
            print(f"  - Extracted {len(df)} record(s)")
            sys.stdout.flush()
    
    # Combine all dataframes
    if all_dataframes:
        combined_df = pd.concat(all_dataframes, ignore_index=True)
        print(f"\nTotal records extracted: {len(combined_df)}")
        return combined_df
    else:
        print("No data extracted from any files!")
        return pd.DataFrame()


def save_to_csv(df: pd.DataFrame, output_file: str):
    """
    Save DataFrame to CSV file.
    
    Args:
        df: DataFrame to save
        output_file: Output CSV filename
    """
    if df.empty:
        print("No data to save!")
        return
    
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"\nData saved successfully to '{output_file}'")
    print(f"Columns: {', '.join(df.columns.tolist())}")


def main():
    """
    Main function to extract and save consumer details.
    """
    print("=" * 60)
    print("Consumer Details Extraction Tool")
    print("=" * 60)
    
    # Process all Excel files
    combined_df = process_all_reports()
    
    # Save to CSV
    if not combined_df.empty:
        save_to_csv(combined_df, OUTPUT_CSV)
        
        # Display summary
        print("\n" + "=" * 60)
        print("Summary:")
        print("=" * 60)
        print(f"Total records: {len(combined_df)}")
        print(f"Output file: {OUTPUT_CSV}")
        print(f"Unique reports processed: {combined_df['Report_ID'].nunique()}")
    else:
        print("\nNo data was extracted. Please check the Excel files and try again.")


if __name__ == "__main__":
    main()

