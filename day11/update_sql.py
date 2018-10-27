from dbconn import Employees, Departments, Session

session = Session()
########################################################
# dep = session.query(Departments).get(1)     #取出主键是1的部门
# dep.dep_name='人力资源部'
# session.commit()
########################################################
emp = session.query(Employees).get(1)
session.delete(emp)
session.commit()