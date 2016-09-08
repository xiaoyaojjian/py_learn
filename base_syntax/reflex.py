"""
反射
"""

tmp = 'sys'
func = 'path'

# 通过字符串导入模块
sys = __import__(tmp)
print(sys)
# 通过字符串获取模块内容
path = getattr(sys, func)
print(path)


# 应用
instr = str(input('Please input model/function:')).split('.')
print(instr)
module = __import__(instr[0])
func = getattr(module, instr[1])
print(func)
