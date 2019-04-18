from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from currency_rates.filters import CurrencyRateFilterSet
from currency_rates.models import CurrencyRate
from currency_rates.serializers import CurrencyRateSerializer


class CurrencyRateViewSet(generics.ListAPIView):
    serializer_class = CurrencyRateSerializer
    queryset = CurrencyRate.objects.all()
    filter_backends = (
        DjangoFilterBackend,
    )
    filterset_class = CurrencyRateFilterSet
