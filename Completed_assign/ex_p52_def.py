# 6810610037 โกมล บุญเรือง


def print_square(x, y):
    x_power_two = x**2
    y_power_two = y**2
    square = x_power_two + y_power_two
    print(f"{x**2} + {y**2} = {square}")


def main():
    print_square(3, 4)
    a, b = 7, 9
    print_square(a, b)


main()
