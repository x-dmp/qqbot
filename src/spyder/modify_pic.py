import os
from PIL import Image
import random

src = 'C:/Users/zwc/Desktop/ys/tmp/'
# src = 'C:/Users/zwc/Downloads/aml/aml/'
location = 'C:/Users/zwc/Desktop/res/'

local_num = os.listdir(location).__len__()
cur = 0
l = os.listdir(src)
for i in l:
    img = Image.open(src+i)
    if os.path.getsize(src+i)/800000 > 5.0:
        width = img.size[0]
        height = img.size[1]
        img = img.resize((int(width * 0.3), int(height * 0.3)), Image.ANTIALIAS)
    elif os.path.getsize(src+i)/800000 > 3:
        width = img.size[0]
        height = img.size[1]
        img = img.resize((int(width * 0.5), int(height * 0.5)), Image.ANTIALIAS)
    elif os.path.getsize(src+i)/800000 > 1:
        width = img.size[0]
        height = img.size[1]
        img = img.resize((int(width * 0.8), int(height * 0.8)), Image.ANTIALIAS)
    print(cur)
    cur += 1
    img.save(location + str(local_num) + '.png')
    local_num += 1