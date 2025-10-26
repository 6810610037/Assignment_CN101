# 6810610037
number = int(input("Enter number of minutes: "))
DAYS = number // 1440
HOURS = (number % 1440) // 60
MINUTES = number % 1440 % 60

print(f"{DAYS} day(s), {HOURS}hour(s), {MINUTES} minute(s)")
