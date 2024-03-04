month = input()
number_nights = int(input())

price_apartment = 0
price_studio = 0

if month == 'May' or month == 'October':
    price_studio = 50
    price_apartment = 65
elif month == 'June' or month == 'September':
    price_studio = 75.20
    price_apartment = 68.70
elif month == 'July' or month == 'August':
    price_studio = 76
    price_apartment = 77

if month in ['May', 'October']:
    if number_nights > 14:
        price_studio -= price_studio * 0.3
    elif number_nights > 7:
        price_studio -= price_studio * 0.05
elif month in ['June', 'September'] and number_nights > 14:
    price_studio -= price_studio * 0.2

if number_nights > 14:
    price_apartment -= price_apartment * 0.1

total_apartment = price_apartment * number_nights
total_studio = price_studio * number_nights

print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")
