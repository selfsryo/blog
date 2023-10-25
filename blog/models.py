from django.db import models
from django.utils.safestring import mark_safe
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Tag(models.Model):
    name = models.CharField("Tag Name", max_length=255)
    color = models.CharField("Background Color", max_length=7, default="#000000", blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField("Title", max_length=255)
    title_en = models.CharField("Title En", max_length=255, blank=True, null=True)
    thumbnail = models.ImageField("Thumbnail", null=True, blank=True)
    tag = models.ManyToManyField(Tag, verbose_name="Tag", related_name="posts_tags")
    slug = models.SlugField("Slug", unique=True)
    lead_text = models.TextField("Introduction", max_length=255)
    lead_text_en = models.TextField("Introduction En", max_length=255, blank=True, null=True)
    main_text = MarkdownxField("Text")
    main_text_en = MarkdownxField("Text En", blank=True, null=True)
    is_public = models.BooleanField("Public", default=False)
    created_at = models.DateField("Created At")
    updated_at = models.DateField("Updated At", blank=True, null=True)

    class Color(models.TextChoices):
        WHITE = "#ffffff", "White"
        BLACK = "#000000", "Black"

    color = models.CharField("Font Color", max_length=7, choices=Color.choices, default="#ffffff")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def convert_markdown_to_html(self):
        return mark_safe(markdownify(self.main_text))

    def convert_english_markdown_to_html(self):
        if self.main_text_en is not None:
            return mark_safe(markdownify(self.main_text_en))
        else:
            return mark_safe(markdownify(self.main_text))

    def build_date(self, date=None):
        """Convert the date to YYYY/MM/DD format"""
        return date.strftime("%Y/%m/%d/%a") if date else None
