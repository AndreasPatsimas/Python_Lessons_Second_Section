from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2 - t1} sec")
        pass
    return wrapper

@performance
def long_time():
    for i in range(0, 10000000):
        i + 1
        pass
    pass

long_time()

