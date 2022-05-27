from datetime import datetime
import pytz


first_timezone = input("Enter a time zone(Continent/Capital): ")
tz_user_input = pytz.timezone(first_timezone)
datetime_user_input: datetime = datetime.now(tz_user_input)
print(f"{first_timezone}:", datetime_user_input.strftime("%H:%M:%S"))

second_timezone = input("Enter a time zone(Continent/Capital): ")
tz_second_user_input = pytz.timezone(second_timezone)
datetime_second_user_input = datetime.now(tz_second_user_input)
print(f"{second_timezone}:", datetime_second_user_input.strftime("%H:%M:%S"))

# difference = datetime_second_user_input - datetime_user_input
# print(f"The difference between the two time zones: {difference}")

time_diff_hour = abs(datetime_second_user_input.hour - datetime_user_input.hour)
time_diff_minute = abs(datetime_second_user_input.minute - datetime_user_input.minute)
time_diff_second = abs(datetime_second_user_input.second - datetime_user_input.second)
print(f"The time difference is {time_diff_hour} hours,{time_diff_minute} minute(s),{time_diff_second} second(s) ")