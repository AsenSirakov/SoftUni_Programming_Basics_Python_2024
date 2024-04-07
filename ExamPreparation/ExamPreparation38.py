number_of_climber_groups = int(input())
musala = 0
montblan = 0
kili = 0
k2 = 0
ever = 0
for i in range(number_of_climber_groups):
    number_of_climbers = int(input())
    if number_of_climbers <= 5:
        musala += number_of_climbers
    elif 6 <= number_of_climbers <= 12:
        montblan += number_of_climbers
    elif 13 <= number_of_climbers <= 25:
        kili += number_of_climbers
    elif 26 <= number_of_climbers <= 40:
        k2 += number_of_climbers
    else:
        ever += number_of_climbers
total = musala + montblan + kili + k2 + ever
percent_m = musala / total * 100
percent_mn = montblan / total * 100
percent_kil = kili / total * 100
percent_k2 = k2 / total * 100
percent_ev = ever / total * 100
print(f"{percent_m:.2f}%")
print(f"{percent_mn:.2f}%")
print(f"{percent_kil:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_ev:.2f}%")


