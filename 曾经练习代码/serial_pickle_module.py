# _*_coding:utf-8_*_
# pickling 浸封 == serialization 序列化
d = dict(name='bob', age=30, score=99)
# 可随时修改变量，Eg：将name改成bill，但是一旦程序结束，变量所占用的内存被操作系统全部回收
# 若没有把修改后的bill存储到磁盘上，下次重新运行，变量又被初始化为bob
# 将 变量从内存中变成可存储或传输的过程 ==》serialization
# Python：pickling 浸封 用盐腌制
# 序列化后，将序列化的内容吸入磁盘，或通过网络传输到别的机器上
# 将变量内容从序列化的对象重新读入内存里称为反序列化 即unpinkling
# 利用pickle模块
import pickle
# pickling
pickle.dumps(d)
# pickle.dumps()方法将任意对象序列化为一个bytes后，将这个bytes写入文件
# 利用pickle.dump()方法把对象序列化后写入一个file-like Object
f = open('dump_test.txt', 'wb')
pickle.dump(d, f)
f.close()
# 此时dump.test.txt文件本身出现 乱七八糟的内容-是Python保存的对象内部信息
# unpickling
f1 = open('dump_test.txt', 'rb')
d1 = pickle.load(f1)
f1.close()
# 此时d1可以将dump.test.txt文件内容读出来，d1=d 变量内容有回来了
# 但d1与d变量完全不相干，独立对象，只是内容相同
'''
pickle仅仅适用于Python自己，甚至不同版本Python都不能兼容，只能用pickle保存不重要的内容信息，有可能不能反序列化
若是需要在不同编程语言中传递对象，则需要将对象序列化为标准化格式eg XML
最好方式是将至序列化为JSON 他表示一个字符串，可以被所有语言读取，
也可以方便存储到磁盘或者通过网络传输
JSON不仅是标准格式，且比XML快，且可直接在WEB中读取
'''
##############json与Python类型对应###################
'''
json tye----------------------------------python type
   {} 									   										dict
   []                                         list
   "string"                                   str
   123.45                                     int/float
   true/false                                 True/False
   null                                       None
'''
#####################################################
# Python内置json模块提供网上Python对象到JSON格式转换
import json
# 此时d是一个dict
json.dumps(d)
# dumps方法返回一个str，内容就是标准的JSON
# 类似的dump方法可直接把JSON写入一个file-like Object
# 要将JSON反序列化为Python 用loads方法-将JSON字符串反序列化
# load()方法从file-likeObject中读取并将之反序列化
# json标准规定JSON编码是UTF-8---Python(str)<-->JSON(string)
#####################################################
# 使用class表示对象并将之序列化


class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('bbb', 20, 33)
# try:print(json.dumps(s))
# 从dumps函数中可选参数default即将任意一个对象变成一个可序列化为JSON对象
# 为Student专门转换函数


def student2dict(std):
    return{
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
# 将line 61中的typeerror利用上述student2dict函数转换成dict 再顺利序列化为JSON
print('利用student2dict函数转换使student实例可序列化：\n',
      json.dumps(s, default=student2dict))
# 为了将转换函数广泛化，偷懒：
# 利用class实例中__dict__属性（this is a Dict） 课用来存储实例变量
# 除了定义了__slosts__的class
print('偷懒化序列化:\n',json.dumps(s, default=lambda obj: obj.__dict__))
# 结合student2dict函数，同理 反序列化
json_str = '{"score": 99, "name": "bob", "age": 30}'


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
s = json.loads(json_str, object_hook=dict2student)
print('利用dict2student函数转换实现反序列化:\n',s.name,s.age,s.score)
# 打印出来即是反序列化后的student实例对象
#print('偷懒化序列化:\n',json.loads(json_str,object_hook=lambda ))
