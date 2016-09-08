#-*-coding:utf-8-*-
__author__ = 'zlxs'
'''
day 3:create a global connection pool
every HTTP request directly collect DB connect from connect pool
'''
import asyncio
import logging
import aiomysql


def log(sql, args=()):
    logging.info('SQL: %s' % sql)

# create connection pool
# 连接池由全局变量__pool存储，缺省情况下将编码设置为utf8，自动提交事务

async def create_pool(loop, **kw):
    logging.info('Create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf-8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )

# 要执行SELECT语句 利用select fun to execute and 需要传入SQL 语句和SQLargument

async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    async with __pool as conn:
        cur = await conn.cursor(aiomysql.DictCursor)
        # SQL语句占位符is ？ BUT MYSQL占位符 is %s
        await cur.execute(sql.replace('?', '%s'), args or ())
        if size:    # select fun 内部自动替换
            rs = await cur.fetchmany(size)  # 部分记录
        else:
            rs = await cur.fetchall()   # 所有记录
        await cur.close()
        logging.info('Row returned: %s' % len(rs))
        return rs   # return result set

# execute 是将 INSERT UPDATE DELETE 语句通用（统一化）{这3中语句都是需要相同参数 及返回一个整数（表示影响的行数）}

async def execute(sql, args):
    log(sql)
    with (await __pool) as conn:
        try:
            cur = await conn.cursor()
            await cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            await cur.close()
        except BaseException as e:
            raise
        return affected     # # return result number


def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
        return ', '.join(L)

# field is 域(字段) 及 stringfield,booleanfield,integerfield,floatfield,textfield


class Field(object):

    """docstring for Field"""

    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)


class StringField(Field):

    "docstring for StringField"

    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)


class BooleanField(Field):

    """docstring for BooleanField"""

    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)


class IntegerField(object):

    """docstring for IntegerField"""

    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)


class FloatField(Field):

    """docstring for FloatField"""

    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)


class TextField(Field):

    """docstring for TextField"""

    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)

# Model is a base class,by metaclass to 将具体子类映射信息读取出来
# 任何继承自Modelの类 会自动by modelMetaclass扫描映射关系 同时存储至自身类attr __table__ mappings__


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        tableName = attrs.get('__table__', None) or name
        logging.info('Found model: %s (table: %s)' % (name, tableName))
        mappings = dict()
        fields = []
        primaryKey = None
        for k, v in attrs.items():
            if isinstance(v, Field):
                logging.info('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
                if v.primary_key:
                    # find the primary_key StandardError
                    if primaryKey:
                        raise StandardError(
                            'Duplicate primary key for field: %s' % k)
                    primaryKey = k
                else:
                    fields.append(k)
        if not primaryKey:
            raise StandardError('Primary key not found.')
        for k in mappings.keys():
            attrs.pop(k)
        escaped_fields = list(map(lambda f: '`%s`' % f, fields))
        attrs['__mappings__'] = mappings  # save attrs and row's map relation
        attrs['__table__'] = tableName
        attrs['__primary_key__'] = primaryKey  # primarykey attrs name
        attrs['__fields__'] = fields  # escape primarykey's attrs name
        attrs['__select__'] = 'select `%s`,%s from `%s`' % (
            primaryKey, ', '.join(escaped_fields), tableName)
        attrs['__insert__'] = 'insert into `%s` (%s,`%s`) values (%s)' % (tableName, ', '.join(
            escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (tableName, ', '.join(
            map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (
            tableName, primaryKey)
        return type.__new__(cls, name, bases, attrs)

# define 所有ORM映射の基类Model
# Model 从dict继承（可使用所有dict功能） 同时实现特殊method __getattr__ and
# __setattr__,即,user['id']=user.id


class Model(dict, metaclass=ModelMetaclass):

    """docstring for Model"""

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(b"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = key

    def getValue(self, key):
        return getattr(self, key, None)

    def getValueOrdefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                value = field.default() if callable(
                    field.default) else field.default
                logging.debug('Using default value for %s: %s' %
                              (key, str(value)))
                setattr(self, key, value)
            return value

    @classmethod
    async def findAll(cls, where=None, args=None, **kw):
        'find object by where clause.'
        sql = [cls.__select__]
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        orderBy = kw.get('orderBy', None)
        if orderBy:
            sql.append('order by')
            sql.append(orderBy)
        limit = kw.get('limit', None)
        if limit is not None:
            sql.append('limit')
            if isinstance(limit, int):
                sql.append('?')
                sql.append(limit)
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append('?, ?')
                args.append(limit)
            else:
                raise ValueError('Invaild limit value: %s' % str(limit))
        rs = await select(' '.join(sql), args)
        return [cls(**r) for r in rs]

    @classmethod
    async def findNumber(cls, selectField, where=None, args=None):
        'find number by select and where'
        sql = ['select %s _num_ from `%s`' % (selectField, cls.__table__)]
        if where:
            sql.appen('where')
            sql.appen(where)
        rs = await select(' '.join(sql), args, 1)
        if len(rs) == 0:
            return None
        return rs[0]['_num_']

    @classmethod
    async def find(cls, pk):
        'find object by primary key.'
        rs = await select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])

    async def save(self):
        args = list(map(self.getValueOrdefault, self.__fields__))
        args.appen(self.getValueOrdefault(self.__primary_key__))
        rows = await execute(self.__insert__, args)
        if rows != 1:
            logging.warn('Failed to insert record: affected rows: %s' % rows)
    async def update(self):
        args = list(map(self.getValue, self.__fields__))
        args.append(self.getValueOrdefault(self.__primary_key__))
        rows = await execute(self.__update__, args)
        if rows != 1:
            logging.warn(
                'Failed to update by primary key: affected rows: %s' % rows)
    async def remove(self):
        args = [self.getValue(self.__primary_key__)]
        rows = await execute(self.__delete__, args)
        if rows != 1:
            logging.warn(
                'Failed to remove by primary key: affected rows: %s' % rows)
