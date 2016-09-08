# collections is python supply many useful set class
# p = (1,2)
# look this(1,2) can't watch out this tuple 是用来表示一个坐标的
#### nametuple ####
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
p.x
p.y
# nametupled是一个函数用来创建自定义的tuple对象 且规定其元素个数
# 可以用属性而不是通过索引来引用tuple某个元素
# created  Point object is tuple の子类
# print(p.x)
# print(p.y)
#print(isinstance(p, Point))
# namedtple('name',[attr_list])
# 若用坐标and半径表示一个圆 亦可用之定义
Circle = namedtuple('Circle', ['x', 'y', 'r'])
#### deque ####
# 使用list存储data时 按索引访问元素很快 butinsert and delete 元素就很慢
# becauselist is linear 存储 data 量很大时 其效率很低
# deque is to 高校实现insert and delete操作 双向列表 适合于queue and stack
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
# deque 可实现list的append and pop 还支持appendleft and popleft
#### defaultdict ####
# 使用dict时 若是应用key不存在 则会抛出keyerror if 希望key不存在时 返回一个默认的值
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
dd['key1']  # key1 exist
dd['key2']  # key2 is't exist return default value
# default value is 调用fun返回的，而函数在创建defaultdice对象时传入 即匿名函数
#### OrderDict ####
# 使用dict时 ,key is 无序的 so 对dict做 迭代 时 我们无法确定key的顺序
# 若要保持key的顺序 则可用OrderDict
from collections import OrderedDict
do = dict([('a', 1), ('b', 2), ('c', 3)])
do  # dict's key is 无序的
doo = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
doo  # OrderDict's key is有序的
# OrderDict's key 按照insert 的顺序排列 不是key本身 进行排序
# by OrderDict 实现 FIFO 队列 dict （当容量超出限制时 先删除最早添加的key）
from collections import OrderedDict


class LastUpdatedOrderedDict(OrderedDict):

    """docstring for LastUpdatedOrderedDict"""

    def __init__(self, first):
        super(LastUpdatedOrderedDict, self).__init__()
        self.first = first  # queue's first

    def __setitem__(self, key, value):
        containKey = 1 if key in self else 0
        if len(self) - containKey >= self._first:
            last = self .popitem(last=False)
            print('remove:', last)
        if containKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(slef, key, value)
#### Counter ####
# Counter is a easy 计数器 eg:统计字符出现的个数
from collections import Counter
c = Counter()
for char in 'programmemmaa':
    c[char] = c[char] + 1
# Counter in fact is a dict's 子类
# collections module give some useful set class
