flower = input()
number = int(input())
budget = int(input())

rose_price = 5.00
dahlias_price = 3.80
tulip_price = 2.80
narcissus_price = 3.00
gladiolus_price = 2.50

total_sum = 0

if flower == 'Roses':
    total_sum = rose_price * number
    if number > 80:
        total_sum -= total_sum * 0.10
elif flower == 'Dahlias':
    total_sum = dahlias_price * number
    if number > 90:
        total_sum -= total_sum * 0.15
elif flower == 'Tulips':
    total_sum = tulip_price * number
    if number > 80:
        total_sum -= total_sum * 0.15
elif flower == 'Narcissus':
    total_sum = narcissus_price * number
    if number < 120:
        total_sum += total_sum * 0.15
elif flower == 'Gladiolus':
    total_sum = gladiolus_price * number
    if number < 80:
        total_sum += total_sum * 0.20

if budget >= total_sum:
    left_sum = budget - total_sum
    print(f"Hey, you have a great garden with {number} {flower} and {left_sum:.2f} leva left.")
else:
    needed_sum = total_sum - budget
    print(f"Not enough money, you need {needed_sum:.2f} leva more.")
