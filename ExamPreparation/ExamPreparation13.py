budget = float(input())
needed_litres = float(input())
day_of_the_week = input()
tour_guide = 100
price_per_litre = needed_litres * 2.10
total_with_tour = price_per_litre + tour_guide
if day_of_the_week == "Sunday":
    total_with_tour-= total_with_tour * 0.2
elif day_of_the_week == "Saturday":
    total_with_tour-= total_with_tour * 0.1
if budget > total_with_tour:
    remains = budget - total_with_tour
    print(f"Safari time! Money left: {remains:.2f} lv.")
else:
    needed_money = total_with_tour - budget
    print(f"Not enough money! Money needed:{needed_money:.2f} lv.")
