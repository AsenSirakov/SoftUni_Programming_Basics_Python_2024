number_of_movies = int(input())
highest_rating = 0
lowest_rating = 0
high_movie = ""
low_movie = ""
total = 0
for i in range(number_of_movies):
    name = input()
    rating = float(input())
    if rating > highest_rating:
        highest_rating = rating
        high_movie = name
    else:
        lowest_rating = rating
        low_movie = name
    total += rating
average = total / number_of_movies
print(f"{high_movie} is with highest rating: {highest_rating:.1f}")
print(f"{low_movie} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average:.1f}")