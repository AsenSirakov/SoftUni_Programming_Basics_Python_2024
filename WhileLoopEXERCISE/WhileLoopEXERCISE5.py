coins = [200, 100, 50, 20, 10, 5, 2, 1]

change = float(input())
change_cents = int(change * 100)

total_coins = 0
index = 0

while change_cents > 0 and index < len(coins):
    current_coin = coins[index]
    coin_count = change_cents // current_coin

    if coin_count > 0:
        total_coins += coin_count
        change_cents %= current_coin


    index += 1

print(f"{total_coins}")
