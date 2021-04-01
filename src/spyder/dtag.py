import os
import src.spyder.test as T
import time

local_dir = 'C:/Users/zwc/Desktop/ys/tmp/'
store_dir = 'C:/Users/zwc/Desktop/ys/test/'
lst = os.listdir(local_dir)
for ii in lst:
    s = ii.split('_')[0]
    d = ''
    for j in s:
        d = d + j + '/'
        if not os.path.exists(store_dir + d):
            os.mkdir(store_dir + d)
    print(store_dir + d)
    dr = store_dir + d
    if not os.path.exists(dr):
        os.mkdir(dr)
    T.store_pic_by_id(s, dr, d)
    time.sleep(2)

