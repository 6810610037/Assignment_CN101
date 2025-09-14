# 6810610037 โกมล บุญเรือง

score = int(input("Enter a score (-1 to end): "))
_sum = 0
count = 0
max_num = score
min_num = score

if score == -1:
    print("No scores entered")
else:
    while score != -1:
        _sum += score
        count += 1

        if score > max_num:
            max_num = score
        if score < min_num:
            min_num = score

        score = int(input("Enter a score (-1 to end): "))
    average = _sum / count

    print(f"Average score: {average:.1f}")
    print(f"Minimum score: {min_num:.1f}")
    print(f"Maximum score: {max_num:.1f}")
