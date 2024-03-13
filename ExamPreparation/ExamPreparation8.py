record_second = float(input())
distance_meters = float(input())
meters_delay_per_second = float(input())
additional = (distance_meters // 50) * 30
total = distance_meters * meters_delay_per_second
record = total + additional
if record < record_second:
    print(f"Yes! The new record is {record:.2f} seconds.")
else:
    needed_seconds = record - record_second
    print(f"No! He was {needed_seconds:.2f} seconds slower.")



