import os
import requests
import json
from api_list import api_urls
from helpers.general_helpers import convertDates

# API Info
api_key = os.getenv("newsCatcherKey")
path = os.getenv("datapath")
api_endpoint = api_urls["newscatcher"]
keywords = "merger AND acquisition"
params = {
    "q": keywords,
    "lang": "en",
    "countries": "US",
    "topic": "business",
    "not_sources": "tmz.com",
    "sort_by": "rank",
    "page_size": 100,
    "page": 1
}
headers = {
    "x-api-key": api_key
}


def getNewsCatcher(previous_data: dict):

    print(f'''Current length of data: {len(previous_data)}''')
    count = 1
    data = []
    request = requests.get(url=api_endpoint, params=params, headers=headers)
    apiData = request.json()
    data.extend(apiData["articles"])
    isNext = True if apiData["total_hits"] > 100 else False
    continuation = True

    while isNext:
        count += 1
        params["page"] += 1
        request = requests.get(url=api_endpoint, params=params, headers=headers)
        new_data = request.json()
        try:
            data.extend(new_data["articles"])
            isNext = True if new_data["total_hits"] > params["page"]*params["page_size"] else False
        except Exception as e:
            print(f'''Error encountered: {e}''')
            print(f'''API return error: {new_data}''')
            break
            continuation = False

    if continuation:  # If no API error encountered

        for obj in data:
            if obj["title"] not in previous_data:
                try:
                    previous_data[obj["title"]] = {
                        "source": obj["clean_url"],
                        "published_at": convertDates(obj["published_date"], type="%Y-%m-%d %H:%M:%S"),
                        "api": "NEWSCATCHER"
                    }
                except Exception as e:
                    print(f'''Date conversion error: {e}''')
                    print(obj)
                    continuation = False
                    break

        print(f'''Updated length of data from newscatcher is: {len(previous_data)}''')

        try:
            with open(path, 'w') as outfile:
                if continuation:
                    json.dump(previous_data, outfile)
                else:
                    raise Exception
        except Exception as e:
            print(f'''DATA UPDATE FAILED: {e}''')
            return False, count

        return True, count
    return False, 0
