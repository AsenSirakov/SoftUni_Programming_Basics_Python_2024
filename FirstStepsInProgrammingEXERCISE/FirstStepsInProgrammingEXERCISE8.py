annualprice = int(input())
shoes = annualprice - (annualprice * 0.4)
clothes = shoes - (shoes * 0.2)
ball = clothes / 4
accessories = ball / 5
sumall = annualprice + shoes + clothes + ball + accessories
print(sumall)