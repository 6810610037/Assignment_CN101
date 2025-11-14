# 6810610037 โกมล บุญเรือง


def calculate_averages(students):
    averages = []
    for data in students:
        name, math_score, science_score = data[0], data[1], data[2]
        average = (math_score + science_score) / 2
        averages.append((name, average))
    return averages


def get_students_above_threshold(averages, threshold=75):
    above_threshold = []
    for name, average in averages:
        if average > threshold:
            above_threshold.append(name)
    return above_threshold


def get_highest_average_student(averages):
    highest_student = None
    highest_score = -1
    for name, averages in averages:
        if averages > highest_score:
            highest_score = averages
            highest_student = name
    return (highest_student, highest_score)


def print_report(averages, above_threshold, highest):
    highest_name = highest[0]
    highest_score = highest[1]
    for name, average in averages:
        print(f"{name} : {average:.2f}")
    print()
    print(f"Students with an average score above 75: {above_threshold}")
    print()
    print(f"Student with the highest average score: {highest[0]} : {highest[1]:.2f}")


def main():
    students = [
        ("Alice", 85, 90),
        ("Bob", 78, 82),
        ("Charlie", 92, 93),
        ("David", 65, 70),
        ("Eve", 88, 85),
    ]
    averages = calculate_averages(students)
    above_threshold = get_students_above_threshold(averages, 75)
    highest = get_highest_average_student(averages)
    print_report(averages, above_threshold, highest)


main()
