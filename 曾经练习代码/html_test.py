# 利用HTMLParser来解析HTML---->获得页面后解析该页面
from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('<%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s' % name)

    def handle_charref(self, name):
        print('&%s' % name)
parser = MyHTMLParser()
parser.feed('''<html>
	<head></head>
	<body>
	<!-- test html parser -->
				<p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
	</body></html>''')
# feed()方法可以多次调用
# 不一定一次就就把整个HTML字符串都塞进去，可一部分一部分传输进去
# 特殊字符：英文表示:&nbsp; 数字表示:&#1234 皆可通过Parser解析出来
