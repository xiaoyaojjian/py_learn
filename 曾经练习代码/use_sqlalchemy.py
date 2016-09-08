from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# create object's base
Base = declarative_base()
# define User object


class User(Base):
    # table name
    __tablename__ = 'user'
    # table struture
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
# initialize DB connect
engine = create_engine(
    'mysql+mysqlconnector://root:password@localhost:3306/test')
# create DBSession type
DBSession = sessionmaker(bind=engine)
# 以上往常SQLAlchemyの initialize an every table class define
# 可继续define其他class
# ORM = Object-Relation Mapping
# 将关系数据库の表结构映射到对象上

# 由于ORM 向数据库中添加一条记录 视为添加一个User对象

# create session object
session = DBSession()
# createe new User object
new_user = User(id='5', name='Bob')
# add to session
session.add(new_user)
# commit and save as DB
session.commit()
# close session
session.close()

# 查询数据 不是tuple 而是User对象
# create session
session = DBSession()
# create Query select,filter is where 条件 后调用one() return 唯一行,而调用all()
# return 所有行
user = session.query(User).filter(User.id == '5').one()
# print type and object's name property
print('type:', type(user))
print('name:', user.name)
session.close()
# 关系数据库多个表可使用外键实现一对多，多对多等关联
# ORM框架可实现两个对象一对多，多对多等功能


class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # one to more
    books = relationship('Book')


class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # '多'の一方のbook表示通过外键关联到user表
    user_id = Column(String(20), ForeginKey('user.id'))
# when we select a User object,its object's books property will return a list including some Book object
# ORM 框架 to 将数据库表の一行记录与一个对象互相做自动转换
