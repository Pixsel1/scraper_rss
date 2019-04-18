import moneyed

from django.db import models
from django.utils.translation import ugettext_lazy as _

from djmoney.models.fields import CurrencyField


class CurrencyRate(models.Model):

    class Meta:
        verbose_name = _('Currency Rate')
        verbose_name_plural = _('Currency Rates')

    source_currency = CurrencyField(
        _('source currency'),
    )
    target_currency = CurrencyField(
        _('target currency'),
        default=moneyed.EUR,
    )
    rate = models.DecimalField(
        _('rate'),
        max_digits=10,
        decimal_places=5,
    )
    uploaded = models.DateTimeField(
        _('uploaded'),
    )
