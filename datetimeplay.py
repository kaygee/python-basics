import datetime

print(datetime.datetime.now())

time_now = datetime.datetime.now()
time_now_again = datetime.datetime.now()
time_elapsed = time_now_again - time_now
print(time_elapsed)
print("time days is {}".format(time_elapsed.days))

date = datetime.datetime.now()
print(date.replace(hour = 14, minute = 30))

datetime.datetime(2015, 9, 28, 15, 52)
datetime.timedelta(days = 3)

time_now + datetime.timedelta(days = 3)

datetime.timedelta(days = -5)

time_now + datetime.timedelta(days = -5)

time_now - datetime.timedelta(days = 5)

time_now - datetime.timedelta(minutes = 5)

print(time_now.date())
print(time_now.time())

def add_delta_to_now(delta):
    return delta + datetime.datetime.now()

print(add_delta_to_now(datetime.timedelta(days = 5)))

today = datetime.datetime.combine(datetime.date.today(), datetime.time())
print(today)
print("Today is {}".format(today))

print(today.month)
print(today.year)
print(today.hour)
print(today.minute)
print(today.weekday())
print("timestamp is {}".format(today.timestamp()))

time_1 = datetime.datetime.now()
time_2 = time_1 + datetime.timedelta(minutes = 6)

def minutes(time_1, time_2):
    print("{} - {}".format(time_2, time_1))
    return round((time_2 - time_1).seconds/60)

print("minutes rounded is {}".format(minutes(time_1, time_2)))

print(time_1.strftime('%B %d'))
print(time_1.strftime('%m/%d/%y'))

print(datetime.datetime.strptime('2015-05-05 12:00', '%Y-%m-%d %H:%M'))

def time_tango(date, time):
    return datetime.datetime.combine(date, time)

## Examples
# to_string(datetime_object) => "24 September 2012"
# from_string("09/24/12 18:30", "%m/%d/%y %H:%M") => datetime
def to_string(datetime):
  return datetime.strftime('%d %B %Y')

starter = datetime.datetime(2015, 10, 21, 16, 29)

def delorean(integer):
    return datetime.timedelta(hours = integer) + starter

print("into the future {}!".format(delorean(5)))

# Write a function named time_machine that takes an integer and a string of
# "minutes", "hours", "days", or "years". This describes a timedelta. Return a
# datetime that is the timedelta's duration from the starter datetime.

# Remember, you can't set "years" on a timedelta!
# Consider a year to be 365 days.

## Example
# time_machine(5, "minutes") => datetime(2015, 10, 21, 16, 34)
def time_machine(integer, interval):
    if interval.upper() == 'YEARS':
        return starter + datetime.timedelta(days = (365 * integer))
    elif interval.upper() == 'MINUTES':
        return starter + datetime.timedelta(minutes = integer)
    elif interval.upper() == 'DAYS':
        return starter + datetime.timedelta(days = integer)
    elif interval.upper() == 'HOURS':
        return starter + datetime.timedelta(hours = integer)

print(time_machine(5, "minutes"))

# Create a function named timestamp_oldest that takes any number of POSIX
# timestamp arguments. Return the oldest one as a datetime object.
# Remember, POSIX timestamps are floats and lists have a .sort() method.
#
# If you need help, look up datetime.datetime.fromtimestamp()
# Also, remember that you *will not* know how many timestamps
# are coming in.

timestamp_tuple = (1443493546.724789, 1443493546.724789, 1443493547.724789, 1443493548.724789)

def timestamp_oldest(timestamps):
    print(timestamps)
    timestamps_list = list(timestamps)
    print(timestamps_list)
    timestamps_list.sort()
    return datetime.datetime.fromtimestamp(timestamps_list[0])

print("Oldest timestamp is {}".format(timestamp_oldest(timestamp_tuple)))
