month = input()
hours = int(input())
number_of_people_in_the_group = int(input())
time_of_day = input()
day_prices = {"march": 10.50, "april": 10.50, "may": 10.50, "june": 12.60, "july": 12.60, "august": 12.60}
night_prices = {"march": 8.40, "april": 8.40, "may": 8.40, "june": 10.20, "july": 10.20, "august": 10.20}
if time_of_day == "day":
    price_per_person = day_prices[month]
else:
    price_per_person = night_prices[month]

if number_of_people_in_the_group >= 4:
    price_per_person *= 0.9
if hours >= 5:
    price_per_person *= 0.5

total_cost = price_per_person * hours * number_of_people_in_the_group
print(f"Price per person for one hour: {price_per_person:.2f}")
print(f"Total cost of the visit: {total_cost:.2f}")