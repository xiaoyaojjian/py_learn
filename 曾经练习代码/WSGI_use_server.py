# _*_coding:utf-8 _*_
# server.py
# from wsgiref module import
from wsgiref.simple_server import make_server
# from our application
from WSGI_use_browser import application
# create a server IP is empty port is 8000 handle fun is application
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# start to listen HTTP request
httpd.serve_forever()
