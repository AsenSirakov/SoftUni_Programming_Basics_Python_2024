initial_food = int(input())
total_food_consumed = 0
while True:
    command = input()
    if command == "Adopted":
        break
    else:
        food_consumed = int(command)
        total_food_consumed += food_consumed
leftovers = initial_food * 1000 - total_food_consumed
if leftovers >= 0:
    print(f"Food is enough! Leftovers: {leftovers} grams.")
else:
    needed_food = abs(leftovers)
    print(f"Food is not enough. You need {needed_food} grams more.")