import datetime

pacific = datetime.timezone(datetime.timedelta(hours =- 8))
europe = datetime.timezone(datetime.timedelta(hours =+ 1))

# naive doesn't know its timezone.
naive = datetime.datetime(2015, 10, 21, 4, 29)

# aware knows its timezone
hill_valley = datetime.datetime(2015, 10, 21, 4, 29, tzinfo=pacific)
paris = datetime.datetime(2015, 10, 21, 4, 29, tzinfo=europe)

paris = hill_valley.astimezone(europe)

print(naive)
print(hill_valley)
print(paris)
