import random
import os


def get_random_src(dir: str) -> str:
    try:
        lst = os.listdir(dir)
        src = dir
        while True:
            n = random.randint(0, lst.__len__())
            src = src + lst[n-1]
            lst = os.listdir(src)
            if lst.__len__() == 0:
                break
            src += '/'
    except Exception:
        pass
    return src

s = get_random_src('C:/Users/zwc/Desktop/ys/setu/')
print(s)