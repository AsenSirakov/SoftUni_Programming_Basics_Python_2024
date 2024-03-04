days = int(input())
where = input()
review = input()
price = 0
sleep = days - 1
if where == 'room for one person':
    price = 18
elif where == 'apartment':
    price = 25
elif where == 'president apartment':
    price = 35
total_price = sleep * price
if where == 'apartment':
    if sleep < 10:
        total_price -= total_price * 0.3
    elif 10 <= sleep <= 15:
        total_price -= total_price * 0.35
    else:
        total_price -= total_price * 0.5

if where == 'president apartment':
    if sleep < 10:
        total_price -= total_price * 0.1
    elif 10 <= sleep <= 15:
        total_price -= total_price * 0.15
    else:
        total_price -= total_price * 0.2

if review == 'positive':
    total_price += total_price * 0.25
elif review == 'negative':
    total_price -= total_price * 0.1

print(f"{total_price:.2f}")