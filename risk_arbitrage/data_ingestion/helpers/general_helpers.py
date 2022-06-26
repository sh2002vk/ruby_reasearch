from datetime import datetime


def convertDates(date: str, type: str) -> float:
    epoch = datetime(1970, 1, 1)
    creation_epoch = 0

    try:
        creation_epoch = (datetime.strptime(date, type) - epoch).total_seconds()
    except Exception as e:
        print(e)

    return creation_epoch
