strawberries_price = float(input())
bananas_quantity_kgs = float(input())
orange_quantity_kgs = float(input())
berry_quantity_kgs = float(input())
strawberries_quantity_kgs = float(input())
berry_price = strawberries_price / 2
orange_price = berry_price - (berry_price*0.4)
banana_price = berry_price - (berry_price*0.8)
sum_berry = berry_quantity_kgs * berry_price
sum_orange = orange_quantity_kgs * orange_price
sum_banana = bananas_quantity_kgs * banana_price
sum_strawberry = strawberries_quantity_kgs * strawberries_price
sum_all = sum_berry + sum_orange + sum_banana + sum_strawberry
print(f"{sum_all:.2f}")