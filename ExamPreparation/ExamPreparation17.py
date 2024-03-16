number_of_buns = int(input())

max_points = -1
winner_name = ""

while number_of_buns > 0:
    baker_name = input()
    total_points = 0

    while True:
        command = input()
        if command == "Stop":
            break

        points = int(command)
        total_points += points

    print(f"{baker_name} has {total_points} points.")

    if total_points > max_points:
        max_points = total_points
        winner_name = baker_name
        print(f"{winner_name} is the new number 1!")

    number_of_buns -= 1

print(f"{winner_name} won competition with {max_points} points!")
