#enumeration枚举类
##为枚举类型定义class 类型 把每个常量作为class 唯一实例
from enum import Enum,unique
Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Aug','Sep','Oct','Nov','Dec'))
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)
@unique #help 检查保证没有重复值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
