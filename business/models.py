from django.db import models


# Create your models here.

# 交易所表
class ExchangeModel(models.Model):
    name_chinese = models.CharField(max_length=100, verbose_name='交易所中文名')
    name_english = models.CharField(max_length=100, verbose_name='交易所英文名')
    official_address = models.CharField(max_length=500, verbose_name='官网地址')
    icon = models.CharField(max_length=500, verbose_name='交易所图标')
    description = models.CharField(max_length=500, verbose_name='交易所描述')
    count_deal = models.IntegerField(verbose_name='交易对总数')

    def __str__(self):
        return self.name_chinese

    class Meta:
        db_table = 'tb_exchange'


# 货币表
class CurrencyModel(models.Model):
    fullname = models.CharField(max_length=100, verbose_name='货币中文名')
    name = models.CharField(max_length=100, verbose_name='货币英文名')
    # description = models.TextField(max_length=500, verbose_name='货币描述')
    # latest_price = models.DecimalField(max_digits=20, decimal_places=8, verbose_name='货币最新价')
    current_price = models.CharField(max_length=100, verbose_name='货币最新价')
    # limit_price = models.DecimalField(max_digits=6, decimal_places=4, verbose_name='货币涨跌幅')
    # top_price = models.DecimalField(max_digits=20, decimal_places=8, verbose_name='24小时最高价')
    high_price = models.CharField(max_length=100, verbose_name='24小时最高价')
    # floor_price = models.DecimalField(max_digits=20, decimal_places=8, verbose_name='24小时最低价')
    low_price = models.CharField(max_length=100, verbose_name='24小时最低价')
    # turnover = models.DecimalField(max_digits=30, decimal_places=3, verbose_name='24小时成交量')
    vol = models.CharField(max_length=100, verbose_name='24小时成交量')
    logo = models.CharField(max_length=500, verbose_name='货币图标')
    # market = models.DecimalField(max_digits=20, decimal_places=9, verbose_name="市值")
    marketcap = models.CharField(max_length=100, verbose_name="市值")

    # issue_date = models.DateTimeField(default="", verbose_name='货币发行时间')
    # withdraw_state = models.SmallIntegerField(default=1, choices=((1, "可提现"), (0, "不可提现")))
    # recharge_state = models.SmallIntegerField(default=1, choices=((1, '可充值'), (0, '不可充值')))

    class Meta:
        db_table = 'tb_currency'

    def __str__(self):
        return self.fullname


# 交易对儿表
class DealModel(models.Model):
    deal_name = models.CharField(max_length=50, verbose_name="交易对名字")
    collect = models.IntegerField(verbose_name='收值')
    open = models.IntegerField(verbose_name='开值')
    limit_price = models.DecimalField(max_digits=20, decimal_places=8, verbose_name='货币涨跌幅')
    top_price = models.DecimalField(max_digits=20, decimal_places=8, verbose_name='最高值')
    floor_price = models.DecimalField(max_digits=20, decimal_places=8, verbose_name='最低值')
    turnover = models.DecimalField(max_digits=30, decimal_places=3, verbose_name='24小时成交量')
    exchange_id = models.ForeignKey(ExchangeModel, on_delete=models.CASCADE, verbose_name="交易所id")
    switch = models.BooleanField(default=1, verbose_name="是否显示的开关")

    class Meta:
        db_table = "tb_deal"

    def __str__(self):
        return self.deal_name


# 币历史表
class CurrencyHistoryModel(models.Model):
    currency_id = models.ForeignKey(CurrencyModel, on_delete=models.CASCADE, verbose_name="币id")
    price = models.CharField(max_length=100, verbose_name="当前价格")
    price_time = models.DateTimeField(auto_now_add=True, verbose_name="价格所属时间")

    class Meta:
        db_table = "tb_currency_history"

    def __str__(self):
        return self.currency_id


# 交易对儿历史表
class TransactionHistoryModel(models.Model):
    currency_id = models.ForeignKey(CurrencyModel, on_delete=models.CASCADE, verbose_name="币id")
    exchange_id = models.ForeignKey(ExchangeModel, on_delete=models.CASCADE, verbose_name="交易所id")
    deal_name = models.ForeignKey(DealModel, on_delete=models.CASCADE, verbose_name="交易对儿名称")
    open = models.IntegerField(verbose_name="开值")
    high = models.IntegerField(verbose_name="高值")
    down = models.IntegerField(verbose_name="低值")
    collect = models.IntegerField(verbose_name="收值")
    limit_price = models.DecimalField(max_digits=6, decimal_places=4, verbose_name='货币涨跌幅')
    data_time = models.DateTimeField(auto_now_add=True, verbose_name="所属时间")

    class Meta:
        db_table = "tb_transaction_history"

    def __str__(self):
        return self.deal_name


# K线 1m
class KLine1Model(models.Model):
    currency_id = models.ForeignKey(CurrencyModel, on_delete=models.CASCADE, verbose_name="币id")
    exchange_id = models.ForeignKey(ExchangeModel, on_delete=models.CASCADE, verbose_name="交易所id")
    # deal_name = models.ForeignKey(DealModel, on_delete=models.CASCADE, verbose_name="交易对儿名称")
    open = models.CharField(max_length=100, verbose_name="开值")
    high = models.CharField(max_length=100, verbose_name="高值")
    down = models.CharField(max_length=100, verbose_name="低值")
    collect = models.CharField(max_length=100, verbose_name="收值")
    limit_price = models.CharField(max_length=1024, verbose_name='货币涨跌幅')
    # data_time = models.DateTimeField(auto_now_add=True, verbose_name="所属时间")
    minute_num = models.CharField(max_length=100, verbose_name="一分钟成交量")
    # minute_price = models.IntegerField(verbose_name="一分钟成交额度")
    along_time = models.CharField(max_length=1024, verbose_name="时间戳")

    class Meta:
        db_table = "tb_1mkline"

    def __str__(self):
        return self.currency_id


# K线 15m
class KLine15Model(models.Model):
    currency_id = models.ForeignKey(CurrencyModel, on_delete=models.CASCADE, verbose_name="币id")
    exchange_id = models.ForeignKey(ExchangeModel, on_delete=models.CASCADE, verbose_name="交易所id")
    # deal_name = models.ForeignKey(DealModel, on_delete=models.CASCADE, verbose_name="交易对儿名称")
    open = models.CharField(max_length=100, verbose_name="开值")
    high = models.CharField(max_length=100, verbose_name="高值")
    down = models.CharField(max_length=100, verbose_name="低值")
    collect = models.CharField(max_length=100, verbose_name="收值")
    limit_price = models.CharField(max_length=1024, verbose_name='货币涨跌幅')
    # data_time = models.DateTimeField(auto_now_add=True, verbose_name="所属时间")
    minute_num = models.CharField(max_length=100, verbose_name="十五分钟成交量")
    # minute_price = models.IntegerField(verbose_name="十五分钟成交额度")
    along_time = models.CharField(max_length=1024, verbose_name="时间戳")

    class Meta:
        db_table = "tb_15mkline"

    def __str__(self):
        return self.currency_id


# 交易对关系表
class DealRelationModel(models.Model):
    currency_id = models.ForeignKey(CurrencyModel, on_delete=models.CASCADE, verbose_name="币id")
    currency_name = models.CharField(max_length=100, verbose_name="货币名字")

    class Meta:
        db_table = "tb_deal_relation"

    def __str__(self):
        return self.currency_name
