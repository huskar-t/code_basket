#coding:utf-8
import datetime

import sqlalchemy
import uuid
from sqlalchemy.orm import sessionmaker

from models import User

engine = sqlalchemy.create_engine("mysql://root:800Lhxz50Xfsws@127.0.0.1/thinkphp",
                                  encoding='utf-8', echo=True)
DB_Session = sessionmaker(bind=engine)

add_session = DB_Session()

# user1 = User(uid = str(uuid.uuid4()), name="max4",pwd="123",reg_time=datetime.datetime.now())
# user2 = User(uid = str(uuid.uuid4()), name="max5",pwd="123",reg_time=datetime.datetime.now())
# user3 = User(uid = str(uuid.uuid4()), name="max6",pwd="123",reg_time=datetime.datetime.now())
# # 单个增
# add_session.add(user1)
# # 批量增
# add_session.add_all([user2,user3])
# # 提交
# add_session.commit()
# # 关闭session
# add_session.close()

# 查
# retrieve_session = DB_Session()
# user = retrieve_session.query(User).filter_by(name = "max4").first()
# retrieve_session.close()
# print(user)

# filter
# equals:

# query(User).filter(User.id == 10001)
# # not equals:
# query(User).filter(User.id != 100)
# # LIKE:
# query(User).filter(User.name.like("%feng%"))
#
# # IN:
# query(User).filter(User.name.in_(['feng', 'xiao', 'qing']))
# # not in
# query(User).filter(~User.name.in_(['feng', 'xiao', 'qing']))
#
# # AND:
# from sqlalchemy import and_
# query(User).filter(and_(User.name == 'fengxiaoqing', User.id ==10001))
#
# # 或者
# query(User).filter(User.name == 'fengxiaoqing').filter(User.id == 100)
#
# # OR:
# from sqlalchemy import or_
# query.filter(or_(User.name == 'fengxiaoqing', User.id ==18))

# 更新

# update_session = DB_Session()
# user = update_session.query(User).filter_by(name = "max4").first()
# print(user.pwd)
# user.pwd = "qwert"
# update_session.commit()
# new_user = update_session.query(User).filter_by(name = "max4").first()
# print(new_user.pwd)
# update_session.close()

# 删除，查询出来直接删
delete_session = DB_Session()
delete_session.query(User).filter_by(name = "max5").delete()
delete_session.commit()
delete_session.close()