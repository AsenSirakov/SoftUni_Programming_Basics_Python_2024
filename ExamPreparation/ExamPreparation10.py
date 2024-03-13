import math

wall_height = int(input())
wall_width = int(input())
percent_not_painted = int(input())
total_surface_area = 4 * wall_height * wall_width
painted_surface_area = total_surface_area * (100 - percent_not_painted) / 100
paint_left = 0

while painted_surface_area > 0:
    command = input()
    if command == "Tired!":
        break
    else:
        liters_of_paint = int(command)
        painted_surface_area -= liters_of_paint
        if painted_surface_area < 0:
            paint_left = abs(painted_surface_area)
            painted_surface_area = 0

if paint_left > 0:
    print(f"All walls are painted and you have {paint_left:.1f} l paint left!")
elif painted_surface_area == 0:
    print("All walls are painted! Great job, Pesho!")
else:
    print(f"{math.ceil(painted_surface_area)} quadratic m left.")
