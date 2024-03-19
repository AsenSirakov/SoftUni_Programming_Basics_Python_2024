drink = input()
sugar = input()
quantity = int(input())

drink_prices = {
    "Espresso": {"Without": 0.90, "Normal": 1.00, "Extra": 1.20},
    "Cappuccino": {"Without": 1.00, "Normal": 1.20, "Extra": 1.60},
    "Tea": {"Without": 0.50, "Normal": 0.60, "Extra": 0.70}
}

drink_price = drink_prices[drink][sugar]
total_price = quantity * drink_price

if sugar == "Without":
    total_price *= 0.65
    if drink == "Espresso" and quantity >= 5:
        total_price *= 0.75

if total_price > 15:
    total_price *= 0.80

print(f"You bought {quantity} cups of {drink} for {total_price:.2f} lv.")
