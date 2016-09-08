'''
178资讯爬取练习
'''

from bs4 import BeautifulSoup
import requests, time

url = 'http://acg.178.com/'
header = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Cookie' : 'bdshare_firstime=1443864896869; _sid=d5bebe9a57fddd93a379ae3b2d0380da7c7f07d2; _l=1443867880; _178c=37301261%23%23shiinamayuri; _e=31536000; CNZZDATA30044031=cnzz_eid%3D2067382496-1443859599-http%253A%252F%252Fwww.178.com%252F%26ntime%3D1446728647; CNZZDATA30039253=cnzz_eid%3D2032988550-1443862791-http%253A%252F%252Fwww.178.com%252F%26ntime%3D1446730799; _i=M79W2nIPUjFGCoc6QRpCR153nhlKUzinCngUxDUWGOLRyNMCcrAUAkHg317Zt%2BpJ_0d2856ad489ba29a4c83b21585c05e36_1456751067; __wmbgid=2wkfbxp6pol446annrp5ztfiany4xm49; __wmbsid=o3n8yefnl4rsyu4z'
}

web_data = requests.get(url, headers=header)
time.sleep(1)
soup = BeautifulSoup(web_data.text, 'lxml')


# titles = soup.select('body > div > div.wrapper.ie6png > div.container > div.left > div > div.newspic')
contents = soup.select('body > div > div.wrapper.ie6png > div.container > div.left > div > div.newstext.text_i')
imgs = soup.select('body > div.bg > div.wrapper.ie6png > div.container > div.left > div > div.newspic > a > img')
tags = soup.select('body > div.bg > div.wrapper.ie6png > div.container > div.left > div > div.title_data > span.float_right')
# print(titles, '\n', contents, '\n', imgs)




for content, img, tag in zip(contents, imgs, tags):
    data = {
        'title' : img.get('alt'),
        'img' : img.get('src'),
        'content' : content.get_text(),
        'tag' : list(tag.stripped_strings)
    }
    print(data)
