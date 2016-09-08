import pymongo

client = pymongo.MongoClient('localhost', 27017)
daba = client['daba']
user_tab = daba['user_tab']

# 取出空行
for item in user_tab.find({'words': 1}):
    print(item)
# 取出非空行
for item in user_tab.find({'words': {'$ne': 1}}):
    print(item)
