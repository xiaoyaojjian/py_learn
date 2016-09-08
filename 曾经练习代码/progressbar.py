import sys
import time
#http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=402334431&idx=2&sn=d61d367aceb18e5590bcb52426736e2e&3rd=MzA3MDU4NTYzMw==&scene=6#rd

class ProgressBar:

    def __init__(self, count=0, total=0, width=50):
        self.count = count
        self.total = total
        self.width = width

    def move(self):
        self.count += 1

    def log(self, s):
        sys.stdout.write(' ' * (self.width + 9) + '\r')
        sys.stdout.flush()
        print(s)
        progress = int(self.width * self.count / self.total)
        sys.stdout.write('{0:3}/{1:3}: '.format(self.count, self.total))
        sys.stdout.write('#' * progress + '-' * (self.width - progress) + '\r')
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()

bar = ProgressBar(total=10)
for i in range(10):
    bar.move()
    bar.log('We have arrived at: ' + str(i + 1))
    time.sleep(1)