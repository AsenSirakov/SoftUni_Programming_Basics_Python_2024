venue_rent = int(input())
statue = venue_rent - (venue_rent*0.3)
catering = statue - (statue*0.15)
sound = catering / 2
total = venue_rent + statue + catering + sound
print(f"{total:.2f}")
