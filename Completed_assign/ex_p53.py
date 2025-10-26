# 6810610037 โกมล บุญเรือง


def print_less(x, a_list):
    for num in a_list:
        if x > num:
            print(num, end=" ")
    print()


def main():
    print_less(50, [50, 51, 99, 79, 47, 83, 90, 39, 90, 25])
    a, list_1 = 55, list(range(30, 100, 15))
    print_less(a, list_1)


main()
