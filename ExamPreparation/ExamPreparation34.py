
budget = float(input())
num_series = int(input())


total_cost = 0


discounts = {
    "Thrones": 0.5,
    "Lucifer": 0.4,
    "Protector": 0.3,
    "TotalDrama": 0.2,
    "Area": 0.1
}


for _ in range(num_series):
    series_name = input()
    series_price = float(input())

    if series_name in discounts:
        series_price *= (1 - discounts[series_name])

    total_cost += series_price


if budget >= total_cost:
    left_money = budget - total_cost
    print(f"You bought all the series and left with {left_money:.2f} lv.")
else:
    needed_money = total_cost - budget
    print(f"You need {needed_money:.2f} lv. more to buy the series!")
