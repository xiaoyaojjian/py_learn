"""
读取文件内容, 将行号,内容,字数写入mongodb
"""

import pymongo

client = pymongo.MongoClient('localhost', 27017)
daba = client['daba']
user_tab = daba['user_tab']

path = './info.txt'
with open(path) as f:
    for index, line in enumerate(f):

        data = {
            'index': index,
            'line': line,
            'words': len(line)
        }
        user_tab.insert(data)

