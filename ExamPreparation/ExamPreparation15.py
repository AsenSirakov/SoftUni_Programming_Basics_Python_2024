total_visitors = int(input())

back_count = 0
chest_count = 0
legs_count = 0
abs_count = 0
protein_shake_count = 0
protein_bar_count = 0

for _ in range(total_visitors):
    activity = input()
    if activity == "Back":
        back_count += 1
    elif activity == "Chest":
        chest_count += 1
    elif activity == "Legs":
        legs_count += 1
    elif activity == "Abs":
        abs_count += 1
    elif activity == "Protein shake":
        protein_shake_count += 1
    elif activity == "Protein bar":
        protein_bar_count += 1

workout_percent = (back_count + chest_count + legs_count + abs_count) / total_visitors * 100
protein_percent = (protein_shake_count + protein_bar_count) / total_visitors * 100

print(f"{back_count} - back")
print(f"{chest_count} - chest")
print(f"{legs_count} - legs")
print(f"{abs_count} - abs")
print(f"{protein_shake_count} - protein shake")
print(f"{protein_bar_count} - protein bar")
print(f"{workout_percent:.2f}% - work out")
print(f"{protein_percent:.2f}% - protein")
