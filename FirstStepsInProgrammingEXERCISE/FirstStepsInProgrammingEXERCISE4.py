from math import floor
npages = int(input())
pageperone = int(input())
ndays = int(input())
hoursall = npages / pageperone
hoursday = hoursall / ndays
print(floor(hoursday))