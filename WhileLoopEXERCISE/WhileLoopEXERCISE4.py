required_steps = 10000
made_steps = 0

while True:
    command = input()

    if command == "Going home":
        additional_steps = int(input())
        made_steps += additional_steps

        if made_steps >= required_steps:
            print("Goal reached! Good job!")
            print(f"{made_steps - required_steps} steps over the goal!")
        else:
            print(f"{required_steps - made_steps} more steps to reach goal.")
        break

    steps = int(command)
    made_steps += steps

    if made_steps >= required_steps:
        print("Goal reached! Good job!")
        print(f"{made_steps - required_steps} steps over the goal!")
        break