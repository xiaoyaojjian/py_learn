'''
从半次元的喜欢页面下载所有喜欢作品的高清图, 保存在当前目录下以页面标题为文件夹名
'''

from bs4 import BeautifulSoup
import requests, time, re, os
from urllib import request

'''
download the favorite page's data
'''
# page = input("link: ")
page = 'http://spider_exercise_bcy.net/u/856501/like/cos'
index_data = BeautifulSoup(requests.get(page).text, 'lxml')
bottom = index_data.select('body > div.div_body > div.container > div > div.l-home-follow-pager > ul > li')
if len(bottom) == 0:
    urls = [page]
else:
    urls = ['http://spider_exercise_bcy.net/u/856501/like/cos?&p={}'.format(i) for i in range(1,len(bottom)-4)]
print(urls)
header = {
    'User-Agent' : '',
    'Cookie' : ''
}

def get_web_data(url):
    web_data = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(web_data.text, 'lxml')
    return soup
'''
get all favorite data
'''
def get_index(url, data=None):
    soup = get_web_data(url)
    titles = soup.select('body > div.div_body > div.container > div > div.mt20 > div > ul > li > div > a')
    imgs = soup.select('body > div.div_body > div.container > div > div.mt20 > div > ul > li > div > a > div > img')
    pnums = soup.select('body > div.div_body > div.container > div > div.mt20 > div > ul > li > div > a > div > span')
    if data == None:
        infos = []
        for title, img, pnum in zip(titles, imgs, pnums):
            data = {
                'title' : title.get('title'),
                'img' : img.get('src'),
                'pnum' : pnum.get_text(),
                'link' : 'http://spider_exercise_bcy.net'+title.get('href')
            }
            infos.append(data)
    return infos

def get_img(url):
    img_link = []
    imgs = get_web_data(url).select('div > img[src*="http"] ')
    web_id = re.findall(r'[0-9]+', url)[1]
    for img in imgs:
        last_link = re.findall(r'.*jpg', img.get('src'))[0]
        img_link.append("http://spider_exercise_bcy.net/image/full?type=coser&id=%s&url=" % web_id +last_link)
    print(img_link, '\n', len(img_link))
    return img_link

def download_img(url, path, filename):
    if not os.path.exists(path):
        os.makedirs(path)
    r = requests.get(url)
    with open(path+'\/'+filename, 'wb') as file:
        file.write(r.content)

for url in urls:
    infos = get_index(url)
    for info in infos:
        url = get_img(info['link'])
        path = os.getcwd() + '\/' + str(info['title']).replace('/','&')
        print(path)
        for url in url:
            filename = re.findall(r'\w+\.jpg', url)[0]
            print(filename)
            download_img(url, path, filename)
            print('done')

