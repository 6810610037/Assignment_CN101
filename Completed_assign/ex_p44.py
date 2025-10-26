# 6810610037 โกมล บุญเรือง


def print_even(a_list):
    list_even = [num for num in a_list if num % 2 == 0]
    for num in list_even:
        print(num, end=" ")
    print()


def main():
    print_even([1, 2, 3, 4, 5])
    list_1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 20, 21, 20]
    list_2 = list(range(20, 0, -3))
    print_even(list_1)
    print_even(list_2)


main()
