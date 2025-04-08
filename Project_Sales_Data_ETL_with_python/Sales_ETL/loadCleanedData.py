# etl/load.py
import pandas as pd
from pathlib import Path

def load_data(df: pd.DataFrame, output_path: str) -> None:
    """
    Save the cleaned DataFrame as a CSV file.
    """
    try:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"Cleaned data saved to {output_path}. Shape: {df.shape}")
    except Exception as e:
        print(f"Error saving cleaned data: {e}")