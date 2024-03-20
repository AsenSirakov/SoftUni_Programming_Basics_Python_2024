food_quantity = int(input()) * 1000
total_food_eaten = 0

while True:
    command = input()
    if command == "Adopted":
        break
    food_eaten = int(command)
    total_food_eaten += food_eaten

leftovers = food_quantity - total_food_eaten

if leftovers >= 0:
    print(f"Food is enough! Leftovers: {leftovers} grams.")
else:
    print(f"Food is not enough. You need {abs(leftovers)} grams more.")
