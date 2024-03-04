lenght = input()
sum = 0
for i in range(0, len(lenght)):
    if lenght[i] == 'a':
        sum+=1
    elif lenght[i] == 'e':
        sum+=2
    elif lenght[i] == 'i':
        sum+=3
    elif lenght[i] == 'o':
        sum+=4
    elif lenght[i] == 'u':
        sum+=5
print(sum)