# 6810610037
price = float(input("Enter normal price: "))
discount_percent = float(input("Enter percent discount: "))
discounted_price = price - (price * discount_percent / 100)
print(f"Normal price: {price:,.2f}")
print(f"Percent discount: {discount_percent:.2f}%")
print(f"Discounted price: {discounted_price:,.2f}")
