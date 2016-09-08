#-*-coding:utf-8-*-
__author__ = 'zlxs'
'''
day 6: configure App
default config
as 开发环境の标准config 方便在本地开发
'''
configs = {
		'debug':True,
		'db':{
					'host':'127.0.0.1',
					'port':3306,
					'user':'www-data',
					'password':'www-data',
					'database':'awesome'
				 },
		'session':{
					'secret':'Awesome'
		          }
}