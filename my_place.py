import requests
import json

path = "https://us1.locationiq.com/v1/search.php"

LOCATIONIQ_API_KEY = "pk.0ef7718df279c413529a016bf766a9f6"
search_term = "Space Needle, Seattle, WA, US"
query_params = {
    "key": LOCATIONIQ_API_KEY,
    "q": search_term,
    "format": "json"
}

response = requests.get(path, params=query_params)

response_body = response.json()
print("The value of response.json():", json.dumps(response_body, indent=1), "\n")
print(f"The lat and lon of {search_term} is {response_body[0]['lat']}, {response_body[0]['lon']}.")
print(f"The display name of {search_term} is  {response_body[0]['display_name']}.")
print(f"{search_term} is a {response_body[0]['type']} {response_body[0]['class']}.")
