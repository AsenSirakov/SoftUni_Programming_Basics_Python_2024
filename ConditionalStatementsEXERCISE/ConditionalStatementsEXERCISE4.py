excursion = float(input())
puzzles = int(input())
dolls = int(input())
bear = int(input())
minion = int(input())
truck = int(input())
suma = (puzzles * 2.60) + (dolls * 3) + (bear * 4.10) + (minion * 8.20) + (truck * 2)
numbertoys = puzzles + dolls + bear + minion + truck
total = 0
if numbertoys >= 50:
    total = suma - (0.25 * suma)
else:
    total = suma
rent = total * 0.1
winning = total - rent
leftover = 0
missing = 0
if winning >= excursion:
    leftover = winning - excursion
    print(f'Yes! {leftover:.2f} lv left.')
else:
    missing = excursion - winning
    print(f'Not enough money! {missing:.2f} lv needed.')

