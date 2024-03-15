import math

number_of_people = int(input())
entry_fee = float(input())
price_per_seat = float(input())
price_per_umbrella = float(input())
people_who_want_seat = math.ceil(number_of_people * 0.75)
people_who_use_umbrella = math.ceil(number_of_people * 0.5)
total_seat = people_who_want_seat * price_per_seat
total_umbrella = people_who_use_umbrella * price_per_umbrella
total_fee = number_of_people * entry_fee
sum_all = total_fee + total_seat + total_umbrella
print(f"{sum_all:.2f} lv.")
