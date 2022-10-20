import time

from django.db import models

# Create your models here.
#比表,交易所,交易对，币跟币，k表，
class Exchange(models.Model):
    name=models.CharField('交易所名称',unique=True,max_length=30)
    img=models.CharField('交易所地址',max_length=1026)
    code=models.CharField('',max_length=100,unique=True)
    sum=models.IntegerField('总数')

    def __str__(self):
        return self.name

    class Meta:
        db_table='tb_exchange'
        verbose_name_plural='交易所表'

class Coin(models.Model):
    name=models.CharField('币名',max_length=30,unique=True)
    abbre_name=models.CharField('缩写',max_length=30,unique=True)
    icon=models.CharField('图标',max_length=680)
    shuffle=models.IntegerField('排行',unique=True)
    spot_price=models.DecimalField('当前价格',max_digits=9,decimal_places=2)
    market=models.DecimalField('市值',max_digits=30,decimal_places=0)
    turnover=models.IntegerField('24成交量')
    minimum=models.IntegerField('最低')
    highest=models.IntegerField('最高')
    def __str__(self):
        return self.name

    class Meta:
        db_table='tb_currency'
        verbose_name_plural='币种表'

#交易对表
class Trading(models.Model):
    cion=models.ForeignKey(Coin,on_delete=models.CASCADE,verbose_name='币id',related_name='coin')
    cions=models.ForeignKey(Coin,on_delete=models.CASCADE,verbose_name='币id')
    exchange=models.ForeignKey(Exchange,on_delete=models.CASCADE,verbose_name='交易所')
    reveal=models.BooleanField('是否显示',default=False)
    name=models.CharField('交易对名称',max_length=20)
    open = models.IntegerField(verbose_name='开值')
    high = models.IntegerField(verbose_name='高值')
    down = models.IntegerField(verbose_name='低值')
    collect = models.IntegerField(verbose_name='收值')
    price_limit = models.IntegerField(verbose_name='涨跌幅')

    def __str__(self):
        return self.name

    class Meta:
        db_table='tb_trading'

class History_coin(models.Model):
    cion = models.ForeignKey(Coin, on_delete=models.CASCADE, verbose_name='币id')
    spot_price = models.DecimalField('当前价格', max_digits=7, decimal_places=2)
    new_time=models.CharField('价格最新时间',max_length=90)

    def __str__(self):
        return self.cion.name

    class Meta:
        db_table='tb_history'
        verbose_name_plural='币历史表'

#交易对历史表
class History_Exchange(models.Model):
    cion = models.ForeignKey(Coin, on_delete=models.CASCADE, verbose_name='币id')
    exchange=models.ForeignKey(Exchange,on_delete=models.CASCADE,verbose_name='交易所')
    time=models.DateTimeField('所属时间')
    name = models.CharField('交易对名称', max_length=20)
    open = models.IntegerField(verbose_name='开值')
    high = models.IntegerField(verbose_name='高值')
    down = models.IntegerField(verbose_name='低值')
    collect = models.IntegerField(verbose_name='收值')
    price_limit = models.IntegerField(verbose_name='涨跌幅')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_history_exchange'

class K_line(models.Model):
    deal_history = models.ForeignKey(Coin, on_delete=models.CASCADE, verbose_name='虚拟货币id')
    ex_id = models.ForeignKey(Exchange, on_delete=models.CASCADE, verbose_name='交易所id')
    trading_name = models.CharField(max_length=64, verbose_name='交易对名字')
    open = models.IntegerField(verbose_name='开值')
    high = models.IntegerField(verbose_name='高值')
    down = models.IntegerField(verbose_name='低值')
    collect = models.IntegerField(verbose_name='收值')
    price_limit = models.IntegerField(verbose_name='涨跌幅')
    minute_num = models.IntegerField(verbose_name='一分钟成交量')
    minute_price = models.IntegerField(verbose_name='一分钟成交额度')
    def __str__(self):
        return self.trading_name

    class Meta:
        db_table = 'tb_k_line'
        verbose_name_plural='1分钟k值'

class K_line_fifteen(models.Model):
    deal_history = models.ForeignKey(Coin, on_delete=models.CASCADE, verbose_name='虚拟货币id')
    ex_id = models.ForeignKey(Exchange, on_delete=models.CASCADE, verbose_name='交易所id')
    trading_name = models.CharField(max_length=64, verbose_name='交易对名字')
    open = models.IntegerField(verbose_name='开值')
    high = models.IntegerField(verbose_name='高值')
    down = models.IntegerField(verbose_name='低值')
    collect = models.IntegerField(verbose_name='收值')
    price_limit = models.IntegerField(verbose_name='涨跌幅')
    minute_num = models.IntegerField(verbose_name='十五分钟成交量')
    minute_price = models.IntegerField(verbose_name='十五分钟成交额度')

    def __str__(self):
        return self.trading_name

    class Meta:
        db_table = 'tb_line_fifteen'
        verbose_name_plural='15分钟k值'