import os
import requests
import json
from api_list import api_urls
from helpers.general_helpers import convertDates

# API Info
api_key = os.getenv("mediaStackKey")
path = os.getenv("datapath")
api_endpoint = api_urls["mediastack"]
keywords = "merger"
params = {
    "access_key": api_key,
    "keywords": keywords,
    "countries": "us",
    "limit": 100,
    "offset": 0
}


def getMediaStack(previous_data: dict) -> (bool, int):
    total = 101  # temp var for pagination

    print(f'''Current length of data: {len(previous_data)}''')
    count = 0

    while params["offset"] < total:
        count += 1
        request = requests.get(url=api_endpoint, params=params)
        data = request.json()
        try:
            for obj in data["data"]:
                if obj["title"] not in previous_data:
                    previous_data[obj["title"]] = {
                        "source": obj["source"],
                        "published_at": convertDates(obj["published_at"][0:-6], type="%Y-%m-%dT%H:%M:%S"),
                        "api": "MEDIASTACK"
                    }
            params["offset"] = params["offset"] + data["pagination"]["limit"]
            total = data["pagination"]["total"]
        except Exception as e:
            total = 0
            print(e)

    print(f'''Updated length of data from mstack is: {len(previous_data)}''')

    try:
        with open(path, 'w') as outfile:
            json.dump(previous_data, outfile)
    except Exception as e:
        print(f'''DATA UPDATE FAILED: {e}''')
        return False, count

    return True, count
