needed_money = float(input())
available_money = float(input())
days_count = 0
spending = 0
while available_money < needed_money and spending < 5:
    command = input()
    money = float(input())
    days_count+=1
    if command == 'save':
        available_money+= money
        spending = 0
    elif command == 'spend':
        available_money-=money
        spending+=1
        if available_money<0:
            available_money = 0
if spending == 5:
    print("You can't save the money.")
    print(days_count)
if available_money >= needed_money:
    print(f"You saved the money for {days_count} days.")