import time
from time import strftime, localtime

mail_head = ""


def timee():
    global mail_head

    start = strftime("%d.%m.%Y - %H:%M:%S", localtime())

    x = 5
    time.sleep(x)

    finish = strftime("%d.%m.%Y - %H:%M:%S", localtime())

    if int(int(finish[20]) - int(start[20])) == x:

        mail_head = finish


timee()
