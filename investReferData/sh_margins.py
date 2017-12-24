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
coll = "sh_margins"
ty = "600547"
market = 'SH'

conn = pymongo.MongoClient('127.0.0.1', port=27017)
if ty == 'all':
    df = ts.sh_margins(start='2017-01-01', end='2017-12-22')
else:
    df = ts.sh_margin_details(
        start='2016-01-01', end='2017-01-01', symbol=ty)
# index data columns(14 columns)
dicIndex = json.loads(df.to_json(orient='split'))
for i, ind in enumerate(dicIndex['index']):
    jsonstr = {
        '_id':  dicIndex['data'][i][0] + "-" + ty,
        'type': ty,
        'market': market,
        dicIndex['columns'][0]: dicIndex['data'][i][0],
        dicIndex['columns'][1]: dicIndex['data'][i][1],
        dicIndex['columns'][2]: dicIndex['data'][i][2],
        dicIndex['columns'][3]: dicIndex['data'][i][3],
        dicIndex['columns'][4]: dicIndex['data'][i][4],
        dicIndex['columns'][5]: dicIndex['data'][i][5],
        dicIndex['columns'][6]: dicIndex['data'][i][6],
        dicIndex['columns'][7]: dicIndex['data'][i][7],
        dicIndex['columns'][8]: dicIndex['data'][i][8]
    }
    try:
        conn[db][coll].insert(jsonstr)
    except:
        pass
