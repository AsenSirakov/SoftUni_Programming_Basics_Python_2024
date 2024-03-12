days = int(input())
hours_per_day = int(input())
total_cost = 0

for day in range(1, days + 1):
    daily_cost = 0

    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            daily_cost += 2.50
        elif (day % 2 != 0 and hour % 2 == 0):
            daily_cost += 1.25
        else:
            daily_cost += 1

    print(f"Day: {day} - {daily_cost:.2f} leva")
    total_cost += daily_cost

print(f"Total: {total_cost:.2f} leva")
