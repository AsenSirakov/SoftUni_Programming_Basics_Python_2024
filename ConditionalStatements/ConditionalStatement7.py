from math import pi
figure = input()
square = 'square'
rectangle = 'rectangle'
circle = 'circle'
triangle = 'triangle'
if figure == square:
    i = float(input())
    areasq = i * i
    print(round(areasq, 3))
elif figure == rectangle:
    a = float(input())
    b = float(input())
    arearec= a * b
    print(round(arearec, 3))
elif figure == circle:
    x = float(input())
    areacirc = pi * (x*x)
    print(round(areacirc, 3))
elif figure == triangle:
    y = float(input())
    z = float(input())
    areatriang = (y*z)/2
    print(round(areatriang, 3))
