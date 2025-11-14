# 6810610037 โกมล บุญเรือง


def calculate_section_average(section_scores):
    section_averages = []
    for section_name, scores in section_scores:
        if len(scores) == 0:
            return 0
        average = sum(scores) / len(scores)
        section_averages.append((section_name, average))
    return section_averages


def print_section_scores(section_scores):
    print("Section Scores: ")
    for section_name, scores in section_scores:
        print(f"{section_name}: {scores}")


def print_section_averages(section_averages):
    print("Section Averages: ")
    for section_name, average in section_averages:
        print(f"{section_name}: {average:.2f}")


def find_max_score(section_scores):
    max_score = -1
    for section_name, scores in section_scores:
        for score in scores:
            if score > max_score:
                max_score = score
    return max_score


def main():
    section_scores = []
    amount_sections = int(input("Enter the number of sections: "))
    for _ in range(amount_sections):
        section_name = input("Enter section section_name: ")
        scores = []
        while True:
            score = float(input(f"Enter score for {section_name} (or -1 to finish): "))
            if score == -1:
                break
            scores.append(score)
        section_scores.append((section_name, scores))
    print()
    print_section_scores(section_scores)
    print()
    section_averages = calculate_section_average(section_scores)
    print_section_averages(section_averages)
    print()
    max_score = find_max_score(section_scores)
    print(f"Maximum score across all sections: {max_score:.2f}")


main()
