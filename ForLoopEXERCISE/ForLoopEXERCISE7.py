group_count = int(input())
total = 0
musala = 0
monblan = 0
kili = 0
k2 = 0
everest = 0
for i in range(group_count):
    group_size = int(input())
    total += group_size
    if group_size <=5:
        musala += group_size
    elif 6 <= group_size <= 12:
        monblan += group_size
    elif 13 <= group_size <= 25:
        kili += group_size
    elif 26<= group_size <= 40:
        k2+= group_size
    else:
        everest += group_size

musalap = musala / total * 100
monp = monblan / total * 100
kilip = kili / total * 100
k2p = k2 / total * 100
everp = everest / total * 100

print(f"{musalap:.2f}%")
print(f"{monp:.2f}%")
print(f"{kilip:.2f}%")
print(f"{k2p:.2f}%")
print(f"{everp:.2f}%")