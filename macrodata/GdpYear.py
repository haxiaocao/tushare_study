# -*- coding:UTF-8 -*-
import tushare as ts
import pymongo
import json

#    ts.get_cash_flow : get specialed Code Cash_flow in the History .

db = "MacroData"
coll = "GdpYear"

conn = pymongo.MongoClient('127.0.0.1', port=27017)
df = ts.get_gdp_year()
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
        dicIndex['columns'][10]: dicIndex['data'][i][10]
    }
    try:
        conn[db][coll].insert(jsonstr)
    except:
        pass
