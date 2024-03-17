control_minutes = int(input())
control_seconds = int(input())
meters_lenght = float(input())
sec_per_hun_meter = int(input())
control_swap_to_sec = control_minutes * 60 + control_seconds
delay = meters_lenght / 120
total_delay = delay * 2.5
marin_time = (meters_lenght/100) * sec_per_hun_meter - total_delay
if control_swap_to_sec >= marin_time:
    print(f"Martin Bignev won an Olympic quota!")
    print(f"His time is {marin_time:.3f}.")
else:
    needed_secs = abs(marin_time - control_swap_to_sec)
    print(f"No,Marin failed! He was {needed_secs:.3f} second slower.")