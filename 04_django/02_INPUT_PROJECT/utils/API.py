from decouple import config
import requests

def send_naver(name, menu):
    naver_client_id = config('NAVER_CLIENT_ID')
    naver_client_secret = config('NAVER_CLIENT_SECRET')

    BASE_URL = 'https://openapi.naver.com/v1/search/local.json'
    headers = {
        'X-Naver-Client-Id': naver_client_id,
        'X-Naver-Client-Secret': naver_client_secret,
    }

    URL = BASE_URL + '?query=' + name + menu + '맛집'

    response = requests.get(URL, headers=headers)
    title = response.json().get('items')[0].get('title')
    link = response.json().get('items')[0].get('link')
    address = response.json().get('items')[0].get('address')
    telephone = response.json().get('items')[0].get('telephone')

    return{
        'title': title,
        'link': link,
        'address': address,
        'telephone': telephone,
    }
