# -*- coding:UTF-8 -*-
import tushare as ts
import pymongo
import json

#    ts.get_cash_flow : get specialed Code Cash_flow in the History .
# 600547:山东黄金
# 600362:江西铜业
# 600312:平高电气
# 600499：科达洁能
# 603993：洛阳钼业
db = "StockBasics"
coll = "AllStocks"

conn = pymongo.MongoClient('127.0.0.1', port=27017)
df = ts.get_stock_basics()
# index data columns(X columns)
dicIndex = json.loads(df.to_json(orient='split'))
for i, ind in enumerate(dicIndex['index']):
    jsonstr = {
        '_id':  dicIndex['data'][i][0],
        dicIndex['columns'][0]: dicIndex['data'][i][0],
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
        dicIndex['columns'][16]: dicIndex['data'][i][16],
        dicIndex['columns'][17]: dicIndex['data'][i][17],
        dicIndex['columns'][18]: dicIndex['data'][i][18],
        dicIndex['columns'][19]: dicIndex['data'][i][19],
        dicIndex['columns'][20]: dicIndex['data'][i][20],
        dicIndex['columns'][21]: dicIndex['data'][i][21],
    }
    try:
        conn[db][coll].insert(jsonstr)
    except:
        pass
