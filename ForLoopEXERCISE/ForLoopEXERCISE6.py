actor = input()
points_start = float(input())
number_judges = int(input())
total = points_start
for i in range(number_judges):
    judge = input()
    points_judge = float(input())
    points = (len(judge) * points_judge) / 2
    total += points
    if total > 1250.5:
        break
need = 1250.5 - total
if total > 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {total:.1f}!")
else:
    print(f"Sorry, {actor} you need {need:.1f} more!")