from typing import Any, List
from dotenv import load_dotenv
import requests
import os

load_dotenv()

anime_base_url = os.getenv('BASE_URL')
anime_bearer_token = os.getenv('BEARER_TOKEN')


HEADERS = {
    'Authorization': 'Bearer ' + anime_bearer_token
}


def get_genres() -> List:
    genres = []
    try: 
        data  = requests.get(anime_base_url + '/resources/1.0/0', headers=HEADERS)
    except Exception as e : 
        data = []
    else:
        genres = data.json()['data']
    return genres

def get_animes() -> List: 
    animes = []
    try:
        data = requests.get(anime_base_url + '/anime', headers=HEADERS)
    except Exception as e:
        data = []
    else: 
        animes = data.json()['data']
    return animes
    