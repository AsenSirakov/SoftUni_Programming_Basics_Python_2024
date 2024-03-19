minutes_walk_per_day = int(input())
number_walks_per_day = int(input())
calories_per_day = int(input())
minutes_total = minutes_walk_per_day * number_walks_per_day
calories_burn_total = minutes_total * 5
half_calories_per_day = calories_per_day / 2
if calories_burn_total >= half_calories_per_day:
    print(f"Yes,the walk for your cat is enough. Burned calories per day : {calories_burn_total}.")
else:
    print(f"No,the walk for your cat is not enough. Burned calories per day: {calories_burn_total}. ")