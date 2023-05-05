import time

def focus_timer(duration, break_time):
    """A simple focus timer with a duration and break time"""
    while True:
        print("Focus time!")
        time.sleep(duration)
        print("Break time!")
        time.sleep(break_time)

# set the duration and break time (in seconds)
focus_duration = 25 * 60  # 25 minutes
break_time = 5 * 60      # 5 minutes

# start the focus timer
focus_timer(focus_duration, break_time)
