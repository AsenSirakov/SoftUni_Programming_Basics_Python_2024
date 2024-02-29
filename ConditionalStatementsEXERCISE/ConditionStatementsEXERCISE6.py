record_seconds = float(input())
meters = float(input())
meter_per_second = float(input())
time_to_swim = meters * meter_per_second
slow = (meters//15) * 12.5
total_time = time_to_swim + slow
if total_time < record_seconds:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    needed_time = total_time - record_seconds
    print(f"No, he failed! He was {needed_time:.2f} seconds slower.")