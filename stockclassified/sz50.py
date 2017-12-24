# -*- coding:UTF-8 -*-
import tushare as ts
import pymongo
import json

db = "ClassifiedStock"
coll = "SZ50"

conn = pymongo.MongoClient('127.0.0.1', port=27017)
# note: this is not working currently .So you should find other ways to get it done.
df = ts.get_sz50s()
# index data columns(X columns)
dicIndex = json.loads(df.to_json(orient='split'))
for i, ind in enumerate(dicIndex['index']):
    d = dicIndex['data'][i][0]
    jsonstr = {
        '_id':  d,
        dicIndex['columns'][0]: d,
        dicIndex['columns'][1]: dicIndex['data'][i][1]
    }
    try:
        conn[db][coll].insert(jsonstr)
    except:
        pass
