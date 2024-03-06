from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedUUID


class Profile(TimeStampedUUID):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name=_('User'))
    profile_image = models.ImageField(
        default='default.png', verbose_name=_('Profile Image'))
    bio = models.TextField(verbose_name=_('Bio'), default='bio')
    linkedin = models.URLField(verbose_name=_(
        'Linkedin URL'), blank=True, null=True)
    instagram = models.URLField(verbose_name=_(
        'Instagram'), blank=True, null=True)
    twitter = models.URLField(verbose_name=_('Twitter'), blank=True, null=True)
    facebook = models.URLField(verbose_name=_(
        'Facebook'), blank=True, null=True)
    slug = AutoSlugField(populate_from='user', unique=True)

    @property
    def profile_pic_url(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    def __str__(self) -> str:
        return self.user.username
