# -*- coding: utf-8 -*-
import requests
import pymysql

url = 'https://dncapi.moveft.com/api/coin/web-coinrank?page=1&type=-1&pagesize=100&webp=1'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52"
}

request = requests.get(url=url, headers=headers)

json_data = request.json()['data']
# pprint(json_data)
print(json_data)
for i in json_data:
    fullname = i['fullname']  # 中文名
    print("-----------------", fullname)
    name = i['name']  # 简称
    logo = i['logo']  # 图标
    # coin_now_price = i['current_price']  # 人民币
    # coin_value = i['current_price_usd']  # 美元现价
    current_price = i['current_price']  # 最新价格
    marketcap = i['marketcap']  # 市值
    vol = i['vol']  # 24成交量
    high_price = i['high_price']  # 最高价格
    low_price = i['low_price']  # 最低价格
    # coin_rank_list = i['rank']  # 排行
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123', database='financial')
    cursor = conn.cursor()

    sql = f"""insert into tb_currency values (0,'{fullname}','{name}','{current_price}','{high_price}','{low_price}','{vol}','{logo}','{marketcap}')"""
    try:
        cursor.execute(sql)
        conn.commit()
        print('插入成功')

    except Exception as e:
        print('插入失败', e)
        conn.rollback()
