width = int(input())
length = int(input())
height = int(input())
total = width * length * height
command = input()
box_added = 0
while command != "Done":
    box_added += int(command)
    if box_added > total:
        print(f"No more free space! You need {box_added - total} Cubic meters more.")
        break
    command = input()
if command == "Done":
    print(f"{total - box_added} Cubic meters left.")
