width = float(input())
length = float(input())
height = float(input())
average_astronaut_height = float(input())
room_volume_for_one_astronaut = (average_astronaut_height + 0.40) * 2 * 2
spaceship_volume = width * length * height
number_of_astronauts = int(spaceship_volume // room_volume_for_one_astronaut)
if 3 <= number_of_astronauts <= 10:
    print(f"The spacecraft holds {number_of_astronauts} astronauts.")
elif number_of_astronauts < 3:
    print("The spacecraft is too small.")
else:
    print("The spacecraft is too big.")