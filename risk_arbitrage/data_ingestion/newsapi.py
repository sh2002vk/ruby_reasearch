# File to access the newsapi.org api
import os
import requests
import json
from api_list import api_urls
from helpers.general_helpers import convertDates

# API info
api_key = os.getenv("newsapiKey")
path = os.getenv("datapath")
api_endpoint = api_urls["newsapi"]
keywords = "merger"  # Keywords the api is looking for
params = {
    "apiKey": api_key,
    "q": keywords,
    "language": "en",
    "page": 1
}


def update_data(previous_data: dict) -> (bool, int):
    """
        Updates current data store with information from newapi.org

    :param previous_data:
    :return:
    """

    print(f'''Current length of data: {len(previous_data)}''')
    more = True
    count = 0
    while more:
        count += 1
        params["page"] = count
        request = requests.get(url=api_endpoint, params=params)
        data = request.json()
        try:
            count += 1
            for obj in data["articles"]:
                if obj["title"] not in previous_data:
                    previous_data[obj["title"]] = {
                        "source": obj["source"]["name"],
                        "published_at": convertDates(obj["publishedAt"], type="%Y-%m-%dT%H:%M:%SZ"),
                        "api": "NEWSAPI"
                    }
        except Exception as e:
            more = False
            print(f'''ERROR in N.A. conversion: {e}''')

    print(f'''Updated length of data from na is: {len(previous_data)}''')

    try:
        with open(path, 'w') as outfile:
            json.dump(previous_data, outfile)
    except Exception as e:
        print(f'''DATA UPDATE FAILED: {e}''')
        return False, count

    return True, count
