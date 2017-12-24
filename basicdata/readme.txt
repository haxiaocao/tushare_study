600547:山东黄金
600362:江西铜业
600312:平高电气
600499：科达洁能
603993：洛阳钼业


沪深股票列表     -> get_stock_basics
业绩预告		 -> get_report_data
业绩报告（主表） -> get_report_data
盈利能力数据     -> get_profit_data
营运能力数据     -> get_operation_data
成长能力数据	 -> get_growth_data
偿债能力数据     -> get_debtpaying_data
现金流量数据     -> get_cashflow_data

# db.getCollection('sh_margins').update( {_id:{$ne:null} } , { $set : { "market" : "SH"} }, false, true );