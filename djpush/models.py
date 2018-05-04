from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class JiGuangReg(models.Model):
    USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
    user = models.ForeignKey(USER_MODEL, verbose_name=_('User'))
    regid = models.CharField(verbose_name=_('RegID'), max_length=24)
    is_push = models.BooleanField(verbose_name=_('Is Push'), default=True)

    class Meta:
        verbose_name = _('Ji Guang Reg id')
        verbose_name_plural = _("Ji Guang Reg id")
