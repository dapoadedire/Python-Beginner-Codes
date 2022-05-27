import datetime
print("Welcome to Date Difference Calculator")
today_date = datetime.date.today()
print(f"Today's date is {today_date}")

year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
someday = datetime.date(year, month, day)
print(f"Another date is {someday}")

difference = someday - today_date
print(f'Thw difference between these days is {difference}days')