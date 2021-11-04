"""
Steam Game Reviews of FengXinLou
Game ID: 1126310
Created By Peng 2021/10/26
"""
import requests
from time import sleep
from urllib.parse import quote
import json


def get_game_reviews(gameID: str, output=False):
    """
    Get Game Reviews by Game ID.
    :param gameID: Steam Game ID.
    :param output: True -> return json; False -> write into json file (data.json).
    :return: None or json depends on param output.
    """
    cursor = '*'
    result = []
    while True:
        url = f'https://store.steampowered.com/appreviews/{gameID}?json=1&cursor={cursor}&filter=recent&num_per_page=100&review_type=all&language=schinese&purchase_type=all'
        res = requests.get(url).json()
        try:
            if cursor == quote(res['cursor']):
                break
            else:
                cursor = quote(res['cursor'])
        except Exception as e:
            print(e)
        for review in res['reviews']:
            result.append({'pub_date': review['timestamp_created'], 'content': review['review']})
        sleep(5)
    if output:
        return result
    else:
        with open('data.json', 'w') as f:
            json.dump(result, f)
        return None


# Get Reviews
# get_game_reviews('1126310')
