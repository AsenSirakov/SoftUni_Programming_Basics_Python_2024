name = input()
number_of_adult_tickets = int(input())
number_of_child_tickets = int(input())
net_price_of_adult_ticket = float(input())
service_tax = float(input())
net_price_of_child_tickets = net_price_of_adult_ticket - (net_price_of_adult_ticket * 0.7)
price_adult = (net_price_of_adult_ticket + service_tax) * number_of_adult_tickets
price_child = (net_price_of_child_tickets + service_tax) * number_of_child_tickets
total = price_child + price_adult
winnings = total * 0.2
print(f"The profit of your agency from {name} tickes is {winnings:.2f} lv.")
