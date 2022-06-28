from helpers.data_helpers import openOldData
from newsapi import update_data
from mediastack import getMediaStack
from newscatcher import getNewsCatcher


def update_newsapi(on=True) -> (bool, int):
    try:
        if on:
            data = openOldData()
            return update_data(previous_data=data)
        else:
            return False, 0
    except Exception as e:
        print(f'''FATAL ERROR IN NEWSAPI: {e}''')


def update_mediastack(on=True) -> (bool, int):
    try:
        if on:
            data = openOldData()
            return getMediaStack(previous_data=data)
        else:
            return False, 0
    except Exception as e:
        print(f'''FATAL ERROR IN MEDIASTACK: {e}''')


def update_newscatcher(on=True) -> (bool, int):
    """UNSTABLE API -> Only call when necessary"""

    try:
        if on:
            data = openOldData()
            return getNewsCatcher(previous_data=data)
        else:
            return False, 0
    except Exception as e:
        print(f'''FATAL ERROR IN NEWSCATCHER: {e}''')


newsapi, newscount = update_newsapi()
mediastack, mediacount = update_mediastack()
newscatcher, catchcount = update_newscatcher()
print("\n\n -----FINAL DATA SATUS-----")
print(f'''NewsAPI status: {newsapi} || Count: {newscount}''')
print(f'''MediaStack status: {mediastack} || Count: {mediacount}''')
print(f'''NewsCatcher status: {newscatcher} || Count: {catchcount}''')
