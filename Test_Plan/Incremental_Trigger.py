#!/usr/bin/env python3
"""
Incremental_Trigger.py - Trigger incremental_task API
"""

import requests
import logging
import os

# ===== CONFIGURATION =====

# API Configuration
LEDGER_API_BASE = "https://engine-web.stage.gomatimvvnl.in"

# Logging Configuration
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/Incremental_Trigger.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


# ===== FUNCTION =====

def trigger_incremental_task():
    """
    Trigger the incremental_task API
    
    Returns:
        bool: True if API call was successful (status 200), False otherwise
    """
    # Second API: incremental_task
    try:
        url2 = f"{LEDGER_API_BASE}/trigger_task/incremental_task/"
        logger.info(f"Calling API 2: {url2}")
        
        response2 = requests.get(
            url2,
            headers={'accept': 'application/json'}
        )
        
        logger.info(f"API 2 Response Status: {response2.status_code}")
        logger.info(f"API 2 Response Text: {response2.text}")
        
        if response2.status_code == 200:
            logger.info("API 2 (incremental_task) called successfully")
            return True
        else:
            logger.warning(f"API 2 returned status {response2.status_code}")
            return False
    except Exception as e:
        logger.error(f"Error calling API 2: {str(e)}")
        return False


# ===== MAIN EXECUTION =====

if __name__ == "__main__":
    # Example usage
    result = trigger_incremental_task()
    if result:
        logger.info("Incremental task triggered successfully")
    else:
        logger.error("Failed to trigger incremental task")

