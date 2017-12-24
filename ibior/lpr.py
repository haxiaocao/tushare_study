# -*- coding:UTF-8 -*-
import tushare as ts
import pymongo
import json
import pandas as pd

#    ts.get_cash_flow : get specialed Code Cash_flow in the History .
# 600547:山东黄金
# 600362:江西铜业
# 600312:平高电气
# 600499：科达洁能
# 603993：洛阳钼业
db = "Shibor"
coll = "Shibor_LPR"
year = 2016

conn = pymongo.MongoClient('127.0.0.1', port=27017)
df = ts.lpr_data(year)
# index data columns(X columns)
dicIndex = json.loads(df.to_json(orient='split'))
for i, ind in enumerate(dicIndex['index']):
    # Note: pandas has some transformation between date,timestampe and string.
    d = pd.to_datetime(dicIndex['data'][i][0], unit='ms').strftime('%Y-%m-%d')
    jsonstr = {
        '_id':  d,
        'year': year,
        dicIndex['columns'][0]: d,
        dicIndex['columns'][1]: dicIndex['data'][i][1],
    }
    try:
        conn[db][coll].insert(jsonstr)
    except:
        pass
