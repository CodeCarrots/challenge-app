from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class UnlockedKey(models.Model):
    user = models.ForeignKey(User, related_name='unlocked_keys')
    key = models.CharField(max_length=128, verbose_name=_('key'),
                             help_text=_('Unlocked key value.'))
    ts = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'key'))
        verbose_name = _('unlocked key')
        verbose_name_plural = _('unlocked keys')
