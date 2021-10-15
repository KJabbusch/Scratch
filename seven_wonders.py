import requests
import pprint
import time

path = "https://us1.locationiq.com/v1/search.php"

LOCATIONIQ_API_KEY = "pk.0ef7718df279c413529a016bf766a9f6"
search_terms = ["Great Wall of China", "Petra", "Colosseum", "Chichen Itza", "Machu Picchu", "Taj Mahal", "Christ the Redeemer"]

seven_wonders = {}

for search_term in search_terms:
    query_params = {
        "key": LOCATIONIQ_API_KEY,
        "q": search_term,
        "format": "json"
    }
    response = requests.get(path, params=query_params)
    response_body = response.json()
    coordinates = {}
    coordinates["latitude"] = response_body[0]['lat']
    coordinates["longitude"] = response_body[0]['lon']
    seven_wonders[search_term] = coordinates
    time.sleep(.25)

pprint.pprint(seven_wonders)



