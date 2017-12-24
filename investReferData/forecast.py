# -*- coding:UTF-8 -*-
import tushare as ts
import pymongo
import json

# 600547:山东黄金
# 600362:江西铜业
# 600312:平高电气
# 600499：科达洁能
# 603993：洛阳钼业
db = "InvestInfos"
coll = "Forecast"
year = 2017
quart = 1

conn = pymongo.MongoClient('127.0.0.1', port=27017)
df = ts.forecast_data(year, quart)
# index data columns(X columns)
dicIndex = json.loads(df.to_json(orient='split'))
for i, ind in enumerate(dicIndex['index']):
    jsonstr = {
        '_id':  dicIndex['data'][i][0] + "-" + str(year) + "-" + str(quart),
        'year': year,
        'quart': quart,
        dicIndex['columns'][0]: dicIndex['data'][i][0],
        dicIndex['columns'][1]: dicIndex['data'][i][1],
        dicIndex['columns'][2]: dicIndex['data'][i][2],
        dicIndex['columns'][3]: dicIndex['data'][i][3],
        dicIndex['columns'][4]: dicIndex['data'][i][4],
        dicIndex['columns'][5]: dicIndex['data'][i][5]
    }
    try:
        conn[db][coll].insert(jsonstr)
    except:
        pass
