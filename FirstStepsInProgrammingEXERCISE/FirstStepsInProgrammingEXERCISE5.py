pen = 5.80
marker = 7.20
wash = 1.20
pennum = int(input())
markernum = int(input())
washlitre = int(input())
percent = int(input())
sumpen = pennum * pen
summark = markernum * marker
sumwash = washlitre * wash
percentconver= percent/100
sumall = sumpen + summark + sumwash
totalperc = sumall - (sumall * percentconver)
print(totalperc)