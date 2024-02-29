hours = int(input())
minutes = int(input())
new_hour = (hours + (minutes + 15) // 60) % 24
new_minutes = (minutes + 15) % 60
if new_minutes < 10:
    print(f'{new_hour}:0{new_minutes}')
else:
    print(f'{new_hour}:{new_minutes}')