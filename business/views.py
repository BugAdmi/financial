
from rest_framework.views import Response, APIView

from business.a import pp
from business.models import ExchangeModel,  CurrencyHistoryModel, CurrencyModel, DealModel
from .serializers import ExchangeSer,CurrencySer



# Create your views here.

class R(APIView):
    def get(self, request):
        print(pp)
        CurrencyHistoryModel.objects.bulk_create([CurrencyHistoryModel(**i) for i in pp])


# 交易所
class ExchangeAPIView(APIView):
    def post(self, request):
        name = request.data.get("name")
        official_address = request.data.get("official_address")
        icon = request.data.get("icon")
        count_deal = request.data.get("count_deal")
        if not ([name, official_address, icon, count_deal]):
            return Response({
                'code': 400,
                'msg': '交易所信息不完整',
            })
        ex = ExchangeModel.objects.filter(name_chinese=name).first()
        if ex:
            return Response({
                'code': 400,
                'msg': '交易所已存在',
            })
        exchange = ExchangeModel.objects.create(
            name_chinese=name,
            official_address=official_address,
            icon=icon,
            count_deal=count_deal
        )
        exchange.save()
        return Response({
            'code': 200,
            'msg': '添加交易所成功',
        })

    def get(self, request):
        exchange = ExchangeModel.objects.all()
        list_1 = []
        for i in exchange:
            ex = {
                "name": i.name_chinese,
                "official_address": i.official_address,
                "icon": i.icon,
                'count_deal': i.count_deal
            }
            list_1.append(ex)
        return Response({
            'code': 200,
            'msg': '获取交易所信息成功',
            'data': list_1,
        })


# 获取单个交易所
class ExchangeOneAPIView(APIView):
    def get(self, request):
        id = request.data.get("id")
        exchange = ExchangeModel.objects.filter(id=id).first()
        ser = ExchangeSer(exchange)
        return Response({
            'code': 200,
            'msg': '交易所单个信息获取成功',
            'data': ser.data,
        })


# 货币
class CurrencyAPIView(APIView):
    def post(self, request):
        fullname = request.data.get("fullname")
        name = request.data.get("name")
        current_price = request.data.get("current_price")
        high_price = request.data.get("high_price")
        low_price = request.data.get("low_price")
        vol = request.data.get("vol")
        logo = request.data.get("logo")
        marketcap = request.data.get("marketcap")
        if not ([fullname, name, current_price, high_price, low_price, vol, logo, marketcap]):
            return Response({
                'code': 400,
                'msg': '请完善币种信息',
            })
        bite = CurrencyModel.objects.filter(fullname=fullname).first()
        if bite:
            return Response({
                'code': 400,
                'msg': '该币种已存在',
            })
        icon_bite = CurrencyModel.objects.create(
            fullname=fullname,
            name=name,
            current_price=current_price,
            high_price=high_price,
            low_price=low_price,
            vol=vol,
            logo=logo,
            marketcap=marketcap
        )
        icon_bite.save()
        return Response({
            'code': 200,
            'msg': '币种添加成功',
        })

    def get(self, request):
        bite = CurrencyModel.objects.all()
        lst_1 = []
        for i in bite:
            a = ({
                "fullname": i.fullname,
                "name": i.name,
                "current_price": i.current_price,
                "high_price": i.high_price,
                "low_price": i.low_price,
                "vol": i.vol,
                "logo": i.logo,
                "marketcap": i.marketcap,
            })
            lst_1.append(a)
            return Response({
                'code': 200,
                'msg': '币种获取成功',
                'data': lst_1,
            })


# 获取单个货币
class CurrencyOneAPIView(APIView):
    def get(self, request):
        id = request.data.get("id")
        bite = CurrencyModel.objects.filter(id=id).first()
        ser = CurrencySer(bite)
        return Response({
            'code': 200,
            'msg': '获取单个数据成功',
            'data': ser.data,
        })


# 交易对
class DealAPIVIew(APIView):
    def get(self, request):
        deal = DealModel.objects.all()
        lst_1 = []
        for i in deal:
            data = {
                "deal_name": i.deal_name,
                "collect": i.collect,
                "open": i.open,
                "limit_price": i.limit_price,
                "top_price": i.top_price,
                "floor_price": i.floor_price,
                "turnover": i.turnover,
                "exchange_id": i.exchange_id.name_chinese,
                "switch": i.switch,
            }
            lst_1.append(data)
        return Response({'code': 200, 'msg': '获取成功！', 'data': lst_1})
