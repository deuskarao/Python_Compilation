import time
import Schedule

timee = "08:51"  # Specific Time When The message will be send

try:
    schedule.every().day.at(timee).do("function")
except TypeError:
    pass

try:
    while True and x != 1:
        schedule.run_pending()
        time.sleep(1)
except UnboundLocalError:
    pass
