# -*- coding:UTF-8 -*-
import tushare as ts
import pymongo
import json

db = "ClassifiedStock"
coll = "HS300"

conn = pymongo.MongoClient('127.0.0.1', port=27017)
# it is not right and you should find other ways to complete it.
df = ts.get_hs300s()
# index data columns(X columns)
dicIndex = json.loads(df.to_json(orient='split'))
for i, ind in enumerate(dicIndex['index']):
    d = dicIndex['data'][i][0]
    jsonstr = {
        '_id':  d,
        dicIndex['columns'][0]: d,
        dicIndex['columns'][1]: dicIndex['data'][i][1],
        dicIndex['columns'][2]: dicIndex['data'][i][2],
        dicIndex['columns'][3]: dicIndex['data'][i][3]
    }
    try:
        conn[db][coll].insert(jsonstr)
    except:
        pass
