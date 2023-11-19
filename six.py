import time

# Get the current time in 24-hour format
current_time = time.localtime().tm_hour

# Greet the user based on the time of the day
if 5 <= current_time < 12:
    print("Good morning!")
elif 12 <= current_time < 17:
    print("Good afternoon!")
else:
    print("Good evening!")
