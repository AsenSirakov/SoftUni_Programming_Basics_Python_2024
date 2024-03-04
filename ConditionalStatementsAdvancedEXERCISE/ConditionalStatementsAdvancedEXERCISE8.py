exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

exam_time = exam_hour * 60 + exam_min
arrival_time = arrival_hour * 60 + arrival_min
time_difference = arrival_time - exam_time

if time_difference > 0:
    print('Late')
    if time_difference < 60:
        print(f"{time_difference} minutes after the start")
    else:
        hours = time_difference // 60
        minutes = time_difference % 60
        print(f"{hours}:{minutes:02d} hours after the start")
elif time_difference == 0:
    print('On time')
elif 0 > time_difference >= -30:
    print('On time')
    print(f"{abs(time_difference)} minutes before the start")
elif -30 > time_difference > -60:
    print('Early')
    print(f"{abs(time_difference)} minutes before the start")
else:
    print('Early')
    hours = abs(time_difference) // 60
    minutes = abs(time_difference) % 60
    print(f"{hours}:{minutes:02d} hours before the start")
