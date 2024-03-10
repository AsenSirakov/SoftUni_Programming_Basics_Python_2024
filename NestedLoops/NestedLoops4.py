start = int(input())
final = int(input())
magic = int(input())
combinations = 0
is_foind = False
for i in range(start, final+1):
    for j in range(start, final+1):
        combinations+=1
        if i + j == magic:
            is_foind = True
            print(f"Combination N:{combinations} ({i} + {j} = {magic})")
            break
    if is_foind:
        break

if not is_foind:
    print(f"{combinations} combinations - neither equals {magic}")