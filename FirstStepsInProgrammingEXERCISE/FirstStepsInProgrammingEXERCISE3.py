deposit = float(input())
duration = int(input())
interest = float(input())
convert = interest/100
total = deposit + duration * ((deposit * convert)/12)
print(total)
