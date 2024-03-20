racket_price = float(input())
racket_quantity = int(input())
shoe_pairs_quantity = int(input())

racket_cost = racket_price * racket_quantity
shoe_cost = (racket_price / 6) * shoe_pairs_quantity
other_equipment_cost = (racket_cost + shoe_cost) * 0.2

total_cost = racket_cost + shoe_cost + other_equipment_cost
djokovic_payment = total_cost / 8
sponsors_payment = total_cost * 7 / 8

print(f"Price to be paid by Djokovic {int(djokovic_payment)}")
print(f"Price to be paid by sponsors {int(sponsors_payment)}")
