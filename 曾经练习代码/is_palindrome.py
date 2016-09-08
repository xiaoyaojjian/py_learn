#回文数0...9,11...99,
#用filter筛选掉非回文数
#判断回文数函数
#先将整型数转换成字符
#list(str(ints)),len(list(str(ints))
#对称地判断两端是否相等
def is_palindrome(ints):
    numlist = list(str(ints))
    length = len(numlist)
    i = 0
    '''
    while i<=length/2:
        if numlist[i:] != numlist[-i:]:
            i=i+1
            
            return False
        else:
            break
        return True

    while numlist[i:i+1] == numlist[-i-1:-i]:
        print(numlist[i:i+1])
        i=i+1
        return True
        break
    return False
#回文数0...9,11...99,
#用filter筛选掉非回文数
#判断回文数函数
#先将整型数转换成字符
#list(str(ints)),len(list(str(ints))
#对称地判断两端是否相等
def is_palindrome(ints):
    numlist = list(str(ints))
    length = len(numlist)
    i = 0
    while i<=length:
        if numlist[i:] == numlist[-i:]:
            i=i+1
            return True
        else:
            break
            return False
    for i in numlist[i]:
        if numlist[i:] == numlist[-i:]:
             return True
        else:break
    while numlist[i:] == numlist[-i:]:
        i=i+1
        return True
        break
        return False
'''
