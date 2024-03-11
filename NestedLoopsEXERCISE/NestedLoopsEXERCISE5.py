N = int(input())

for num in range(1111, 10000):
    digits = [int(digit) for digit in str(num)]
    if all(digit != 0 and N % digit == 0 for digit in digits):
        print(num, end=" ")
