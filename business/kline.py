# -*- coding: utf-8 -*-
import requests
import pymysql
# 1分钟
url = 'https://www.mexc.com/api/platform/spot/market/kline?end=1666437419999&interval=Min1&openPriceMode=LAST_CLOSE&start=1666428420000&symbol=BTC_USDT'
# 15分钟
# url='https://www.mexc.com/api/platform/spot/market/kline?end=1666464299999&interval=Min15&openPriceMode=LAST_CLOSE&start=1666329300000&symbol=BTC_USDT'

r = requests.get(url)
s = r.json()['data']

for i in s:
    along_time = s['t']
    print("------------------", along_time)
    open = s['o']  # 开值
    collect = s['c']  # 收值
    high = s['h']  # 最高价
    down = s['l']  # 最低价
    limit_price = s['q']  # 涨跌幅
    minute_num = s['v']  # 一分钟成交量

    for j in range(len(along_time)):
        # print(along_time[j],open[j])

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123', database='financial')
        cursor = conn.cursor()
        # 1分钟
        sql = f"-- insert into tb_1mKline values (0,{open[j]},{high[j]},{down[j]},{collect[j]},{limit_price[j]},{minute_num[j]},{along_time[j]},1,1)"
        # 15分钟
        # sql = f"-- insert into tb_15mKline values (0,{open[j]},{high[j]},{down[j]},{collect[j]},{limit_price[j]},{minute_num[j]},{along_time[j]},1,1)"
        try:
            cursor.execute(sql)
            conn.commit()
            print('插入成功')
        except Exception as e:
            print('插入失败', e)
            conn.rollback()


