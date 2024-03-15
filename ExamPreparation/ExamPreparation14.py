city = input()
package = input()
is_vip = input()
days = int(input())

price_per_day = 0

if city in ["Bansko", "Borovets"]:
    if package == "noEquipment":
        price_per_day = 80
        if is_vip == "yes":
            price_per_day *= 0.95  # 5% VIP discount
    elif package == "withEquipment":
        price_per_day = 100
        if is_vip == "yes":
            price_per_day *= 0.90  # 10% VIP discount
    else:
        print("Invalid input!")
        exit()
elif city in ["Varna", "Burgas"]:
    if package == "withBreakfast":
        price_per_day = 130
        if is_vip == "yes":
            price_per_day *= 0.88  # 12% VIP discount
    elif package == "noBreakfast":
        price_per_day = 100
        if is_vip == "yes":
            price_per_day *= 0.93  # 7% VIP discount
    else:
        print("Invalid input!")
        exit()
else:
    print("Invalid input!")
    exit()

total_price = days * price_per_day

if days <= 0:
    print("Days must be a positive number!")
else:
    if days > 7:
        total_price -= price_per_day
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
