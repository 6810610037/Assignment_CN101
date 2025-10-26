# 6810610037 โกมล บุญเรือง


def print_digit(a_string):
    list_digit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for letter in a_string:
        for digit in list_digit:
            if letter == str(digit):
                print(digit, end=" ")
    print()


def main():
    print_digit("24 hours in 1 day, 7 days in a 1 week. ")
    message = "I met a man with 7 wives. Each wife had 7 sacks."
    print_digit(message)


main()
