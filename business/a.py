# -*- coding: utf-8 -*-


import json

with open('btc.json', 'r') as f:
    t = json.loads(f.read())["stats"]
pp = [{"currency_id": 1, "price": i[0], "price_time": i[1]} for i in t]
