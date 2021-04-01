import src.main.pysql.pysql_test as pysql
import random
import src.spyder.pic_operation as po
import src.main.utils.option as option
import os

lst = pysql.find_ids_by_tag('旗袍')
n = random.randint(0, lst.__len__())
src = pysql.get_dir(lst[n])
dir = po.get_local_dir(src, 'C:/Users/zwc/Desktop/ys/test/')
print(dir + os.listdir(dir)[0])
