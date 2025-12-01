import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
from typing import Dict, List, Tuple
import warnings
import logging
import os
warnings.filterwarnings('ignore')

# Create logs folder if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/Formula_103.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class PrepaidLedgerComparison:
    def __init__(self):
        # Configuration parameters - Updated with new rates
        self.contracted_load = 1  # kW
        self.fc_rate_0 = 50  # Rs. per kW (if cumm_daily_consumption_mtd <= 100 kWh)
        self.fc_rate_1 = 110  # Rs. per kW (if cumm_daily_consumption_mtd > 100 kWh)
        self.ed_rate = 0.05  # 5%
        self.rebate_rate = 0.02  # 2%
        self.opening_balance = 0
        self.ec_rate_0 = 3  # Rs. per kWh (upto 100 kWh)
        self.ec_rate_1 = 5.5  # Rs. per kWh (0 to 100 kWh when consumption crosses 100)
        self.ec_rate_2 = 5.5  # Rs. per kWh (101 to 150 kWh)
        self.ec_rate_3 = 6  # Rs. per kWh (151 to 300 kWh)
        self.ec_rate_4 = 6.5  # Rs. per kWh (above 301 kWh)
        self.days_in_month = 31
        
        # API configuration
        self.api_url = "https://engine-web.stage.gomatimvvnl.in/daily_prepaid_ledger/2222550013/"
        
        # Log account information
        logger.info("Test Case ID : Formula_103 - Prepaid Ledger Comparison")
        logger.info("Account ID: 2222550011")
        
        # Date range for energy consumption calculation
        self.start_date = "2025-10-01T00:00:00"
        self.end_date = "2025-11-01T00:00:00"  # End date is exclusive, covers all of October 2025
        logger.info(f"Date Range: {self.start_date} to {self.end_date} (exclusive end date)")
        
        
        # Required columns from API - Updated with new column names
        self.required_columns = [
            "start_date_time", 
            "end_date_time", 
            "account_id", 
            "meter_number", 
            "applied_supply_type_code", 
            "daily_consumption", 
            "cumm_daily_consumption_mtd", 
            "daily_consumption_in_rupees", 
            "cumm_daily_consumption_rupees_mtd",
            "cumm_ec_life_line_switch_charge_deducted",
            "remaining_ec_life_line_switch_charge",
            "daily_ec_final_charge",
            "cumm_ec_final_charges_mtd",
            "max_demand", 
            "daily_max_demand_penalty", 
            "cumm_daily_max_demand_penalty_mtd",
            "daily_fixed_charge_adjustment", 
            "cumm_daily_fixed_charge_adjustment_mtd", 
            "daily_fixed_charges", 
            "cumm_daily_fixed_charges_mtd",
            "cumm_fc_life_line_switch_charge_deducted",
            "remaining_fc_life_line_switch_charge",
            "daily_fc_final_charge", 
            "cumm_fc_final_charges_mtd", 
            "daily_ec_plus_fc_charge", 
            "cumm_daily_ec_plus_fc_charge_mtd", 
            "daily_ed_charge", 
            "cumm_ed_charges_mtd", 
            "daily_final_rebate", 
            "cumm_daily_final_rebate_mtd", 
            "daily_final_charge", 
            "cumm_daily_final_charge_mtd", 
            "opening_balance", 
            "closing_balance"
        ]
        
        # Columns to compare - Updated with new column names
        self.comparison_columns = [
            'daily_consumption',
            'cumm_daily_consumption_mtd',
            "daily_consumption_in_rupees", 
            "cumm_daily_consumption_rupees_mtd",
            "cumm_ec_life_line_switch_charge_deducted",
            "remaining_ec_life_line_switch_charge",
            "daily_ec_final_charge",
            "cumm_ec_final_charges_mtd",
            "max_demand", 
            "daily_max_demand_penalty", 
            "cumm_daily_max_demand_penalty_mtd",
            "daily_fixed_charge_adjustment", 
            "cumm_daily_fixed_charge_adjustment_mtd", 
            "daily_fixed_charges", 
            "cumm_daily_fixed_charges_mtd",
            "cumm_fc_life_line_switch_charge_deducted",
            "remaining_fc_life_line_switch_charge",
            "daily_fc_final_charge", 
            "cumm_fc_final_charges_mtd", 
            "daily_ec_plus_fc_charge", 
            "cumm_daily_ec_plus_fc_charge_mtd", 
            "daily_ed_charge", 
            "cumm_ed_charges_mtd", 
            "daily_final_rebate", 
            "cumm_daily_final_rebate_mtd", 
            "daily_final_charge", 
            "cumm_daily_final_charge_mtd", 
            "opening_balance", 
            "closing_balance"
        ]
    
    def fetch_prepaid_ledger_data(self) -> pd.DataFrame:
        """Fetch prepaid ledger data from API"""
        try:
            response = requests.get(self.api_url, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            
            if isinstance(data, dict) and 'data' in data:
                df = pd.DataFrame(data['data'])
            elif isinstance(data, list):
                df = pd.DataFrame(data)
            else:
                raise ValueError("Unexpected API response format")
            
            # Filter data for the specified date range
            df['start_date_time'] = pd.to_datetime(df['start_date_time'], utc=True)
            df['end_date_time'] = pd.to_datetime(df['end_date_time'], utc=True)
            
            start_dt = pd.to_datetime(self.start_date, utc=True)
            end_dt = pd.to_datetime(self.end_date, utc=True)
            
            df_filtered = df[
                (df['start_date_time'] >= start_dt) & 
                (df['start_date_time'] < end_dt)
            ].copy()
            
            # Sort by start_date_time to ensure proper order for cumulative calculations
            df_filtered = df_filtered.sort_values('start_date_time').reset_index(drop=True)
            
            logger.info(f"Fetched {len(df_filtered)} records for date range {self.start_date} to {self.end_date}")
            
            return df_filtered
            
        except Exception as e:
            return pd.DataFrame()
    
    def calculate_expected_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calculate expected values based on our formulas"""
        df_calc = df.copy()
        
        # Initialize running balance and cumulative values
        running_balance = self.opening_balance
        cumm_daily_consumption = 0
        cumm_daily_consumption_rupees = 0
        cumm_daily_max_demand_penalty = 0
        cumm_daily_fixed_charge_adjustment = 0
        cumm_daily_fixed_charges = 0
        cumm_ec_final_charges = 0
        cumm_fc_final_charges = 0
        cumm_daily_ec_plus_fc_charge = 0
        cumm_daily_ed_charge = 0
        cumm_daily_final_rebate = 0
        cumm_daily_final_charge = 0
        
        # Life line switch tracking variables
        cumm_ec_life_line_switch_charge_deducted = 0
        remaining_ec_life_line_switch_charge = 0
        cumm_fc_life_line_switch_charge_deducted = 0
        remaining_fc_life_line_switch_charge = 0
        life_line_switch_triggered = False
        days_since_life_line_switch = 0
        total_ec_life_line_switch_charge = 0
        total_fc_life_line_switch_charge = 0
        
        # Track previous day's max demand for fixed charge adjustment calculation
        previous_max_demand = 0
        previous_max_demand_percentage = 0
        previous_day = 0
        
        # Track EDP calculation variables for dynamic recalculation
        previous_max_demand_for_edp = 0
        previous_edp_daily_rate = 0
        days_with_previous_edp = 0
        total_edp_charged_so_far = 0
        
        # Calculate expected values for each row
        for idx, row in df_calc.iterrows():
            daily_consumption = row['daily_consumption']
            max_demand = row.get('max_demand', 0)
            current_day = idx + 1
            date_str = row['start_date_time'].strftime('%Y-%m-%d') if hasattr(row['start_date_time'], 'strftime') else str(row['start_date_time'])[:10]
            
            logger.info(f"**********DAY {current_day} - {date_str}************")
            
            logger.info(f"Daily Consumption: {daily_consumption:.4f} kWh")
            logger.info(f"Max Demand: {max_demand:.4f} kW")
            
            # Update cumulative consumption
            cumm_daily_consumption += daily_consumption
            
            # Check if life line switch should be triggered (consumption crosses 100 kWh)
            if cumm_daily_consumption > 100 and not life_line_switch_triggered:
                life_line_switch_triggered = True
                days_since_life_line_switch = 0
                
                # Calculate total EC life line switch charge
                # = ((previous day cumm_daily_consumption_mtd * ec_rate_1) - (previous day cumm_daily_consumption_mtd * ec_rate_0))
                previous_cumm_consumption = cumm_daily_consumption - daily_consumption
                total_ec_life_line_switch_charge = (previous_cumm_consumption * self.ec_rate_1) - (previous_cumm_consumption * self.ec_rate_0)
                remaining_ec_life_line_switch_charge = total_ec_life_line_switch_charge
                
                # Calculate total FC life line switch charge
                # = {(fc_rate_1 * contracted_load * (total no of days crossed - 1) * (max_demand / contracted_load)) / days_in_month } - { (fc_rate_0 * contracted_load * (total no of days crossed - 1) * (max_demand / contracted_load)) / days_in_month }
                days_crossed = current_day - 1
                max_demand_ratio = max_demand / self.contracted_load
                total_fc_life_line_switch_charge = ((self.fc_rate_1 * self.contracted_load * days_crossed * max_demand_ratio) / self.days_in_month) - ((self.fc_rate_0 * self.contracted_load * days_crossed * max_demand_ratio) / self.days_in_month)
                remaining_fc_life_line_switch_charge = total_fc_life_line_switch_charge
                
                logger.info(f"Day {current_day}: Life line switch triggered! Total EC switch charge: {total_ec_life_line_switch_charge:.4f}, Total FC switch charge: {total_fc_life_line_switch_charge:.4f}")
            
            # Calculate Daily EC with tiered rates
            expected_daily_ec = 0
            if cumm_daily_consumption <= 100:
                # Use ec_rate_0 for consumption up to 100 kWh
                expected_daily_ec = daily_consumption * self.ec_rate_0
            elif cumm_daily_consumption <= 150:
                # 101-150 kWh range: use ec_rate_2
                if cumm_daily_consumption - daily_consumption <= 100:
                    # Part of consumption is in 0-100 range, part in 101-150 range
                    consumption_in_0_100 = 100 - (cumm_daily_consumption - daily_consumption)
                    consumption_in_101_150 = daily_consumption - consumption_in_0_100
                    expected_daily_ec = (consumption_in_0_100 * self.ec_rate_0) + (consumption_in_101_150 * self.ec_rate_2)
                else:
                    # All consumption is in 101-150 range
                    expected_daily_ec = daily_consumption * self.ec_rate_2
            elif cumm_daily_consumption <= 300:
                # 151-300 kWh range: use ec_rate_3
                if cumm_daily_consumption - daily_consumption <= 100:
                    # Consumption spans multiple ranges
                    consumption_in_0_100 = 100 - (cumm_daily_consumption - daily_consumption)
                    consumption_in_101_150 = 50  # 101-150 range
                    consumption_in_151_300 = daily_consumption - consumption_in_0_100 - consumption_in_101_150
                    expected_daily_ec = (consumption_in_0_100 * self.ec_rate_0) + (consumption_in_101_150 * self.ec_rate_2) + (consumption_in_151_300 * self.ec_rate_3)
                elif cumm_daily_consumption - daily_consumption <= 150:
                    # Consumption spans 101-150 and 151-300 ranges
                    consumption_in_101_150 = 150 - (cumm_daily_consumption - daily_consumption)
                    consumption_in_151_300 = daily_consumption - consumption_in_101_150
                    expected_daily_ec = (consumption_in_101_150 * self.ec_rate_2) + (consumption_in_151_300 * self.ec_rate_3)
                else:
                    # All consumption is in 151-300 range
                    expected_daily_ec = daily_consumption * self.ec_rate_3
            else:
                # Above 300 kWh: use ec_rate_4
                if cumm_daily_consumption - daily_consumption <= 100:
                    # Consumption spans multiple ranges
                    consumption_in_0_100 = 100 - (cumm_daily_consumption - daily_consumption)
                    consumption_in_101_150 = 50  # 101-150 range
                    consumption_in_151_300 = 150  # 151-300 range
                    consumption_above_300 = daily_consumption - consumption_in_0_100 - consumption_in_101_150 - consumption_in_151_300
                    expected_daily_ec = (consumption_in_0_100 * self.ec_rate_0) + (consumption_in_101_150 * self.ec_rate_2) + (consumption_in_151_300 * self.ec_rate_3) + (consumption_above_300 * self.ec_rate_4)
                elif cumm_daily_consumption - daily_consumption <= 150:
                    # Consumption spans 101-150, 151-300, and above 300 ranges
                    consumption_in_101_150 = 150 - (cumm_daily_consumption - daily_consumption)
                    consumption_in_151_300 = 150  # 151-300 range
                    consumption_above_300 = daily_consumption - consumption_in_101_150 - consumption_in_151_300
                    expected_daily_ec = (consumption_in_101_150 * self.ec_rate_2) + (consumption_in_151_300 * self.ec_rate_3) + (consumption_above_300 * self.ec_rate_4)
                elif cumm_daily_consumption - daily_consumption <= 300:
                    # Consumption spans 151-300 and above 300 ranges
                    consumption_in_151_300 = 300 - (cumm_daily_consumption - daily_consumption)
                    consumption_above_300 = daily_consumption - consumption_in_151_300
                    expected_daily_ec = (consumption_in_151_300 * self.ec_rate_3) + (consumption_above_300 * self.ec_rate_4)
                else:
                    # All consumption is above 300 kWh
                    expected_daily_ec = daily_consumption * self.ec_rate_4
            
            logger.info(f"Daily EC: {expected_daily_ec:.4f} Rs.")
            
            # Calculate Daily EC Life Line Switch Charge (if applicable)
            daily_ec_life_line_switch_charge = 0
            if life_line_switch_triggered and days_since_life_line_switch < 3:
                daily_ec_life_line_switch_charge = total_ec_life_line_switch_charge / 3
                cumm_ec_life_line_switch_charge_deducted += daily_ec_life_line_switch_charge
                remaining_ec_life_line_switch_charge -= daily_ec_life_line_switch_charge
                days_since_life_line_switch += 1
            
            # Calculate Daily EC Final Charge = Daily EC - Daily EC Life Line Switch Charge
            expected_daily_ec_final_charge = expected_daily_ec - daily_ec_life_line_switch_charge
            
            # Determine FC rate based on consumption
            fc_rate = self.fc_rate_1 if cumm_daily_consumption > 100 else self.fc_rate_0
            
            # Calculate Daily Fixed Charges (FC) based on max demand percentage
            max_demand_percentage = (max_demand / self.contracted_load) * 100
            logger.info(f"Max Demand Percentage: ({max_demand:.4f} / {self.contracted_load}) x 100 = {max_demand_percentage:.4f}%")
            
            if max_demand_percentage <= 75:
                # FC (if max_Demand less than and equal to 75% of contracted load)
                expected_daily_fc = (0.75 * self.contracted_load * fc_rate) / self.days_in_month
                logger.info(f"Daily FC (<=75%): (0.75 x {self.contracted_load} x {fc_rate}) / {self.days_in_month} = {expected_daily_fc:.4f} Rs.")
            elif max_demand_percentage <= 100:
                # FC (if max_Demand between 75% to 100% of contracted load)
                expected_daily_fc = (fc_rate * self.contracted_load * (max_demand / self.contracted_load)) / self.days_in_month
                logger.info(f"Daily FC (75-100%): ({fc_rate} x {self.contracted_load} x ({max_demand:.4f} / {self.contracted_load})) / {self.days_in_month} = {expected_daily_fc:.4f} Rs.")
            else:
                # FC (if max_Demand greater than 100% of contracted load)
                expected_daily_fc = (fc_rate * self.contracted_load * (max_demand / self.contracted_load)) / self.days_in_month
                logger.info(f"Daily FC (>100%): ({fc_rate} x {self.contracted_load} x ({max_demand:.4f} / {self.contracted_load})) / {self.days_in_month} = {expected_daily_fc:.4f} Rs.")
            
            # Calculate Daily FC Life Line Switch Charge (if applicable)
            daily_fc_life_line_switch_charge = 0
            if life_line_switch_triggered and days_since_life_line_switch < 3:
                daily_fc_life_line_switch_charge = total_fc_life_line_switch_charge / 3
                cumm_fc_life_line_switch_charge_deducted += daily_fc_life_line_switch_charge
                remaining_fc_life_line_switch_charge -= daily_fc_life_line_switch_charge
            
            # Calculate Fixed Charge Adjustment (if md is greater than 75% of contracted load)
            expected_daily_fc_adjustment = 0
            if max_demand_percentage > 75 and previous_day > 0:
                # Fixed Charge Adjustment = ((FC Rate × Sanctioned Load × % of Contracted Load for Current Day × (Current Day − 1)) ÷ Total Number of Days in the Month) − ((FC Rate × Sanctioned Load × % of Contracted Load for Previous Day × (Current Day − 1)) ÷ Total Number of Days in the Month)
                current_day_percentage = max_demand / self.contracted_load
                previous_day_percentage = previous_max_demand / self.contracted_load
                
                current_adjustment = (fc_rate * self.contracted_load * current_day_percentage * (current_day - 1)) / self.days_in_month
                previous_adjustment = (fc_rate * self.contracted_load * previous_day_percentage * (current_day - 1)) / self.days_in_month
                
                expected_daily_fc_adjustment = current_adjustment - previous_adjustment
                logger.info(f"Daily FC Adjustment: {expected_daily_fc_adjustment:.4f} Rs.")
            else:
                logger.info(f"Daily FC Adjustment: 0.0000 Rs. (Max demand <= 75% or first day)")
            
            # Calculate final FC = FC + fixed charge adjustment - Daily FC Life Line Switch Charge
            expected_daily_fc_final_charge = expected_daily_fc + expected_daily_fc_adjustment - daily_fc_life_line_switch_charge
            logger.info(f"Daily FC Final: {expected_daily_fc:.4f} + {expected_daily_fc_adjustment:.4f} - {daily_fc_life_line_switch_charge:.4f} = {expected_daily_fc_final_charge:.4f} Rs.")
            
            # Calculate Daily EC + final FC
            expected_daily_ec_plus_fc = expected_daily_ec_final_charge + expected_daily_fc_final_charge
            logger.info(f"Daily EC + FC: {expected_daily_ec_final_charge:.4f} + {expected_daily_fc_final_charge:.4f} = {expected_daily_ec_plus_fc:.4f} Rs.")
            
            # Calculate Daily Excess Demand Penalty (EDP) (if md is greater than 100% of contracted load)
            expected_daily_edp = 0
            if max_demand_percentage > 100:
                excess_demand = max_demand - self.contracted_load
                remaining_days = self.days_in_month - current_day + 1
                
                if remaining_days > 0:
                    # Calculate new total penalty based on current max demand
                    new_total_penalty = excess_demand * fc_rate
                    
                    # Check if max demand has increased from previous value
                    if max_demand >= previous_max_demand_for_edp and previous_max_demand_for_edp > 0:
                        # Max demand has increased - need to recalculate
                        # Use previous day's cumulative EDP already charged
                        edp_already_charged = cumm_daily_max_demand_penalty
                        
                        # Calculate remaining penalty to be distributed
                        remaining_penalty = new_total_penalty - edp_already_charged
                        
                        if remaining_penalty > 0:
                            expected_daily_edp = remaining_penalty / remaining_days
                        else:
                            expected_daily_edp = 0
                        
                        logger.info(f"Day {current_day}: Max demand increased from {previous_max_demand_for_edp:.4f} to {max_demand:.4f}")
                        logger.info(f"  New total penalty: {new_total_penalty:.4f}")
                        logger.info(f"  Previous day cumm EDP already charged: {edp_already_charged:.4f}")
                        logger.info(f"  Remaining penalty: {remaining_penalty:.4f}")
                        logger.info(f"  Daily EDP: {expected_daily_edp:.4f}")
                    else:
                        # First time or max demand hasn't increased - normal calculation
                        expected_daily_edp = new_total_penalty / remaining_days
                    
                    # Update tracking variables
                    previous_max_demand_for_edp = max_demand
                    previous_edp_daily_rate = expected_daily_edp
                    days_with_previous_edp = 0  # Reset for new calculation
                    total_edp_charged_so_far = 0  # Reset for new calculation
                else:
                    expected_daily_edp = 0
            else:
                # If max demand is not > 100%, reset tracking variables
                if previous_max_demand_for_edp > 0:
                    # Update days with previous EDP
                    days_with_previous_edp += 1
                    total_edp_charged_so_far += previous_edp_daily_rate
            
            # Calculate Daily Electricity Duty (ED) = (EC final + FC final + EDP) * ED rate
            expected_daily_ed = (expected_daily_ec_final_charge + expected_daily_fc_final_charge + expected_daily_edp) * self.ed_rate
            logger.info(f"Daily ED: ({expected_daily_ec_final_charge:.4f} + {expected_daily_fc_final_charge:.4f} + {expected_daily_edp:.4f}) x {self.ed_rate} = {expected_daily_ed:.4f} Rs.")
            
            # Calculate Daily Rebate = (EC final + FC final) * Rebate rate
            expected_daily_rebate = (expected_daily_ec_final_charge + expected_daily_fc_final_charge) * self.rebate_rate
            logger.info(f"Daily Rebate: ({expected_daily_ec_final_charge:.4f} + {expected_daily_fc_final_charge:.4f}) x {self.rebate_rate} = {expected_daily_rebate:.4f} Rs.")
            
            # Calculate Daily Final charge = (EC final + FC final + ED + EDP) - Rebate
            expected_daily_final_charge = (expected_daily_ec_final_charge + expected_daily_fc_final_charge + expected_daily_ed + expected_daily_edp) - expected_daily_rebate
            logger.info(f"Daily Final Charge: ({expected_daily_ec_final_charge:.4f} + {expected_daily_fc_final_charge:.4f} + {expected_daily_ed:.4f} + {expected_daily_edp:.4f}) - {expected_daily_rebate:.4f} = {expected_daily_final_charge:.4f} Rs.")
            
            # Update cumulative values
            cumm_daily_consumption_rupees += expected_daily_ec
            cumm_daily_max_demand_penalty += expected_daily_edp
            cumm_daily_fixed_charge_adjustment += expected_daily_fc_adjustment
            cumm_daily_fixed_charges += expected_daily_fc
            cumm_ec_final_charges += expected_daily_ec_final_charge
            cumm_fc_final_charges += expected_daily_fc_final_charge
            cumm_daily_ec_plus_fc_charge += expected_daily_ec_plus_fc
            cumm_daily_ed_charge += expected_daily_ed
            cumm_daily_final_rebate += expected_daily_rebate
            cumm_daily_final_charge += expected_daily_final_charge
            
            # Calculate Expected Opening and Closing Balance
            if idx == 0:
                expected_opening_balance = self.opening_balance
            else:
                expected_opening_balance = running_balance
            
            expected_closing_balance = expected_opening_balance - expected_daily_final_charge
            
            # Update running balance for next iteration
            running_balance = expected_closing_balance
            
            # Update previous values for next iteration
            previous_max_demand = max_demand
            previous_day = current_day
            
            # Update EDP tracking for next iteration
            if max_demand_percentage > 100:
                days_with_previous_edp += 1
                total_edp_charged_so_far += expected_daily_edp
            
            logger.info(f"Opening Balance: {expected_opening_balance:.4f} Rs.")
            logger.info(f"Daily Final Charge: {expected_daily_final_charge:.4f} Rs.")
            logger.info(f"Closing Balance: {expected_opening_balance:.4f} - {expected_daily_final_charge:.4f} = {expected_closing_balance:.4f} Rs.")
            
            # Store expected calculated values
            df_calc.loc[idx, 'expected_daily_consumption_in_rupees'] = expected_daily_ec
            df_calc.loc[idx, 'expected_cumm_ec_life_line_switch_charge_deducted'] = cumm_ec_life_line_switch_charge_deducted
            df_calc.loc[idx, 'expected_remaining_ec_life_line_switch_charge'] = remaining_ec_life_line_switch_charge
            df_calc.loc[idx, 'expected_daily_ec_final_charge'] = expected_daily_ec_final_charge
            df_calc.loc[idx, 'expected_daily_max_demand_penalty'] = expected_daily_edp
            df_calc.loc[idx, 'expected_daily_fixed_charge_adjustment'] = expected_daily_fc_adjustment
            df_calc.loc[idx, 'expected_daily_fixed_charges'] = expected_daily_fc
            df_calc.loc[idx, 'expected_cumm_fc_life_line_switch_charge_deducted'] = cumm_fc_life_line_switch_charge_deducted
            df_calc.loc[idx, 'expected_remaining_fc_life_line_switch_charge'] = remaining_fc_life_line_switch_charge
            df_calc.loc[idx, 'expected_daily_fc_final_charge'] = expected_daily_fc_final_charge
            df_calc.loc[idx, 'expected_daily_ec_plus_fc_charge'] = expected_daily_ec_plus_fc
            df_calc.loc[idx, 'expected_daily_ed_charge'] = expected_daily_ed
            df_calc.loc[idx, 'expected_daily_final_rebate'] = expected_daily_rebate
            df_calc.loc[idx, 'expected_daily_final_charge'] = expected_daily_final_charge
            df_calc.loc[idx, 'expected_opening_balance'] = expected_opening_balance
            df_calc.loc[idx, 'expected_closing_balance'] = expected_closing_balance
            
            # Store expected cumulative values
            df_calc.loc[idx, 'expected_cumm_daily_consumption_rupees_mtd'] = cumm_daily_consumption_rupees
            df_calc.loc[idx, 'expected_cumm_ec_final_charges_mtd'] = cumm_ec_final_charges
            df_calc.loc[idx, 'expected_cumm_daily_max_demand_penalty_mtd'] = cumm_daily_max_demand_penalty
            df_calc.loc[idx, 'expected_cumm_daily_fixed_charge_adjustment_mtd'] = cumm_daily_fixed_charge_adjustment
            df_calc.loc[idx, 'expected_cumm_daily_fixed_charges_mtd'] = cumm_daily_fixed_charges
            df_calc.loc[idx, 'expected_cumm_fc_final_charges_mtd'] = cumm_fc_final_charges
            df_calc.loc[idx, 'expected_cumm_daily_ec_plus_fc_charge_mtd'] = cumm_daily_ec_plus_fc_charge
            df_calc.loc[idx, 'expected_cumm_ed_charges_mtd'] = cumm_daily_ed_charge
            df_calc.loc[idx, 'expected_cumm_daily_final_rebate_mtd'] = cumm_daily_final_rebate
            df_calc.loc[idx, 'expected_cumm_daily_final_charge_mtd'] = cumm_daily_final_charge
        
        return df_calc
    
    def compare_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Compare calculated vs expected values and generate status"""
        df_compare = df.copy()
        
        # Tolerance for floating point comparison
        tolerance = 0.01
        
        def check_match(actual_val, expected_val, col_name):
            """Check if actual and expected values match within tolerance"""
            try:
                actual = float(actual_val) if pd.notna(actual_val) else 0
                expected = float(expected_val) if pd.notna(expected_val) else 0
                return abs(actual - expected) <= tolerance
            except (ValueError, TypeError):
                return False
        
        # Compare each column and generate status
        mismatch_columns = []
        
        for col in self.comparison_columns:
            expected_col = f"expected_{col}"
            
            if expected_col in df_compare.columns:
                # Create comparison column
                df_compare[f"{col}_match"] = df_compare.apply(
                    lambda row: check_match(row[col], row[expected_col], col), 
                    axis=1
                )
                
                # Check if all values match for this column
                all_match = df_compare[f"{col}_match"].all()
                if not all_match:
                    mismatch_columns.append(col)
            else:
                pass
        
        # Generate overall status for each row
        def generate_row_status(row):
            row_mismatches = []
            for col in self.comparison_columns:
                match_col = f"{col}_match"
                if match_col in df_compare.columns:
                    if not row[match_col]:
                        row_mismatches.append(col)
            
            if not row_mismatches:
                return "All Match"
            else:
                return ", ".join(row_mismatches)
        
        df_compare['Status'] = df_compare.apply(generate_row_status, axis=1)
        
        all_match_count = len(df_compare[df_compare['Status'] == 'All Match'])
        
        # Log comprehensive comparison summary
        
        logger.info("===========================================")
        
        if mismatch_columns:
            logger.info("Mismatched Columns:")
            for col in mismatch_columns:
                logger.info(f"  - {col}")
        else:
            logger.info("All columns match perfectly!")
        
        # Log detailed mismatch analysis
        if len(df_compare) - all_match_count > 0:
            
            logger.info("DETAILED MISMATCH ANALYSIS")
            
            mismatch_records = df_compare[df_compare['Status'] != 'All Match']
            for idx, row in mismatch_records.iterrows():
                date_str = row['start_date_time'].strftime('%Y-%m-%d') if hasattr(row['start_date_time'], 'strftime') else str(row['start_date_time'])[:10]
                logger.info(f"Date: {date_str} - Status: {row['Status']}")
        
        return df_compare
    
    def generate_comparison_report(self, df: pd.DataFrame, filename: str = "Formula_103.xlsx"):
        """Generate comprehensive Excel report with comparison"""
        
        # Calculate final status and remarks for logging
        all_match_count = len(df[df['Status'] == 'All Match'])
        mismatch_count = len(df[df['Status'] != 'All Match'])
        
        if mismatch_count == 0:
            final_status = "PASS"
            remarks = "All ledger calculations are correct"
        else:
            final_status = "FAIL"
            # Get unique mismatch reasons
            mismatch_reasons = set()
            mismatch_records = df[df['Status'] != 'All Match']
            for _, row in mismatch_records.iterrows():
                if row['Status'] != 'All Match':
                    mismatch_reasons.add(row['Status'])
            remarks = f"Mismatches found in {mismatch_count} records. Issues: {', '.join(list(mismatch_reasons)[:3])}{'...' if len(mismatch_reasons) > 3 else ''}"
        
        # Log test case status
        logger.info(f"Test Case Result: {final_status}")
        logger.info(f"Total Records: {len(df)}")
        logger.info(f"Passed Records: {all_match_count}")
        logger.info(f"Failed Records: {mismatch_count}")
        logger.info(f"Success Rate: {(all_match_count/len(df)*100):.4f}%")
        logger.info(f"Remarks: {remarks}")
        logger.info(f"Test Case Report: {filename}")
        
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            # Main comparison sheet (renamed to "Prepaid_Ledger")
            comparison_columns = [
                'start_date_time', 'end_date_time', 'account_id', 'meter_number',
                'daily_consumption', 'cumm_daily_consumption_mtd',
                'daily_consumption_in_rupees', 'expected_daily_consumption_in_rupees',
                'cumm_daily_consumption_rupees_mtd', 'expected_cumm_daily_consumption_rupees_mtd',
                'cumm_ec_life_line_switch_charge_deducted', 'expected_cumm_ec_life_line_switch_charge_deducted',
                'remaining_ec_life_line_switch_charge', 'expected_remaining_ec_life_line_switch_charge',
                'daily_ec_final_charge', 'expected_daily_ec_final_charge',
                'cumm_ec_final_charges_mtd', 'expected_cumm_ec_final_charges_mtd',
                'max_demand',
                'daily_max_demand_penalty', 'expected_daily_max_demand_penalty',
                'cumm_daily_max_demand_penalty_mtd', 'expected_cumm_daily_max_demand_penalty_mtd',
                'daily_fixed_charge_adjustment', 'expected_daily_fixed_charge_adjustment',
                'cumm_daily_fixed_charge_adjustment_mtd', 'expected_cumm_daily_fixed_charge_adjustment_mtd',
                'daily_fixed_charges', 'expected_daily_fixed_charges',
                'cumm_daily_fixed_charges_mtd', 'expected_cumm_daily_fixed_charges_mtd',
                'cumm_fc_life_line_switch_charge_deducted', 'expected_cumm_fc_life_line_switch_charge_deducted',
                'remaining_fc_life_line_switch_charge', 'expected_remaining_fc_life_line_switch_charge',
                'daily_fc_final_charge', 'expected_daily_fc_final_charge',
                'cumm_fc_final_charges_mtd', 'expected_cumm_fc_final_charges_mtd',
                'daily_ec_plus_fc_charge', 'expected_daily_ec_plus_fc_charge',
                'cumm_daily_ec_plus_fc_charge_mtd', 'expected_cumm_daily_ec_plus_fc_charge_mtd',
                'daily_ed_charge', 'expected_daily_ed_charge',
                'cumm_ed_charges_mtd', 'expected_cumm_ed_charges_mtd',
                'daily_final_rebate', 'expected_daily_final_rebate',
                'cumm_daily_final_rebate_mtd', 'expected_cumm_daily_final_rebate_mtd',
                'daily_final_charge', 'expected_daily_final_charge',
                'cumm_daily_final_charge_mtd', 'expected_cumm_daily_final_charge_mtd',
                'opening_balance', 'expected_opening_balance',
                'closing_balance', 'expected_closing_balance',
                'Status'
            ]
            
            # Filter columns that exist in the dataframe
            available_columns = [col for col in comparison_columns if col in df.columns]
            comparison_df = df[available_columns].copy()
            
            # Format date columns for better readability
            if 'start_date_time' in comparison_df.columns:
                comparison_df['start_date_time'] = pd.to_datetime(comparison_df['start_date_time']).dt.strftime('%Y-%m-%d %H:%M:%S')
            if 'end_date_time' in comparison_df.columns:
                comparison_df['end_date_time'] = pd.to_datetime(comparison_df['end_date_time']).dt.strftime('%Y-%m-%d %H:%M:%S')
            
            # Format all numeric columns to 4 decimal places
            numeric_columns = comparison_df.select_dtypes(include=[np.number]).columns
            for col in numeric_columns:
                if col not in ['account_id']:  # Exclude account_id if it's numeric
                    comparison_df[col] = comparison_df[col].round(4)
            
            comparison_df.to_excel(writer, sheet_name='Prepaid_Ledger', index=False)
    
    def run_comparison(self):
        """Run the complete comparison process"""
        
        # Step 1: Fetch data from API
        df = self.fetch_prepaid_ledger_data()
        if df.empty:
            return
        
        # Step 2: Calculate expected values
        df_with_expected = self.calculate_expected_values(df)
        
        # Step 3: Compare values
        df_comparison = self.compare_values(df_with_expected)
        
        # Step 4: Generate comparison report
        self.generate_comparison_report(df_comparison)
        
        all_match_count = len(df_comparison[df_comparison['Status'] == 'All Match'])
        mismatch_count = len(df_comparison[df_comparison['Status'] != 'All Match'])
        
        # Final test case status logging
        test_status = "PASS" if mismatch_count == 0 else "FAIL"
        

        if test_status == "PASS":
            logger.info("PASS - All calculations are correct - Test Case PASSED")
        else:
            logger.info("FAIL - Some calculations have mismatches - Test Case FAILED")
        

def main():
    """Main function to run the comparison"""
    
    comparator = PrepaidLedgerComparison()
    comparator.run_comparison()

if __name__ == "__main__":
    main()
