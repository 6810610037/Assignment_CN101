# 6810610037 โกมล บุญเรือง

days = int(input("Input number of days: "))
amount_time_slot = int(input("Input number of time slots per day: "))
most_car_day = 0
count = 0
sum_amount = 0
sum_amount_cars_week = 0
count_week = 0
most_car_week = 0
day_most_car = 0

for initial in range(1, days + 1):

    print(f"Day {initial}")
    print("-" * 10)

    for order in range(1, amount_time_slot + 1):
        amount_cars = int(input(f"Time slot no.{order}: "))
        sum_amount += amount_cars
        sum_amount_cars_week += amount_cars
        count += 1
        if amount_cars > most_car_day:
            most_car_day = amount_cars
        if most_car_week < most_car_day:
            most_car_week = most_car_day
            day_most_car = initial

    average_quantity = sum_amount / count
    count_week += count
    sum_amount = 0
    count = 0

    print(f"Average cars in this day: {average_quantity:.2f}")
    print(f"Most cars in this day: {most_car_day}")
    print()

average_quantity_week = sum_amount_cars_week / count_week

print(f"Average cars per week: {average_quantity_week:.2f}")
print(f"Day {day_most_car} had the most cars: {most_car_week}")
