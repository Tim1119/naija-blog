from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedUUID
from apps.profiles.models import Profile
# Create your models here.


class Tags(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Article Tag'
        verbose_name_plural = 'Article Tag'


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'


class Article(TimeStampedUUID):

    class ArticleStatus(models.TextChoices):
        Draft = "Draft", _("Draft")
        Published = "Published", _("Published")

    author = models.ForeignKey(
        Profile, on_delete=models.PROTECT, verbose_name=_("Article Author"))
    title = models.CharField(verbose_name=_(
        "Article Title"), max_length=255, unique=True)
    image_headline = models.ImageField(upload_to='headlines-images')
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name=_("Article Category"))
    tag = models.ManyToManyField(
        Tags, verbose_name=_("Article Tag"))
    slug = AutoSlugField(populate_from='title', unique=True)
    content = RichTextField(verbose_name=_('Content'))
    status = models.CharField(
        max_length=255, choices=ArticleStatus.choices, default=ArticleStatus.Draft)

    approved = models.BooleanField(default=True)
    likes = models.ManyToManyField(
        User, related_name='likes', blank=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Article'
        verbose_name_plural = 'Article'

    def __str__(self):
        return self.title

    def count_comment(self):
        return self.comment_set.count()

    @property
    def image_headline_url(self):
        try:
            url = self.image_headline.url
        except:
            url = ''
        return url
