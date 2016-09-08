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
2版数据获取出错, 将div.container 后第二个div.mt20 改为div
'''
def get_index(page_url, data=None):
    soup = get_web_data(page_url)
    titles = soup.select('body > div.div_body > div.container > div > div > div > ul > li > div > a')
    imgs = soup.select('body > div.div_body > div.container > div > div > div > ul > li > div > a > div > img')
    pnums = soup.select('body > div.div_body > div.container > div > div > div > ul > li > div > a > div > span')
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
        img_link.append("http://spider_exercise_bcy.net/image/full?type=coser&id=%s&url=%s" % (web_id,last_link))
    print(img_link, '\n', len(img_link))
    return img_link

def download_img(url, path, filename):
    if not os.path.exists(path):
        os.makedirs(path)
    r = requests.get(url)
    with open(path+'\/'+filename, 'wb') as file:
        file.write(r.content)

for url in urls:
    all_infos = get_index(url)
    for per_info in all_infos:
        img_url = get_img(per_info['link'])
        # 传说用的加号多了, 内存占用会变高, 但是这样改好像也是创建两次内存, 特加此注释, 以后再看
        # 等学会线程, 回来记得给下载上个多线程, 但是感觉图片太大, 可能会没什么效果
        # path = os.getcwd() + '\/' + str(info['title']).replace('/','&')
        path = os.getcwd()+'%s%s' % ('\/',str(per_info['title']).replace('/','&'))
        print(path)
        for per_img_url in img_url:
            filename = re.findall(r'\w+\.jpg', per_img_url)[0]
            print(filename)
            download_img(per_img_url, path, filename)
            print('done')

