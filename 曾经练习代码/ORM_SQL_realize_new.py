# 编写一个ORM框架
# 2 定义Field类 负责保存DB的字段名和字段类型
class Field(object):
    def __init__(self,name,column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s : %s>' % (self.__class__.__name__,self.name)
# 2.1基于Field类进一步定义StrinField
class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')
# 2.2基于Field类进一步定义IntegerField
class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')
# 3 创建元类（模型）ModelMetaclass
class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name == 'Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found model: %s ' % name)
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping: %s ==> %s' % (k,v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__table__'] = name # 假设表名与类名一致
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        return type.__new__(cls,name,bases,attrs)
# 4 创建基类Model
class Model(dict,metaclass = ModelMetaclass):
    __metaclass__ = ModelMetaclass
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r'''Model'object has no attribute '%s''' % key)
    def __setattr__(self,key,value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__,','.join(fields),','.join(params))
        print('SQL:%s' % sql)
        print('ARGS:%s' % str(args))
# 1 调用接口 定义个User类来操作对应的DBUser
'''
父类 Model 和属性类型 StringField、 IntegerField 是由 ORM 框架提供的，
方法比如 save()全部由 metaclass 自动完成
'''
class User(Model):
    # 定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
# 创建一个实例
u = User(id = 12345,name = 'ma',email = 'test@orm,oeg',password = 'my-pwd')
# 保存到DB
u.save()
'''
当用户定义一个 class User(Model)时， Python 解释器首先在当前类 User 的定义中查找
__metaclass__，如果没有找到，就继续在父类 Model 中查找__metaclass__，找到了，就使用
Model 中定义的__metaclass__的 ModelMetaclass 来创建 User 类，也就是说， metaclass 可以
隐式地继承到子类，但子类自己却感觉不到。
在 ModelMetaclass 中，一共做了几件事情：
排除掉对 Model 类的修改；
在当前类（比如 User）中查找定义的类的所有属性，如果找到一个 Field 属性，就把它保存
到一个__mappings__的 dict 中，同时从类属性中删除该 Field 属性，否则，容易造成运行时
错误；
把表名保存到__table__中，这里简化为表名默认为类名。
在 Model 类中，就可以定义各种操作数据库的方法，比如 save()， delete()， find()， update
等等。
我们实现了 save()方法，把一个实例保存到数据库中。因为有表名，属性到字段的映射和属
性值的集合，就可以构造出 INSERT 语句。
'''