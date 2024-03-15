target_profit = float(input())

total_income = 0

while True:
    cocktail_name = input()
    if cocktail_name == "Party!":
        break

    cocktail_quantity = int(input())
    cocktail_price = len(cocktail_name) * cocktail_quantity

    if cocktail_price % 2 != 0:
        cocktail_price *= 0.75

    total_income += cocktail_price

    if total_income >= target_profit:
        print("Target acquired.")
        break

if total_income < target_profit:
    needed_money = target_profit - total_income
    print(f"We need {needed_money:.2f} leva more.")
print(f"Club income - {total_income:.2f} leva.")
