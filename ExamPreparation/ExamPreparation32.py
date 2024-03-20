baggage_price_over_20 = float(input())
baggage_weight = float(input())
days_until_travel = int(input())
number_of_bags = int(input())


if baggage_weight <= 10:
    baggage_price = baggage_price_over_20 * 0.2
elif 10 < baggage_weight <= 20:
    baggage_price = baggage_price_over_20 * 0.5
else:
    baggage_price = baggage_price_over_20


if days_until_travel > 30:
    baggage_price += baggage_price * 0.1
elif 7 <= days_until_travel <= 30:
    baggage_price += baggage_price * 0.15
else:
    baggage_price += baggage_price * 0.4

total_price = baggage_price * number_of_bags

print(f"The total price of bags is: {total_price:.2f} lv.")
