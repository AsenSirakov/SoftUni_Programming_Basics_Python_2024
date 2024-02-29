budget = float(input())
videocard_number = int(input())
processor_number = int(input())
ram_number = int(input())
videocard_price = 250
videocard_all = videocard_number * videocard_price
processor_price = 0.35 * videocard_all
ram_price = 0.1 * videocard_all
processor_all = processor_price * processor_number
ram_all = ram_price * ram_number
sumall = videocard_all + processor_all + ram_all
if videocard_number > processor_number:
    sumall -= 0.15 * sumall

if budget >= sumall:
    remaining_money = budget - sumall
    print(f"You have {remaining_money:.2f} leva left!")
else:
    needed_money = sumall - budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")

