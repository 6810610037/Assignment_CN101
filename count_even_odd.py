# 6810610037 โกมล บุญเรือง


even_num = 0
odd_num = 0
confirm = "y"

while confirm == "y":
    num = int(input("Enter a positive integer: "))
    if num % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
    confirm = ""
    while confirm != "y" and confirm != "n":
        confirm = input("Do you want to continue? (y/n): ")

print(f"Even number: {even_num}")
print(f"Odd number: {odd_num}")
