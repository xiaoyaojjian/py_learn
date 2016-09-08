# -*- coding:utf-8 -*-
import requests
import os
import re
import time

t1 = time.time()


def get_items(response):
    # 获取专辑信息
    items = re.findall('<div class="item">(.*?)</div>', response, re.S)
    special = 1
    music_num = 0
    for item in items:
        special_name = re.search('class="name" title=".*?">(.*?)</a>', item, re.S)
        if special_name:
            special_name = special_name.group(1).decode('utf-8')
        else:
            break
        special_link = re.search('<a href="(.*?)" class="cover-wrapper".*?>', item, re.S)
        if special_link:
            special_link = special_link.group(1).decode('utf-8')
        print u'----------开始下载 %s ----------' % special_name

        try:
            file_name = u'D:\\LW_music\\%s' % special_name

            # 判断是否存在专辑文件夹，不存在则创建
            if not os.path.exists(file_name):
                os.mkdir(file_name)

            # 获取专辑海报，并保存
            special_picture = re.search(
                '<a href=".*?" class="cover-wrapper" title=".*?">.*?<img src="(.*?).image.*?" alt=".*?" class=".*?">',
                item,
                re.S)
            if special_picture:
                special_picture = special_picture.group(1).decode('utf-8')
            image = requests.get(special_picture).content
            try:
                picture = file(file_name + '\\%s.jpg' % special_name, 'wb')
            except IOError as e:
                print e
                picture = file(file_name + '\\special.jpg', 'wb')
            picture.write(image)
            picture.close()

        except (IOError, WindowsError) as e:
            file_name = u'D:\\LW_music\\%d' % (special + 1 )
            print e
            # 判断是否存在专辑文件夹，不存在则创建
            if not os.path.exists(file_name):
                os.mkdir(file_name)

            # 获取专辑海报，并保存
            special_picture = re.search(
                '<a href=".*?" class="cover-wrapper" title=".*?">.*?<img src="(.*?).image.*?" alt=".*?" class=".*?">',
                item,
                re.S)
            if special_picture:
                special_picture = special_picture.group(1).decode('utf-8')
            image = requests.get(special_picture).content
            try:
                picture = file(file_name + '\\%s.jpg' % special_name, 'wb')
            except IOError as e:
                print e
                picture = file(file_name + '\\special.jpg', 'wb')
            picture.write(image)
            picture.close()

        music_num += get_music(special_name, special_link, file_name)
    special += 1
    return music_num, special


def get_music(special_name, special_link, file_name):
    # 获取歌曲信息，并下载
    i = 1
    music_page = requests.get(special_link).content

    # 写入专辑简介
    intro = re.search('<div class="vol-desc">(.*?)</div>', music_page, re.S)
    if intro:
        intro = intro.group(1)
    intro_alter = re.sub('<br>', '\n', intro, re.S)
    try:
        intro_text = file(file_name + '\\%s.txt' % special_name, 'w+')
    except IOError as e:
        print e
        intro_text = file(file_name + '\\special.txt', 'w+')
    intro_text.write(intro_alter)
    intro_text.close()

    song_list = re.findall('<li class=".*?>(.*?)</li>', music_page, re.S)
    for music in song_list:
        # 获取歌曲名
        song_name = re.search('class="trackname btn-play">(.*?)</a>', music, re.S)
        if song_name:
            song_name = song_name.group(1).decode('utf-8')

        # 获取歌手名
        artist = re.search('class="artist btn-play">(.*?)</span>', music, re.S)
        if artist:
            artist = artist.group(1).decode('utf-8')

        # 获取专辑序号，构建歌曲 url
        special_num = re.search('vol.(\d+)', special_name, re.S)
        if special_num:
            special_num = special_num.group(1).decode('utf-8')
        else:
            break
        # 获取歌曲序号，构建歌曲 url
        song_num = re.search('(\d+).', song_name, re.S)
        if song_num:
            song_num = song_num.group(1).decode('utf-8')
        else:
            break
        # 构建歌曲 url
        song_url = 'http://luoo-mp3.kssws.ks-cdn.com/low/luoo/radio%s/%s.mp3' % (special_num, song_num)

        # 下载歌曲，并保存
        print u'----------正在下载 %s--%s----------' % (special_name, song_name)
        song = requests.get(song_url).content
        try:
            f = file(file_name + '\\%s-%s.mp3' % (song_name, artist), 'wb')
        except IOError as e:
            print e
            f = file(file_name + '\\%s-%s.mp3' % (special_num, song_num), 'wb')
            print u'----------音乐名写入失败----------'
        f.write(song)
        f.close()
        if i % 10 == 0:
            time.sleep(0.5)
        i += 1
    return i


def get_resp(url):
    user = 'http://www.luoo.net/event/local'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 UBrowser/5.6.11815.13 Safari/537.36'}

    request = requests.Session()
    request.get(user, headers=header)
    response = request.get(url, headers=header).content
    return response


if not os.path.exists('D:\\LW_music'):
    os.mkdir('D:\\LW_music')

start = int(raw_input(u'请输入开始爬取页数：'))
end = int(raw_input(u'请输入结束页数：'))
total_special_num = 0
total_music_num = 0
page = start
while True:
    url = 'http://www.luoo.net/tag/?p=%d' % page
    response = get_resp(url)
    per_page_total_music, per_page_special_num = get_items(response)
    total_music_num += per_page_total_music
    total_special_num += per_page_special_num

    page += 1
    if page == end + 1:
        break
t2 = time.time()
t = t2 - t1

print u'----------程序结束，共下载%d张专辑%d首歌曲--用时 %d 秒----------' % (total_special_num, total_music_num, t)
