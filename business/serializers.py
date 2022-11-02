
from .models import *
from rest_framework.serializers import ModelSerializer


# 交易所的序列化器
class ExchangeSer(ModelSerializer):
    class Meta:
        model = ExchangeModel
        fields = "__all__"


# 货币的序列化器
class CurrencySer(ModelSerializer):
    class Meta:
        model = CurrencyModel
        fields = "__all__"


# 交易对的序列化器
class DealSer(ModelSerializer):
    class Meta:
        model = DealModel
        fields = "__all__"
