from helpers.data_helpers import openOldData
from newsapi import update_data
from mediastack import getMediaStack


def update_newsapi() -> (bool, int):
    data = openOldData()
    return update_data(previous_data=data)


def update_mediastack() -> (bool, int):
    data = openOldData()
    return getMediaStack(previous_data=data)


newsapi, ncount = update_newsapi()
mediastack, mcount = update_mediastack()
print("\n\n -----FINAL DATA SATUS-----")
print(f'''NewsAPI status: {newsapi} || Count: {ncount}''')
print(f'''MediaStack status: {mediastack} || Count: {mcount}''')
