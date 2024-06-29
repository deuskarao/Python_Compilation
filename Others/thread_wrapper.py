import threading
import time


def as_thread(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(
            target=func,
            args=args,
            kwargs=kwargs
        )
        thread.start()
        return thread
    return wrapper


@as_thread
def func1():
    time.sleep(15)
    print("slept 15")


@as_thread
def func2():
    time.sleep(3)
    print("slept 3")


func1()
func2()
