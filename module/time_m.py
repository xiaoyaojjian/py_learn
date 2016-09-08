import time, datetime


t = datetime.datetime.fromtimestamp(float('1463470722'))
tt = time.localtime(float('1463470722'))

print(time.strftime('%Y-%m-%d %H:%M:%S', tt))

print('time model'.center(40,'*'))
print(time.ctime())

print(time.strftime("%Y-%m-%d", time.gmtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()))
print(time.gmtime(time.time()))
time.sleep(0.1)

print('datatime model'.center(40,'*'))
print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.datetime.utcnow())
print(time.time())
print(datetime.datetime.fromtimestamp(time.time()))