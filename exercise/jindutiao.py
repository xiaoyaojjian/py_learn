"""
进度打印
"""

import sys
import time

for i in range(101):
    sys.stdout.write('   \r')
    # sys.stdout.flush()
    sys.stdout.write('%s%s\r' % (i, '%'))
    sys.stdout.flush()
    time.sleep(0.01)

for i in range(101):
    sys.stdout.write('\r')
    # sys.stdout.flush()
    sys.stdout.write('loading:  [%s%s]' % ('#'*int(i/5), ' '*(20 - int(i/5))))
    sys.stdout.flush()
    time.sleep(0.01)