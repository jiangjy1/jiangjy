#数据库查
from dbconn import Employees, Departments, Session

session = Session()
query1 = session.query(Departments)
print(query1)

# for dep in query1:
#     print(dep)      #返回的是Departments的实例
#     print(dep.dep_id,dep.dep_name)
#     print('-'*30)
#################################################
# query2 = session.query(Employees.name,Employees.phone)
# print(query2)
# for item in query2:
#     print(item)
# for name,phone in query2:
#     print('%s:%s'%(name,phone))
#################################################
# query3 = session.query(Departments.dep_name.label('部门'))
# print(query3)
# for dep in query3:
#     print(dep.部门)
#################################################
# query4 = session.query(Departments).order_by(Departments.dep_id)
# for dep in query4:
#     print(dep)
#################################################
# query5 = session.query(Employees)[2:4]      #切片后查询到的不是实例了，而是由实例构成的列表
# print(query5)
#################################################
# query6 = session.query(Departments).filter(Departments.dep_id==1)
# print(query6)
# for dep in query6:
#     print(dep)
#################################################
# query7 = session.query(Employees).filter(Employees.emp_id>1)\
#     .filter(Employees.emp_id<6)
# # print(query7)
# for emp in query7:
#     print(emp)
#################################################
# query8 = session.query(Departments)\
#     .filter(Departments.dep_name.in_(['人事部','运维部']))
# print(query8)
# for dep in query8:
#     print(dep.dep_id,dep.dep_name)
#################################################
#query9 = session.query(Departments) \
#     .filter(~Departments.dep_name.in_(['人事部','运维部']))
# print(query9)
# for dep in query9:
#     print(dep.dep_id,dep.dep_name)
#################################################
from sqlalchemy import and_,or_

# query10 = session.query(Employees)\
#     .filter(and_(Employees.emp_id>1,Employees.emp_id<6))
# print(query10)
# for emp in query10:
#     print(emp)
#################################################
# query11 = session.query(Employees)\
#     .filter(or_(Employees.emp_id==6,Employees.gender=='女'))
# print(query11)
# for emp in query11:
#     print(emp)
#
# result = query11.all()      #all取出全部值
# print(result)
# result1 = query11.first()   #取出查询集中的第一个结果
# print(result1)
# result2 = query11.one()     #只取出一个结果，超过一个报错
# print(result2)
##################################################
# query12 = session.query(Departments).count()
# print(query12)      #select count(*) from Departments;
##################################################
# query先写的是Employees.name,join 时就要用Departments
query13 = session.query(Employees.name,Departments.dep_name,Departments.dep_id)\
    .join(Departments,Employees.dep_id==Departments.dep_id)
print(query13)
for dep_id,emp_name,dep in query13:
    print(dep_id,emp_name,dep)