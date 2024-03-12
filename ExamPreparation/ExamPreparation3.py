country = input()
tool = input()
hard = 0
do = 0
if tool == "ribbon":
    if country == "Russia":
        hard = 9.100
        do = 9.400
    elif country == "Bulgaria":
        hard = 9.600
        do = 9.400
    elif country == "Italy":
        hard = 9.200
        do = 9.500
if tool == "hoop":
    if country == "Russia":
        hard = 9.300
        do = 9.800
    elif country == "Bulgaria":
        hard = 9.550
        do = 9.750
    elif country == "Italy":
        hard = 9.450
        do = 9.350
if tool == "rope":
    if country == "Russia":
        hard = 9.600
        do = 9.000
    elif country == "Bulgaria":
        hard = 9.500
        do = 9.400
    elif country == "Italy":
        hard = 9.700
        do = 9.150
total = hard + do
percent = 20 - total
percent_miss = (percent/20) * 100
print(f"The team of {country} get {total:.3f} on {tool}.")
print(f"{percent_miss:.2f}%")
