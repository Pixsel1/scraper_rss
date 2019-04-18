from django.urls import path

from currency_rates.views import CurrencyRateViewSet


app_name = 'currency_rates'

urlpatterns = [
    path('', CurrencyRateViewSet.as_view()),
]
