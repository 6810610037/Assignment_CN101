# 6810610037 โกมล บุญเรือง
list1 = []
unique_list = []
unique_count = 0
normal_count = 0
while True:
    word = input("Enter word (END to stop):")
    if word == "END":
        break
    normal_count += 1
    if word not in list1:
        list1.append(word)
        unique_count += 1


print(f"Before: {normal_count} items")
print(f"After: {unique_count} items")
print(f"Uniquew: {list1}")
