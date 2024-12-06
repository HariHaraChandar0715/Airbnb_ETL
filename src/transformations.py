import pandas as pd
from pandas import DataFrame

def get_airbnb_data(df:DataFrame):
    has_next_page = True

    while has_next_page != False:
        try:
            index=0
            host_type = df['data'][0]['badges'][0]
            latitude = df['data'][0]['coordinates']['latitude']
            longitude = df['data'][0]['coordinates']['longitude']
            stay_id = df['data'][0]['id']
            currency = df['data'][0]['price']['currency']
            original_price_per_night = df['data'][0]['price']['originalPricePerNight']
            ratings = df['data'][0]['rating']
            total_reviews = df['data'][0]['reviews']
            room_type = df['data'][0]['roomType']
            title = df['data'][0]['title']

            final_data = {
                'host':[host_type],
                'latitude':[latitude],
                'longitude':[longitude],
                'stay_id':[stay_id],
                'currency':[currency],
                'original_price':[original_price_per_night],
                'ratings':[ratings],
                'total_reviews':[total_reviews],
                'room_type':[room_type],
                'title':[title]
            }
            prdf = pd.DataFrame(final_data)

        except Exception as error:
            print(f'Error : {error}')
            return None
    return prdf
