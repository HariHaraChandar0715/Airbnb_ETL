import requests
from dotenv import load_dotenv
import os 

load_dotenv()





def fetch_data_from_api():

    rapid_api_key = os.getenv('RAPID_API_KEY')
    rapid_api_host = os.getenv('RAPID_API_HOST')
    
    url = os.getenv('URL')
    querystring = {"location": "banglore"}
    has_next_page = False
    cursor = None
    response = None
    

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": rapid_api_host
    }
    if has_next_page is False:
        response = requests.get(url=url, headers=headers, params=querystring)
        cursor = response['data']['endCursor']
    else:
        querystring['cursor'] = cursor

    ardf = response.json()

    
    return ardf

