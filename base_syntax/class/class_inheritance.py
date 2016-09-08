# 类的继承

class Hk(object):
    def __init__(self, name):
        self.name = name
        print('Hk')

    def show(self):
        print('show', self.name)


class Jk(Hk):
    def __init__(self, name):
        print('Jk')
        super().__init__(name)


ad = Jk('shiina')
ad.show()



# 两种继承的写法

class Base(object):
    def __init__(self):
        print("Base created")

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()

kid = ChildB()
