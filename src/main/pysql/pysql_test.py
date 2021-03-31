import pymysql
from src.main.utils.direction import get_dir

def insert_pic(uid, dir, tag):
   flag = True

   db = pymysql.connect(host='localhost', user='root', passwd='root', db='setu_t_p', port=3306, charset='utf8')
   cursor = db.cursor()
   sql = """INSERT INTO setupic(uid,dir,tag)VALUES(%s,%s,%s)"""
   sqlargs=[]
   sqlargs.append(uid)
   sqlargs.append(dir)
   sqlargs.append(tag)

   try:
      # 执行sql语句
      cursor.execute(query=sql,args=sqlargs)
      print('执行sql语句')
      # 提交到数据库执行
      db.commit()
      print('提交数据库')
   except:
      # 如果发生错误则回滚
      db.rollback()
      print('错误')
      flag=False
   cursor.close()
   db.close()

   return flag


def find_ids_by_tag(tag):
   # 打开数据库连接
   db = pymysql.connect(host='localhost', user='root', passwd='root', db='setu_t_p', port=3306, charset='utf8')

   # 使用cursor()方法获取操作游标
   cursor = db.cursor()

   # SQL 插入语句
   sql = """SELECT * FROM setupic WHERE tag LIKE %s"""
   tag = '%' + tag + '%'
   sqlargs = []
   ids = []
   sqlargs.append(tag)
   try:
      # 执行sql语句
      cursor.execute(query=sql, args=sqlargs)
      print('执行sql语句')

      # 获取结果
      results = cursor.fetchall()
      for row in results:
         ids.append(row[0])
   except:
      # 如果发生错误
      print('错误')

   cursor.close()
   db.close()
   print(ids)
   return ids

