from data_extract import get_data
from transformations import get_airbnb_data

try:
    df = get_data()
    print("data fetched from API successfully")
    print("Starting Transformations for the data")
    final_df = get_airbnb_data(df)
    print(final_df.head())
except Exception as error:
    print(f'Error Occured : {error}')