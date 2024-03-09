width = int(input())
length = int(input())

total_pieces = width * length
command = input()
pieces_taken = 0

while command != "STOP":
    pieces_taken += int(command)

    if pieces_taken >= total_pieces:
        print(f"No more cake left! You need {pieces_taken - total_pieces} pieces more.")
        break

    command = input()

if command == "STOP":
    print(f"{total_pieces - pieces_taken} pieces are left.")
