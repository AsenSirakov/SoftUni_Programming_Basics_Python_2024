nailon = 1.50
paint = 14.50
thinner = 5
neednailon = int(input())
needpaint = int(input())
needthinn = int(input())
hours = int(input())
extranail = (neednailon+2)
extrapaint = needpaint + ((needpaint/100)*10)
packets = 0.40
costnail= extranail * nailon
costpaint = extrapaint * paint
costhinn = needthinn * thinner
allcostmaterial = costnail + costpaint + costhinn + packets
salaryhour = allcostmaterial * 0.3
salaryday = salaryhour * hours
sumall = allcostmaterial + salaryday
print(sumall)
