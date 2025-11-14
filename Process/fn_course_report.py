# 6810610037 โกมล บุญเรือง
QUIZ_WEIGHT = 0.2
MIDTERM_WEIGHT = 0.3
FINAL_WEIGHT = 0.5


def calculate_final_scores(students):
    final_scores = []
    for student in students:
        name, quizzes, midterm, final = student
        if len(quizzes) == 0:
            quiz_avg = 0
        quiz_avg = sum(quizzes) / len(quizzes)
        final_score = (
            (quiz_avg * QUIZ_WEIGHT)
            + (midterm * MIDTERM_WEIGHT)
            + (final * FINAL_WEIGHT)
        )
        final_scores.append((name, final_score))
    return final_scores


def assign_letter_grades(final_scores):
    graded = []
    for name, score in final_scores:
        if score >= 80:
            grade = "A"
        elif score >= 70:
            grade = "B"
        elif score >= 60:
            grade = "C"
        elif score >= 50:
            grade = "D"
        else:
            grade = "F"
        graded.append((name, score, grade))
    return graded


def get_honors_students(graded_students, threshold=80):  ################
    honors = []
    for name, score, grade in graded_students:
        if score >= threshold:
            honors.append(name)
    return honors


def get_at_risk_students(graded_students, threshold=50):
    at_risk = []
    for name, score, grade in graded_students:
        if score < threshold:
            at_risk.append(name)
    return at_risk


def calculate_overall_statistics(graded_students):
    scores = []
    for name, score, grade in graded_students:
        scores.append(score)
        if len(scores) == 0:
            class_average = 0
    class_average = sum(scores) / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)
    return (class_average, highest_score, lowest_score)


def print_report(graded_students, honors_students, at_risk_students, stats):
    class_average, highest_score, lowest_score = stats
    print("Final scores and grades of each student:")
    for name, score, grade in graded_students:
        print(f"{name}: {score:.2f} ({grade})")
    print()
    print("Honors students (>= 80): ")
    print(honors_students)
    print()
    print("At-risk students (< 50): ")
    print(at_risk_students)
    print()
    print("Class statistics:")
    print(f"Average score: {class_average:.2f}")
    print(f"Highest score:  {highest_score:.2f}")
    print(f"Lowest score: {lowest_score:.2f}")


def main():
    students = []
    n = int(input("Enter number of students: "))
    for i in range(1, n + 1):
        name = input(f"Enter name of student #{i}: ")
        quizzes = [
            float(x)
            for x in input(
                f"Enter 3 quiz scores for {name} (separated by spaces): "
            ).split(" ")
        ]
        midterm = float(input(f"Enter midterm score for {name}: "))
        final = float(input(f"Enter final exam score for {name}: "))
        students.append((name, quizzes, midterm, final))
    print()
    final_scores = calculate_final_scores(students)
    graded_students = assign_letter_grades(final_scores)
    honors_students = get_honors_students(graded_students, 80)
    at_risk_students = get_at_risk_students(graded_students, 50)
    stats = calculate_overall_statistics(graded_students)
    print_report(graded_students, honors_students, at_risk_students, stats)


main()
