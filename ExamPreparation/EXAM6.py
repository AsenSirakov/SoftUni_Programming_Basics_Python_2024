number_of_locations = int(input())
for _ in range(number_of_locations):
    expected_gold = float(input())
    days = int(input())
    total_gold = 0
    count_days = 0
    for _ in range(days):
        gold = float(input())
        total_gold += gold
        count_days += 1

    average = total_gold / count_days
    if average >= expected_gold:
        print(f"Good job! Average gold per day: {average:.2f}.")
    else:
        needed_gold = expected_gold - average
        print(f"You need {needed_gold:.2f} gold.")