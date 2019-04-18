import moneyed

from celery import shared_task

from currency_rates.models import CurrencyRate
from currency_rates.utils import (
    CurrencyRate as RawCurrencyRate,
    ECBCurrencyRate,
)

ECB_CURRENCIES = (
    moneyed.USD, moneyed.JPY, moneyed.BGN, moneyed.CZK, moneyed.DKK,
    moneyed.GBP, moneyed.HUF, moneyed.PLN, moneyed.RON, moneyed.SEK,
    moneyed.CHF, moneyed.ISK, moneyed.NOK, moneyed.HRK, moneyed.RUB,
    moneyed.TRY, moneyed.AUD, moneyed.BRL, moneyed.CAD, moneyed.CNY,
    moneyed.HKD, moneyed.IDR, moneyed.INR, moneyed.KRW, moneyed.MXN,
    moneyed.MYR, moneyed.NZD, moneyed.PHP, moneyed.SGD, moneyed.THB,
    moneyed.ZAR,
)


def save_currency_rate(currency_rate: RawCurrencyRate) -> None:
    if CurrencyRate.objects.filter(
        source_currency=currency_rate.source_currency,
        target_currency=currency_rate.target_currency,
        uploaded=currency_rate.uploaded,
    ).exists():
        return

    model = CurrencyRate(
        source_currency=currency_rate.source_currency,
        target_currency=currency_rate.target_currency,
        rate=currency_rate.rate,
        uploaded=currency_rate.uploaded,
    )
    model.save()


def extract_currency_rates(currency_rate: ECBCurrencyRate) -> None:
    for c_rate in currency_rate.get_currency_rates():
        save_currency_rate(c_rate)


@shared_task
def get_currency_rates():
    main_source_url = 'https://www.ecb.europa.eu/rss/fxref-{}.html'
    for currency in ECB_CURRENCIES:
        extract_currency_rates(
            ECBCurrencyRate(
                source_url=main_source_url.format(str(currency).lower()),
                source_currency=currency,
                target_currency=moneyed.EUR
            )
        )
