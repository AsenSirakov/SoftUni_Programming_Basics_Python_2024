minutes_per_day = int(input())
number_of_walks_per_day = int(input())
calories_intake = int(input())
total_time = minutes_per_day * number_of_walks_per_day
total_calories_burned = total_time * 5
half_calories = calories_intake / 2
if total_calories_burned >= half_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories_burned}.")