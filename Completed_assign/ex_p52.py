# โกมล บุญเรือง
amount_package = int(input("Number of packages purchased: "))
PACKAGES_PRICE = 99
discount_price = 0
normal_price = amount_package * PACKAGES_PRICE
if amount_package >= 10 and amount_package <= 19:
    discount_price = normal_price * 10 / 100
elif amount_package >= 20 and amount_package <= 49:
    discount_price = normal_price * 20 / 100
elif amount_package >= 50 and amount_package <= 99:
    discount_price = normal_price * 30 / 100
elif amount_package >= 100:
    discount_price = normal_price * 40 / 100
else:
    discount_price = 0
total_cost = normal_price - discount_price
print(f"Normal amount: {normal_price:,.2f} Baht")
print(f"Discount amount: {discount_price:,.2f} Baht")
print(f"Total amount: {total_cost:,.2f} Baht")
