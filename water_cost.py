amount = int(input("Enter the number of liters consumed: "))
rate_per_liter = float(input("Enter the rate per liter: "))
if amount > 500:
    extra_cost = (amount - 500) * (rate_per_liter * 1.2)
    base_cost = 500 * rate_per_liter
    total_cost = base_cost + extra_cost
else:
    total_cost = amount * rate_per_liter
print(f"The total water cost is ${total_cost:.2f}")
