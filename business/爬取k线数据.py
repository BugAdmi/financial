import requests
import json
from pprint import pprint
import pymysql
#1分钟
# url = 'https://www.mexc.com/api/platform/spot/market/kline?end=1666437419999&interval=Min1&openPriceMode=LAST_CLOSE&start=1666428420000&symbol=BTC_USDT'
#15分钟
url='https://www.mexc.com/api/platform/spot/market/kline?end=1666464299999&interval=Min15&openPriceMode=LAST_CLOSE&start=1666329300000&symbol=BTC_USDT'

r = requests.get(url)
s = r.json()['data']

for i in s:
    lowtime=s['t']
    print(lowtime)
    open = s['o']  # 第一笔成交价
    collect = s['c']  # 末一笔成交价
    high = s['h']  # 最高价
    down = s['l']  # 最低价
    price_limit = s['q']  # 涨跌幅
    minute_num = s['v']  # 一分钟成交量
    for j in range(len(lowtime)):
        # print(lowtime[j],open[j])

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123', database='financial')
        cursor = conn.cursor()
        #1分钟
        # sql = f"insert into tb_k_line values (0,{open[j]},{down[j]},{collect[j]},{price_limit[j]},{minute_num[j]},1,{lowtime[j]},1,{high[j]})"
        #15分钟
        sql = f"insert into tb_line_fifteen values (0,{open[j]},{high[j]},{down[j]},{collect[j]},{price_limit[j]},{minute_num[j]},1,{lowtime[j]},1)"
        try:
            cursor.execute(sql)
            conn.commit()
            print('插入成功')
        except Exception as e:
            print('插入失败', e)
            conn.rollback()


# a = [1,2,3]
# b = [4,5,6]
# for i in range(len(a)):
#     print(a[i], b[i])