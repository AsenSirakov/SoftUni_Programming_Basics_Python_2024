inpt = input()
min = 100000000
while inpt != "Stop":
    num = int(inpt)
    if num < min:
        min = num
    inpt = input()
print(min)