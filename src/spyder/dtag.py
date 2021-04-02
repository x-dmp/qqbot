import os
import sys
sys.path.append('/usr/local/qbot/bot/')
import src.spyder.pic_operation as T
import time
from PIL import Image

local_dir = 'C:/Users/zwc/Desktop/piv/'
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
    img = Image.open(local_dir + ii)
    img.save(store_dir + d + s + '.png')
    print(store_dir + d + s + '.png')
    time.sleep(3)

