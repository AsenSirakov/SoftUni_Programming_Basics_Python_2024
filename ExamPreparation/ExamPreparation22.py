import math

name = input()
seasons = int(input())
episodes = int(input())
duration_without_ads = float(input())
ads = duration_without_ads * 0.2
duration_with_ads = duration_without_ads + ads
specials = seasons * 10
total = (duration_with_ads * episodes * seasons) + specials
print(f"Total time needed to watch the {name} series is {math.floor(total)} minutes.")