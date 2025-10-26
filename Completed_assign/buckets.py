# 6810610037 โกมล บุญเรือง


list_90_to_100 = []
list_80_to_89 = []
list_70_to_79 = []
list_60_to_69 = []
list_below_60 = []

while True:
    score = int(input("Score (-1 to stop): "))
    if score == -1:
        break
    if score >= 90:
        list_90_to_100.append(score)
    elif score >= 80:
        list_80_to_89.append(score)
    elif score >= 70:
        list_70_to_79.append(score)
    elif score >= 60:
        list_60_to_69.append(score)
    else:
        list_below_60.append(score)

merge_list = (
    list_below_60 + list_60_to_69 + list_70_to_79 + list_80_to_89 + list_90_to_100
)
min_score = min(merge_list)
max_score = max(merge_list)
average = sum(merge_list) / len(merge_list)

print()
print("Buckets:")
print(f"90-100: {len(list_90_to_100)}")
print(f"80-89: {len(list_80_to_89)}")
print(f"70-79: {len(list_70_to_79)}")
print(f"60-69: {len(list_60_to_69)}")
print(f"<60: {len(list_below_60)}")
print()
print(f"Min={min_score},Max={max_score},Avg={average:.2f}")
