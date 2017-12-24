600547:山东黄金
600362:江西铜业
600312:平高电气
600499：科达洁能
603993：洛阳钼业


分配预案  ->  ts.profit_data
业绩预告  ->  ts.forecast_data
限售股解禁->  ts.xsg_data
基金持股  ->  ts.fund_holdings
新股上市  ->  ts.new_stocks
融资融券（沪市） -> ts.sh_margins, ts.sh_margin_details
融资融券（深市） -> ts.sz_margins, ts.sz_margin_details

# db.getCollection('sh_margins').update( {_id:{$ne:null} } , { $set : { "market" : "SH"} }, false, true );