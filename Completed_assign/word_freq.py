# 6810610037 โกมล บุญเรือง

list1 = []
count_list = []
while True:
    word = input("Enter word (END to stop):")
    if word == "END":
        break
    if word not in list1:
        list1.append(word)
        count_list.append(1)
    for i in range(len(list1) - 1):
        if word == list1[i]:
            count_list[i] += 1
highest_frequency_index = count_list.index(max(count_list))

print(f"Words : {list1}")
print(f"Counts: {count_list}")
print(f"Most frequents: '{list1[highest_frequency_index]}' ({max(count_list)})")
