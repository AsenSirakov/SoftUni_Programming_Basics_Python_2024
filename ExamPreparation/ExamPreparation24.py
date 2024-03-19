name = input()
nubmer_ticket_adult = int(input())
number_ticket_child = int(input())
price_adult = float(input())
price_kid = price_adult -(price_adult * 0.7)
service = float(input())
total_adult = price_adult + service
total_kid = price_kid + service
all = (nubmer_ticket_adult * total_adult) + (number_ticket_child * total_kid)
final_price = all * 0.2
print(f"The profit of your agency from {name} tickets is {final_price:.2f} lv.")