# 6810610037 โกมล บุญเรือง
SERVICE_CHARGE = 24.62
UNIT_RATE = 0
RATE1 = 3.2484
RATE2 = 4.2218
RATE3 = 4.4217

keep_going = "y"
electric_cost = 0

while keep_going == "y":

    energy_unit = int(input("Enter the energy consumption (kilowatt-hours): "))

    while energy_unit < 0 or energy_unit > 1000:
        energy_unit = int(input("Enter the energy consumption (kilowatt-hours): "))

    if energy_unit == 0:
        electric_cost = 0
    elif energy_unit <= 150:
        electric_cost = energy_unit * RATE1
    elif energy_unit <= 400:
        electric_cost = (150 * RATE1) + (energy_unit - 150) * RATE2
    else:
        electric_cost = (150 * RATE1) + (250 * RATE2) + (energy_unit - 400) * RATE3

    VAT = (electric_cost + SERVICE_CHARGE) * 7 / 100
    total_cost = electric_cost + SERVICE_CHARGE + VAT

    print(f"Electricity cost = {electric_cost:,.2f} Baht")
    print(f"Service charge = {SERVICE_CHARGE} Baht")
    print(f"VAT (7 percent) = {VAT:,.2f} Baht")
    print(f"Total cost = {total_cost:,.2f} Baht")

    keep_going = ""

    while keep_going != "y" and keep_going != "n":
        keep_going = input("Do you want to continue? (y/n): ")

print("Goodbye!")
