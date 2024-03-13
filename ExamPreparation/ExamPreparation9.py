tournament_stage = input()
ticket_type = input()
number_tickets = int(input())
photo = input()
price = 0
photo_price = 40
if tournament_stage == "Quarter final":
    if ticket_type == "Standard":
        price = 55.50
    elif ticket_type == "Premium":
        price = 105.20
    elif ticket_type == "VIP":
        price = 118.90
if tournament_stage == "Semi final":
    if ticket_type == "Standard":
        price = 75.88
    elif ticket_type == "Premium":
        price = 125.22
    elif ticket_type == "VIP":
        price = 300.40
if tournament_stage == "Final":
    if ticket_type == "Standard":
        price = 110.10
    elif ticket_type == "Premium":
        price = 160.66
    elif ticket_type == "VIP":
        price = 400
sum_price = number_tickets * price
if sum_price > 4000:
    sum_price -= sum_price * 0.25
elif 2500 < sum_price <= 4000:
    sum_price -= sum_price * 0.1
if photo == "Y":
    sum_price+= number_tickets * photo_price

print(f"{sum_price:.2f}")
