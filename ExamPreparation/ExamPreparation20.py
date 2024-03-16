days = int(input())
total_food = float(input())

total_eaten_food = 0
total_eaten_dog_food = 0
total_eaten_cat_food = 0
total_biscuits = 0

for day in range(1, days + 1):
    dog_food_eaten = int(input())
    cat_food_eaten = int(input())

    total_food_eaten = dog_food_eaten + cat_food_eaten
    total_eaten_food += total_food_eaten
    total_eaten_dog_food += dog_food_eaten
    total_eaten_cat_food += cat_food_eaten

    if day % 3 == 0:
        biscuits = round(total_food_eaten * 0.1)
        total_biscuits += biscuits

percent_food_eaten = (total_eaten_food / total_food) * 100
percent_dog_food = (total_eaten_dog_food / total_eaten_food) * 100
percent_cat_food = (total_eaten_cat_food / total_eaten_food) * 100

print(f"Total eaten biscuits: {total_biscuits}gr.")
print(f"{percent_food_eaten:.2f}% of the food has been eaten.")
print(f"{percent_dog_food:.2f}% eaten from the dog.")
print(f"{percent_cat_food:.2f}% eaten from the cat.")
