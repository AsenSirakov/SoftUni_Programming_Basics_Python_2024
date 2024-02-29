budget = float(input())
decor = budget * 0.1
statists = int(input())
pricesuit = float(input())
totalsuit = statists * pricesuit
if statists > 150:
    totalsuit -= 0.1 * totalsuit

totalprice = decor + totalsuit

if totalprice > budget:
    neededmoney = totalprice - budget
    print('Not enough money!')
    print(f'Wingard needs {neededmoney:.2f} leva more.')
else:
    remainingmoney = budget - totalprice
    print('Action!')
    print(f'Wingard starts filming with {remainingmoney:.2f} leva left.')

