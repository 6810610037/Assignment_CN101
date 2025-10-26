# 6810610037
amount = int(input("ป้อนจำนวนน้ำที่ต้องการดื่ม (ml): "))
price = 0
if amount <= 150:
    price = 5
    amount = 150
elif amount <= 250:
    price = 7
    amount = 250
elif amount <= 500:
    price = 10
    amount = 500
elif amount <= 1000:
    price = 20
    amount = 1000
else:
    price = 35
    amount = 2000


print(f"แนะนำให้ซื้อขวดน้ำขนาด {amount} ml")
print(f"รวมเป็นเงิน: {price} บาท")
