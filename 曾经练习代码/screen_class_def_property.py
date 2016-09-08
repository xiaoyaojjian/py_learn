#给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width = value
    @property 
    def height(self):
        return self._height
    @height.setter
    def  height(self,value):
        self._height = value
    @property 
    def resolution(self):
        print('%s X %s' % (self._width,self._height))
'''
用width,height既能起到 设置，又能起到 调用 的作用呢？既然两个方面都要起作用，
那么在class类中写这两个函数时不就是 重名 了吗？如果我们能 解决函数名重名 的问题就可以了，
所以增加了这个装饰@property和@score.setter，有了装饰，即使重名了，系统也能区分一个是接受的，一个是返回的
装饰器目的是 《解决函数重名》
'''
