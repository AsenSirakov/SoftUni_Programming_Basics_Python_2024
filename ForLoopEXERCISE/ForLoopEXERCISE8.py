import math

tours = int(input())
initial_points = int(input())
total = 0
win = 0
for i in range(tours):
    stage = input()
    if stage == 'F':
        total+=1200
    elif stage == 'SF':
        total+=720
    elif stage == 'W':
        total+=2000
        win+= 1
average = total / tours
all = initial_points + total
winp = (win/tours) * 100
print(f"Final points: {all}")
print(f"Average points: {math.floor(average)}")
print(f"{winp:.2f}%")