# 6810610037 โกมล บุญเรือง

amount = int(input("Enter number of classes: "))
high_average = 0
highest_class_name = ""

for i in range(1, amount + 1):
    i = input("Class name: ")
    times = 0
    _sum = 0
    while True:
        score = int(input("Enter score (-1 to stop): "))
        if score == -1:
            break
        _sum += score
        times += 1

    average = _sum / times

    if average > high_average:
        high_average = average
        highest_class_name = i

    print(f"{i} Average = {average:.2f}")
    print()

print(f"Highest average class: {highest_class_name} ({high_average:.2f})")
