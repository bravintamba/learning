from time import time

now = time()

# Seconds in a day = 24 * 60 * 60 = 86400
days_since_epoch = int(now // 86400)

# Get the remainder of seconds for the current day
seconds_left = int(now % 86400)

hours = seconds_left // 3600
minutes = (seconds_left % 3600) // 60
seconds = seconds_left % 60

print(f"Days since epoch: {days_since_epoch}")
print(f"Current time: {hours:02d}:{minutes:02d}:{seconds:02d} UTC")