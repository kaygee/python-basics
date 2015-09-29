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

print(today.month)
print(today.year)
print(today.hour)
print(today.minute)
print(today.weekday())
print(today.timestamp())

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
