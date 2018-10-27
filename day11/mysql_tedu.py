import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='tedu.cn',
    db='tedu1805',
    charset='utf8'
)

cursor=conn.cursor()
############################################################
#增
# insert1='insert into departments(dep_id,dep_name) VALUES (%s,%s)'
# result1=cursor.execute(insert1,(1,'人事部'))
# result2=cursor.executemany(insert1,[(2,'运维部'),(3,'开发部')])
# result3=cursor.executemany(insert1,[(4,'财务部'),(5,'销售部'),(6,'市场部')])
############################################################
# 查
# query1="select * from departments"
# result4=cursor.execute(query1)
# print(cursor.fetchone())
# print('-'*30)
# print(cursor.fetchmany(2))
# print('-'*30)
# print(cursor.fetchall())
############################################################
# query1="select * from departments"
# result4=cursor.execute(query1)
# print(cursor.fetchone())
# print('-'*30)
# cursor.scroll(0,mode='absolute')
# print(cursor.fetchone())
# print('-'*30)
# cursor.scroll(2)  vc
# print(cursor.fetchone())
# cursor.scroll(1,mode='absolute')
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
#############################################################
# 改
# update1="update departments set dep_name=%s where dep_name=%s"
# result5=cursor.execute(update1,('人力资源部','人事部'))
# print(result5)      #返回1，表示影响一行记录
############################################################
# 删
delete1="delete from departments where dep_name=%s"
result6=cursor.execute(delete1,'市场部')
print(result6)


conn.commit()
cursor.close()
conn.close()