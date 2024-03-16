budget = float(input())
destination = input()
season = input()
days = int(input())
price = 0
if destination == "Dubai":
    if season == "Winter":
        price = 45000
    elif season == "Summer":
        price = 40000
if destination == "Sofia":
    if season == "Winter":
        price = 17000
    elif season == "Summer":
        price = 12500
if destination == "London":
    if season == "Winter":
        price = 24000
    elif season == "Summer":
        price = 20250
total_price = days * price
if destination == "Dubai":
    total_price -= total_price * 0.3
if destination == "Sofia":
    total_price += total_price * 0.25
if budget > total_price:
    remaining_money = budget - total_price
    print(f"The budget for the movie is enough! We have {remaining_money:.2f} leva left!")
else:
    needed_money = abs(budget - total_price)
    print(f"The director needs {needed_money:.2f} leva more!")
