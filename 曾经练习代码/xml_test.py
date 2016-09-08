# parse is 解析 剖析
# 这里解析是指读取或者时让人理解XmL所代表の
# 在这里对XML进行操作
from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):

    def start_element(slef, name, attrs):
        print('sax : start_element : %s, attrs : %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax : end_element : %s' % name)

    def char_data(self, text):
        print('sax : char_data : %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
		<li><a href="/python">Python</a></li>
		<li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
# 读取一大段字符串CharacterDataHandler可能被多吃调用 so 需要自己保存 在EndElementHandler里面进行合并
# 生成XML---拼接字符串
'''
	L = []
	L.append(r'<?xml version="1?>')
	L.append(r'<root>')
	L.append(encode('some & data'))
	L.append(r'</root>')
	return ''.join(L)
'''
# if want complex XML --->>JSON
# parse XML find 自己感兴趣的节点 响应事件时，将节点数据保存起来 解析完毕后，就可处理数据
#######################
# parameter w is city code.if select one city code explorer URL is it
from xml.parsers.expat import ParserCreate
from datetime import datetime, timedelta


class WeatherSaxHandler(object):

    """docstring for WeatherSaxHandler"""

    def __init__(self):
        self._weather = {}

    def start_element_w(self, name, attrs):
        if name == 'yweather : location':
            self._weather['city'] = attrs['city']
            self._weather['country'] = attrs['country']
        elif name == 'yweather : condition':
            self._weather['condition'] = attrs
        elif name == 'yweather : forecast':
            self._weather[attrs['date']] = attrs

    def end_element_w(self, name):
        pass

    def char_data_w(self, text):
        pass

    def parse_weather(data):
        handler = WeatherSaxHandler()
        parser = ParserCreate()
        parser.StartElementHandler = handler.start_element_w
        parser.EndElementHandler = handler.end_element_w
        parser.CharacterDataHandler = handler.char_data_w
        parser.Parse(data)

        Dweather = {}
        Dweather['today'] = {}
        Dweather['tomorrow'] = {}

        condition = handler._weather['condition'][
            'date'].split(',')[1].strip().split(' ')
        today = condition[0] + ' ' + condition[1] + ' ' + condition[2]
        tomorrow = datetime.strptime(today, '%d %b %Y') + timedelta(days=1)

        Dweather['city'] = handler._weather['city']
        Dweather['country'] = handler._weather['country']
        Dweather['today']['text'] = handler._weather[today]['text']
        Dweather['today']['low'] = handler._weather[today]['low']
        Dweather['today']['high'] = handler._weather[today]['high']
        Dweather['tomorrow']['text'] = handler._weather[
            tomorrow.strftime('%d %b %Y')]['text']
        Dweather['tomorrow']['low'] = handler._weather[
            tomorrow.strftime('%d %b %Y')]['low']
        Dweather['tomorrow']['high'] = handler._weather[
            tomorrow.strftime('%d %b %Y')]['high']

        return Dweather


'''
    def parse_weather(xml):
        return{
            'city': 'Beijing',
            'country': 'China',
            'today': {
                'text': 'Partly Cloudy',
                'low': 20,
                'high': 33
            },
            'tomorrow':
            {
                'text': 'Sunny',
                'low': 21,
                'high', 34
            }
        }
'''
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(data)
'''

weather = parse_weather(data)
assert weather['city'] == 'Beijing', weather['city']
assert weather['country'] == 'China', weather['country']
assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
assert weather['today']['low'] == 20, weather['today']['low']
assert weather['today']['high'] == 33, weather['today']['high']
assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
assert weather['tomorrow']['low'] == 21, weather['tomorrow']['low']
assert weather['tomorrow']['high'] == 34, weather['tomorrow']['high']
print('Weather:', str(weather))


data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''