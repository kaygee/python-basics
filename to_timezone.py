import datetime
import pytz

# Create a function named to_timezone that takes a timezone name as a string.
# Convert starter to that timezone using pytz's timezones and return the new datetime.
starter = pytz.utc.localize(datetime.datetime(2015, 10, 21, 23, 29))

def to_timezone(name):
    timezone = pytz.timezone(name)
    return starter.astimezone(timezone)

pacific = "US/Pacific"
print("To {} the time is {}".format(pacific, to_timezone(pacific)))
india = "Asia/Calcutta"
print("To {} the time is {}".format(india, to_timezone(india)))
