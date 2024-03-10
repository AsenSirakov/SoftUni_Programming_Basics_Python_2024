fnum = int(input())
snum = int(input())
for num in range(fnum, snum+1):
    num_str = str(num)
    even = 0
    odd = 0
    for index, digit in enumerate(num_str):
        digit_value = int(digit)
        if index % 2 == 0:
            even += digit_value
        else:
            odd += digit_value
    if even == odd:
        print(num, end=" ")
print()