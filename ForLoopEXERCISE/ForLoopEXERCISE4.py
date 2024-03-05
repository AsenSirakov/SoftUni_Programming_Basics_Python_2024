age = int(input())
price = float(input())
price_toy = int(input())
toy = 0
money = 0
for i in range (1, age+1):
    if i % 2 == 0:
        money += (i * 10/2) - 1
    else:
        toy += 1
money_toy = toy * price_toy
total = money + money_toy
if total >= price:
    remain = total - price
    print(f"Yes! {remain:.2f}")
else:
    need = price - total
    print(f"No! {need:.2f}")
