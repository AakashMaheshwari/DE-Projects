# etl/extract.py
import pandas as pd
from pathlib import Path

def extract_data(file_path: str, sheet_name: str = 'Bike Sales') -> pd.DataFrame:
    """
    Extract data from Excel file.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print(f"Data extracted from {sheet_name} successfully. Shape: {df.shape}")
        return df
    except Exception as e:
        print(f"Error during extraction: {e}")
        return pd.DataFrame()