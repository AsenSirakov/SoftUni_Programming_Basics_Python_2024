budget = int(input())
season = input()
number_fisherman = int(input())
total_sum = 0
left_money = 0
needed_money = 0

if season == 'Spring':
    total_sum = 3000
elif season == 'Summer' or season == 'Autumn':
    total_sum = 4200
elif season == 'Winter':
    total_sum = 2600

if 0 < number_fisherman <= 6:
    total_sum -= total_sum * 0.1
elif 7 <= number_fisherman <= 11:
    total_sum -= total_sum * 0.15
else:
    total_sum -= total_sum * 0.25

if number_fisherman % 2 == 0 and season != 'Autumn':
    total_sum -= total_sum * 0.05

if budget >= total_sum:
    left_money = budget - total_sum
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    needed_money = total_sum - budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")
