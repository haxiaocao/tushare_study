# -*- coding:UTF-8 -*-
import tushare as ts
import pymongo
import json

# 600547:山东黄金
# 600362:江西铜业
# 600312:平高电气
# 600499：科达洁能
# 603993：洛阳钼业
conn = pymongo.MongoClient('127.0.0.1', port=27017)
df = ts.get_index()
# index data columns(14 columns)
dicIndex = json.loads(df.to_json(orient='split'))
for i, ind in enumerate(dicIndex['index']):
    jsonstr = {
        '_id': "20171219-" + dicIndex['data'][i][0],
        'Date': '20171219',
        dicIndex['columns'][0]: dicIndex['data'][i][0],
        dicIndex['columns'][1]: dicIndex['data'][i][1],
        dicIndex['columns'][2]: dicIndex['data'][i][2],
        dicIndex['columns'][3]: dicIndex['data'][i][3],
        dicIndex['columns'][4]: dicIndex['data'][i][4],
        dicIndex['columns'][5]: dicIndex['data'][i][5],
        dicIndex['columns'][6]: dicIndex['data'][i][6],
        dicIndex['columns'][7]: dicIndex['data'][i][7],
        dicIndex['columns'][8]: dicIndex['data'][i][8],
        dicIndex['columns'][9]: dicIndex['data'][i][9]
    }
    conn.Trade.AllIndies.insert(jsonstr)
