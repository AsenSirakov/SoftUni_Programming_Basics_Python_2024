lengthcm = int(input())
widthcm = int(input())
heightcm = int(input())
percent = int(input())
vol = lengthcm * widthcm * heightcm
liters = vol/1000
occupied = percent/100
neededwater = liters *(1 - occupied)
print(neededwater)