n = int(input())
odd = 0
even = 0
for i in range(1, n+1):
    element = int(input())
    if i % 2 == 0:
        even+= element
    else:
        odd+= element
if odd == even:
    print('Yes')
    print(f"Sum = {odd}")
else:
    diff = abs(odd-even)
    print('No')
    print(f"Diff = {diff}")
