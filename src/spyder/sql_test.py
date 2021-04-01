import src.main.pysql.pysql_test as pysql
import random

lst = pysql.find_ids_by_tag('女孩子')
n = random.randint(0, lst.__len__())
print(pysql.get_dir(n))