import math

series_name = input()
duration_episode = int(input())
duration_break = int(input())
lunchtime = duration_break / 8
relaxtime = duration_break / 4
freetime = duration_break - lunchtime - relaxtime
if freetime >= duration_episode:
    remaining_time = math.ceil(freetime - duration_episode)
    print(f"You have enough time to watch {series_name} and left with {remaining_time} minutes free time.")

else:
    needed_time = math.ceil(duration_episode - freetime)
    print(f"You don't have enough time to watch {series_name}, you need {needed_time} more minutes.")
