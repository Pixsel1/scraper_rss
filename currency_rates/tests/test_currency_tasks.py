import moneyed
import pytz

from datetime import datetime
from decimal import Decimal
from typing import List

from django.test import TestCase

from currency_rates.models import CurrencyRate
from currency_rates.utils import (
    ECBCurrencyRate,
    CurrencyRate as RawCurrencyRate,
)
from currency_rates.tasks import extract_currency_rates


class TestECBCurrencyRate:

    def get_currency_rates(self) -> List[RawCurrencyRate]:
        return [
            RawCurrencyRate(
                source_currency=moneyed.USD,
                target_currency=moneyed.EUR,
                rate=Decimal('5.6'),
                uploaded=datetime(2019, 10, 10, 1, 1, 1),
            ),
            RawCurrencyRate(
                source_currency=moneyed.JPY,
                target_currency=moneyed.EUR,
                rate=Decimal('1.20'),
                uploaded=datetime(2019, 10, 10, 1, 1, 1),
            ),
        ]


test_currency_rate = TestECBCurrencyRate()


class CurrencyRateTest(TestCase):

    def test_get_currency_rates(self):
        extract_currency_rates(test_currency_rate)

        currency_rate = CurrencyRate.objects.get(source_currency=moneyed.USD)

        assert currency_rate.source_currency == moneyed.USD.code
        assert currency_rate.target_currency == moneyed.EUR.code
        assert currency_rate.rate == Decimal('5.6')
        assert currency_rate.uploaded == datetime(
            2019, 10, 10, 1, 1, 1,
            tzinfo=pytz.UTC
        )
        assert CurrencyRate.objects.count() == 2
