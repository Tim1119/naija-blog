from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from apps.posts.models import Article
from apps.profiles.models import Profile
from apps.common.models import TimeStampedUUID
from apps.posts.models import Article
from autoslug import AutoSlugField

# Create your models here.


class Comment(TimeStampedUUID):
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name=_("Comment Author"))
    content = models.TextField()
    article = models.ForeignKey(Article, verbose_name=_(
        'Article'), on_delete=models.PROTECT)
    slug = AutoSlugField(populate_from='content', unique=True)

    def __str__(self) -> str:
        return self.content

    def count_category(self):
        return self.article_set.count
