drink = input()
sugar = input()
number_of_drinks = int(input())
price = 0
if drink == "Espresso":
    if sugar == "Without":
        price = (0.90) - (0.90 * 0.35)
    elif sugar == "Normal":
        price = 1
    elif sugar == "Extra":
        price = 1.20
if drink == "Cappuccino":
    if sugar == "Without":
        price = 1 - (1 * 0.35)
    elif sugar == "Normal":
        price = 1.20
    elif sugar == "Extra":
        price = 1.60
if drink == "Tea":
    if sugar == "Without":
        price = (0.50) - (0.50 * 0.35)
    elif sugar == "Normal":
        price = 0.60
    elif sugar == "Extra":
        price = 0.70
if drink == "Espresso" and number_of_drinks >= 5:
    price -= price * 0.25
total = number_of_drinks * price
if total > 15:
    total -= total * 0.20

print(f"You bought {number_of_drinks} cups of {drink} for {total:.2f} lv.")