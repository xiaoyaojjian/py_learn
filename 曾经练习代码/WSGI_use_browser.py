# Web
# Browser send a HTTP request
# Server receivew this request,product a HTML documnet
# Server send this HTML docment to Browser ass HTTP response の Body
# Browser sent this HTTP response,take this HTML docment and print from HTTP Body
# WSGI: Web Server Gateway Interface


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, web!</h1></br><h2>Hello,%s !</h2>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
# environ: include all HTTP request info dict object
# start_response: send HTTP response function
