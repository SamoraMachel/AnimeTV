from dotenv import load_dotenv
import requests
import beyonic  
import os

load_dotenv()

anime_base_url = os.getenv('BASE_URL')
anime_bearer_token = os.getenv('BEARER_TOKEN')
beyonic_bearer_token = os.getenv('BEYONIC_KEY')
website_url = os.getenv('WEBSITE_URL')


HEADERS = {
    'Authorization': 'Bearer ' + anime_bearer_token
}

ALL_ANIMES = {}
ALL_GENRES = {}


def get_genres() -> dict:
    if ALL_GENRES == {}:
        try: 
            data  = requests.get(anime_base_url + '/resources/1.0/0', headers=HEADERS)
        except Exception as e : 
            data = []
        else:
            ALL_GENRES.update(data.json()['data'])
    return ALL_GENRES

def get_animes() -> dict: 
    if ALL_ANIMES == {}:
        try:
            data = requests.get(anime_base_url + '/anime', headers=HEADERS)
        except Exception as e:
            data = []
        else: 
            ALL_ANIMES.update(data.json()['data'])
    return ALL_ANIMES
    
def get_specific_anime(id : int) -> dict:
    anime = {}
    try: 
        data = requests.get(anime_base_url + '/anime/' + str(id), headers=HEADERS)
    except Exception as e:
        data = []
        print(e)
    else: 
        anime = data.json()['data']
    return anime
        
def make_subscription(data : dict):
    first_name = data['first_name']
    last_name = data['last_name']
    phone_number = data['phone_number']
    amount = data['amount']
    currency = data['currency']
    callback = website_url
    
    payment = beyonic.Payment.create(
        phonenumber = phone_number,
        first_name = first_name,
        last_name = last_name, 
        amount = amount,
        currency = currency,
        callback_url = callback
    )
    
def transaction():
    transactions = beyonic.Transaction.list()
    return transactions

def currencies():
    return beyonic.Currency.list()