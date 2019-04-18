import django_filters

from currency_rates.models import CurrencyRate


class CurrencyRateFilterSet(django_filters.FilterSet):
    uploaded__gte = django_filters.DateTimeFilter(
        field_name='uploaded',
        lookup_expr='gte',
    )
    uploaded__lte = django_filters.DateTimeFilter(
        field_name='uploaded',
        lookup_expr='lte',
    )

    class Meta:
        model = CurrencyRate
        fields = (
            'source_currency',
            'target_currency',
        )
