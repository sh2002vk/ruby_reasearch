# File to access the newsapi.org api
import os
import requests
import json
from api_list import api_urls

# API info
api_key = os.getenv("newsapiKey")
api_endpoint = api_urls["newsapi"]
q = "merge OR merger OR buyout OR acquisition"

# Data store info
path = "/Users/shubh/Desktop/Ruby/R & D/ruby_reasearch/risk_arbitrage/data_store/newsapi_store.json"

params = {
    "apiKey": api_key,
    "q": q,
    "language": "en",
    "page": 1
}

for i in range(1, 5):
    params["page"] = i
    request = requests.get(url=api_endpoint, params=params)
    data = request.json()
    for obj in data["articles"]:
        print(obj["title"])
        print()

# with open(path, 'w') as outfile:
#     json.dump(data, outfile)
