# etl/transform.py
import pandas as pd

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

def standardize_country_names(df: pd.DataFrame) -> pd.DataFrame:
    df['country'] = df['country'].str.replace('  ', ' ').str.strip()
    return df

def fix_unit_cost(df: pd.DataFrame) -> pd.DataFrame:
    df['unit_cost'] = df['unit_cost'].replace(0, pd.NA)
    df['unit_cost'].fillna(df['unit_cost'].median(), inplace=True)
    return df

def recalculate_cost_profit(df: pd.DataFrame) -> pd.DataFrame:
    df['cost'] = df['order_quantity'] * df['unit_cost']
    df['revenue'] = df['order_quantity'] * df['unit_price']
    df['profit'] = df['revenue'] - df['cost']
    return df

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = clean_column_names(df)
    df = standardize_country_names(df)
    df = fix_unit_cost(df)
    df = recalculate_cost_profit(df)
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['sales_order_#', 'date'], inplace=True)
    return df