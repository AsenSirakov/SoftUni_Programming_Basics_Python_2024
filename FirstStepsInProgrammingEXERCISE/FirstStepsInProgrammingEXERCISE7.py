chickmenu = int(input())
fishmenu = int(input())
vegmenu = int(input())
delivery = 2.50
chickall = chickmenu * 10.35
fishall = fishmenu * 12.40
vegall = vegmenu * 8.15
sumall = chickall + fishall + vegall
dessert = sumall * 0.2
total = sumall + dessert + delivery
print(total)