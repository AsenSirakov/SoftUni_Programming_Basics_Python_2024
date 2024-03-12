budget = float(input())
nights = int(input())
price_per_night = float(input())
percent_additional_cost = int(input())
percent_discount = 0
if nights > 7:
    price_per_night -= price_per_night * 0.05
total_nights = price_per_night * nights
percet_additional_cost_sum = budget * percent_additional_cost/100
total = total_nights + percet_additional_cost_sum
left_money = budget - total
needed_money = total - budget
if budget > total:
    print(f"Ivanovi will be left with {left_money:.2f} leva ater vacation.")
else:
    print(f"{needed_money:.2f} leva needed.")