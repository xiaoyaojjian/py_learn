"""
有序 dict
"""

import collections
dic = collections.OrderedDict()

dic['k1'] = 'v1'
dic['k2'] = None

dic.setdefault('k2', '666')
dic.setdefault('k3', 'v3')

print(dic)
