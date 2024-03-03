budget = float(input())
season = input()
where = ''
price = 0
accommodation = ''
if budget <= 100 :
    where = 'Bulgaria'
elif budget <= 1000:
    where = 'Balkans'
else:
    where = 'Europe'

if season == 'summer':
    accommodation = 'Camp'
elif season == 'winter':
    accommodation = 'Hotel'
if where == 'Bulgaria':
    if season == 'summer':
        price = budget * 0.3
    elif season == 'winter':
        price = budget * 0.7
if where == 'Balkans':
    if season == 'summer':
        price = budget * 0.4
    elif season == 'winter':
        price = budget * 0.8
if where == 'Europe':
    accommodation = 'Hotel'
    if season == 'summer':
        price = budget * 0.9
    elif season == 'winter':
        price = budget * 0.9

print(f"Somewhere in {where}")
print(f"{accommodation} - {price:.2f}")