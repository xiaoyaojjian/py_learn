"""
异常处理, try exception
"""

try:
    instr = str(input('Please input model.function:')).split('.')
    print(instr)
    module = __import__(instr[0])
    func = getattr(module, instr[1])
    print(func)
except Exception:
    print('Invalid input')
else:
    print('没有出错时, 将会执行else')
finally:
    print('无论是否成功执行, 都会执行finally')