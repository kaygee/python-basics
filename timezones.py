improt datetime

pacific = datetime.timezone(datetime.timedelta(hours =- 8))
eastern = datetime.timezone(datetime.timedelta(hours =- 5))
naive = datetime.datetime(2015, 5, 5, 9)

aware = datetime.datetime(2015, 5, 5, 0, tzinfo=pacific)
