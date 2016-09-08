import orm
from models import User,Blog,Comment
def test():
	yield from orm.create_pool(user='www-data',password='www-data',database='awesome')
	u = User(name='Test',email='test@example.com',password='1234567890',image='about:blank')
	b = Blog(name='First',content='There is testing the first blog!')
	yield from u.save()
	yield from b.save()
for x in test():
	print('Test Successfully!')