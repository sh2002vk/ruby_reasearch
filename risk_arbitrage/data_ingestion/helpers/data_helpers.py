import json
import os

# Data store info
path = os.getenv("datapath")


def openOldData() -> dict:
    """Pulls in old data from data store -> to be updated"""

    try:
        with open(path) as f:
            merger_headlines = json.load(f)
        return merger_headlines
    except Exception as e:
        print(f'''DATA LOAD FAILED: {e}''')
        return {}
