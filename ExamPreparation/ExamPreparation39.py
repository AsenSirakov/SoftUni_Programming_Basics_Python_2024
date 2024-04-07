budget = float(input())
total = 0
while True:
    actor_name = input()
    if actor_name == "ACTION":
        break
    if len(actor_name) > 15:
        payment = budget * 0.20
    else:
        payment = float(input())
    total+= payment
    budget -= payment
    if budget <= 0:
        print(f"We need {-budget:.2f} leva for our actors.")
        break
if budget > 0:
    print(f"We are left with {budget:.2f} leva.")
