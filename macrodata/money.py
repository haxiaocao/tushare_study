# -*- coding:UTF-8 -*-
import tushare as ts
import pymongo
import json

db = "MacroData"
coll = "MoneySupply"

conn = pymongo.MongoClient('127.0.0.1', port=27017)
df = ts.get_money_supply()
# index data columns(X columns)
dicIndex = json.loads(df.to_json(orient='split'))
for i, ind in enumerate(dicIndex['index']):
    d = dicIndex['data'][i][0]
    jsonstr = {
        '_id':  d,
        dicIndex['columns'][0]: d,
        dicIndex['columns'][1]: dicIndex['data'][i][1],
        dicIndex['columns'][2]: dicIndex['data'][i][2],
        dicIndex['columns'][3]: dicIndex['data'][i][3],
        dicIndex['columns'][4]: dicIndex['data'][i][4],
        dicIndex['columns'][5]: dicIndex['data'][i][5],
        dicIndex['columns'][6]: dicIndex['data'][i][6],
        dicIndex['columns'][7]: dicIndex['data'][i][7],
        dicIndex['columns'][8]: dicIndex['data'][i][8],
        dicIndex['columns'][9]: dicIndex['data'][i][9],
        dicIndex['columns'][10]: dicIndex['data'][i][10],
        dicIndex['columns'][11]: dicIndex['data'][i][11],
        dicIndex['columns'][12]: dicIndex['data'][i][12],
        dicIndex['columns'][13]: dicIndex['data'][i][13],
        dicIndex['columns'][14]: dicIndex['data'][i][14],
        dicIndex['columns'][15]: dicIndex['data'][i][15],
        dicIndex['columns'][16]: dicIndex['data'][i][16]
    }
    try:
        conn[db][coll].insert(jsonstr)
    except:
        pass
