# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from business.views import ExchangeAPIView, ExchangeOneAPIView, CurrencyAPIView, CurrencyOneAPIView, DealAPIVIew
from rest_framework.routers import DefaultRouter

# 实例化
route = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    # 交易所
    path('exchange/', ExchangeAPIView.as_view()),
    # 获取单个交易所
    path('exchange/', ExchangeOneAPIView.as_view()),
    # 货币
    path('currency/', CurrencyAPIView.as_view()),
    # 获取单个货币
    path('currency/', CurrencyOneAPIView.as_view()),
    # 交易对
    path('deal/', DealAPIVIew.as_view()),
]

# 路由拼接
urlpatterns += route.urls
