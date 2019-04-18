from rest_framework import serializers

from currency_rates.models import CurrencyRate


class CurrencyRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CurrencyRate
        fields = (
            'id',
            'source_currency',
            'target_currency',
            'rate',
            'uploaded',
        )
