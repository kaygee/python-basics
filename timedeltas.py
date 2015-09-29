import datetime
import pytz

pacific = pytz.timezone("US/Pacific")
eastern = pytz.timezone("US/Eastern")

fmt = '%Y-%m-%d %H:%M:%S %Z%z'
utc = pytz.utc

# localize works with naive dates
start = pacific.localize(datetime.datetime(2015, 5, 5, 9))
print("localized with pytz {}".format(start))

print(start.strftime(fmt))

# astimezone works with aware dates
start_eastern = start.astimezone(eastern)
print("start timezone as eastern time {}".format(start_eastern))

auckland = pytz.timezone("Pacific/Auckland")
mumbai = pytz.timezone("Asia/Calcutta")

apollo_13_native = datetime.datetime(1970, 4, 11, 14, 13)
print(apollo_13_native)
apollo_13_eastern = eastern.localize(apollo_13_native)
print(apollo_13_eastern)
apollo_13_utc = apollo_13_eastern.astimezone(utc)
print(apollo_13_utc)
print("apollo 13 launch from utc as in pacific timezone {}".format(apollo_13_utc.astimezone(pacific).strftime(fmt)))

print(pytz.all_timezones)
print(pytz.country_timezones['us'])

# starter is a naive datetime. Use pytz to make it a "US/Pacific" datetime
# instead and assign this converted datetime to the variable local.
fmt = '%m-%d %H:%M %Z%z'
starter = datetime.datetime(2015, 10, 21, 4, 29)

local = pytz.timezone("US/Pacific").localize(starter)
print(local)

# Now create a variable named pytz_string by using strftime with the local
# datetime. Use the fmt string for the formatting.
pytz_string = local.strftime(fmt)

# Create a function named to_timezone that takes a timezone name as a string.
# Convert starter to that timezone using pytz's timezones and return the new datetime.
localized_convert = pytz.utc.localize(datetime.datetime(2015, 10, 21, 23, 29))

def to_timezone(name):
  return pytz.timezone(name).localize(localized_convert)

print(to_timezone("US/Pacific"))
print(to_timezone("Asia/Calcutta"))
