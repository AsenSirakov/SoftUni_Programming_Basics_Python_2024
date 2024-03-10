total_destination = 0
while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())
    saved_money = 0
    while saved_money < budget:
        current_savings = float(input())
        saved_money += current_savings
    print(f"Going to {destination}!")
    total_destination +=1
