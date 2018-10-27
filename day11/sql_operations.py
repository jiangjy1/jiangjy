#数据库增
from dbconn import Departments, Session, Salary, Employees
from sqlalchemy.orm import sessionmaker

session = Session()
# hr=Departments(dep_name='运维部')
# print(hr.dep_name)
# print(hr.dep_id)
# session.add(hr)
# session.commit()
# print(hr.dep_id)
#############################################
# ops = Departments(dep_id=6,dep_name='营销部')
# dev = Departments(dep_id=7,dep_name='开发部')
# session.add_all([ops,dev])
#############################################
# jjy = Employees(
#     name='姜俊羽',
#     gender='男',
#     birth_date='1995-10-6',
#     phone='15700064723',
#     email='jjy@qq.com',
#     dep_id=1
# )
# hsm = Employees(
#     name='何孙淼',
#     gender='女',
#     birth_date='1998-10-8',
#     phone='18866663333',
#     email='hsm@qq.com',
#     dep_id=4
# )
# hst = Employees(
#     name='胡森涛',
#     gender='男',
#     birth_date='1996-6-8',
#     phone='17812345678',
#     email='hst@qq.com',
#     dep_id=5
# )
# session.add_all([jjy, hsm, hst])

session.commit()
session.close()
