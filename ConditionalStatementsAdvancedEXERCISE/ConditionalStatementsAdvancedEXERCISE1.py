screening = input()
rows = int(input())
cols = int(input())
income = 0
capacity = rows * cols
if screening == 'Premiere':
    income = capacity * 12.00
elif screening == 'Normal':
    income = capacity * 7.50
elif screening == 'Discount':
    income = capacity * 5.00

print(f'{income:.2f} leva')