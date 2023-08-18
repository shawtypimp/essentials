import requests
from config import API_TOKEN

headers = {"x-api-key": API_TOKEN}

def get_photo(category):
    response = requests.get(
        'https://api.thecatapi.com/v1/images/search',
        params = {"category_ids": category},
        headers = headers  

    )
    return response 




