from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Tag(models.Model):
    name = models.CharField('タグ名', max_length=255)
    color = models.CharField('背景色', max_length=7, default='#ffffff')

    def __str__(self):
        return self.name


class Post(models.Model):

    class Color(models.TextChoices):
        WHITE = "#ffffff", "白"
        BLACK = "#000000", "黒"
        
    title = models.CharField('タイトル', max_length=255)
    thumbnail = models.ImageField('サムネイル', null=True, blank=True)
    tag = models.ManyToManyField(Tag, verbose_name='タグ', related_name='posts_tags')
    slug = models.SlugField('スラッグ', unique=True)
    lead_text = models.TextField('紹介文', max_length=255)
    main_text = MarkdownxField('本文')
    is_public = models.BooleanField('公開する', default=False)
    color = models.CharField('文字色', max_length=7, choices=Color.choices, default="#ffffff")
    created_at = models.DateField('作成日')
    updated_at = models.DateField('更新日', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def convert_markdown_to_html(self):
        return mark_safe(markdownify(self.main_text))

    def build_date(self, date=None):
        """日付をyyyy/mm/dd/aaa表記に変換"""
        return date.strftime('%Y/%m/%d/%a') if date else None
