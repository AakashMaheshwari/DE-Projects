from Sales_ETL.DataExtraction import extract_data
from Sales_ETL.DataTransformation import transform_data
from Sales_ETL.loadCleanedData import load_data

if __name__ == "__main__":
    input_file = "Data/uncleaned bike sales data.xlsx"
    output_file = "Data/cleaned/cleaned_bike_sales_data.csv"

    # Run ETL
    raw_df = extract_data(input_file)
    cleaned_df = transform_data(raw_df)
    load_data(cleaned_df, output_file)