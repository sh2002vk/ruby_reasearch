# File to access the newsapi.org api
import os
import requests
import json
from api_list import api_urls
from datetime import datetime


def convertDates(date: str):
    epoch = datetime(1970, 1, 1)
    creation_epoch = 0

    try:
        creation_epoch = (datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ") - epoch).total_seconds()
    except Exception as e:
        print(e)

    return creation_epoch


# API info
api_key = os.getenv("newsapiKey")
api_endpoint = api_urls["newsapi"]
q = "merger"  # Keywords the api is looking for
params = {
    "apiKey": api_key,
    "q": q,
    "language": "en",
    "page": 1
}


# Data store info
path = "/Users/shubh/Desktop/Ruby/R & D/ruby_reasearch/risk_arbitrage/data_store/newsapi_store.json"
merger_headlines = {}
with open(path) as f:
  merger_headlines = json.load(f)


# Func body
more = True
count = params["page"]
while more:
    params["page"] = count
    request = requests.get(url=api_endpoint, params=params)
    data = request.json()
    try:
        count += 1
        for obj in data["articles"]:
            if obj["title"] not in merger_headlines:
                merger_headlines[obj["title"]] = {
                    "source": obj["source"]["name"],
                    "published_at": convertDates(obj["publishedAt"])
                }
    except Exception as e:
        more = False
        print(e)


with open(path, 'w') as outfile:
    json.dump(merger_headlines, outfile)
