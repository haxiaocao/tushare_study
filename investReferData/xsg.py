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
coll = "XSG_jiejin"
year = 2017
month = 12

conn = pymongo.MongoClient('127.0.0.1', port=27017)
df = ts.xsg_data()
# index data columns(X columns)
dicIndex = json.loads(df.to_json(orient='split'))
for i, ind in enumerate(dicIndex['index']):
    jsonstr = {
        '_id':  dicIndex['data'][i][2] + "-" + dicIndex['data'][i][0],
        'year': year,
        'month': month,
        dicIndex['columns'][0]: dicIndex['data'][i][0],
        dicIndex['columns'][1]: dicIndex['data'][i][1],
        dicIndex['columns'][2]: dicIndex['data'][i][2],
        dicIndex['columns'][3]: dicIndex['data'][i][3],
        dicIndex['columns'][4]: dicIndex['data'][i][4]
    }
    try:
        conn[db][coll].insert(jsonstr)
    except:
        pass
