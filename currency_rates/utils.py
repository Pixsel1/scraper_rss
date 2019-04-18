import feedparser
import re

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from moneyed import Currency
from typing import List


@dataclass
class CurrencyRate:
    source_currency: Currency
    target_currency: Currency
    rate: Decimal
    uploaded: datetime


class ECBCurrencyRate:
    pattern = re.compile('\d+\.\d+')

    def __init__(self, source_url, source_currency, target_currency):
        self.source_url = source_url
        self.source_currency = source_currency
        self.target_currency = target_currency

    def get_currency_rates(self) -> List[CurrencyRate]:
        data = feedparser.parse(self.source_url)

        return [
            CurrencyRate(
                source_currency=self.source_currency,
                target_currency=self.target_currency,
                rate=self.parse_rate(entry.cb_exchangerate),
                uploaded=datetime.fromisoformat(entry.updated),
            )
            for entry in data.entries
        ]

    def parse_rate(self, rate):
        # rate from ECB is a concat of rate and currency e.g. 1278.95\nEUR
        return re.match(self.pattern, rate).group()
