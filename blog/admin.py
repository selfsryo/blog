from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Post, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "color")


class PostAdmin(MarkdownxModelAdmin):
    list_display = ("title", "get_tag", "slug", "is_public", "created_at", "updated_at")
    list_display_links = list_display
    ordering = ("-created_at",)

    def get_tag(self, row):
        """In an admin panel, display the 'tag' which is a ManyToMany field, separated by commas."""
        return ",".join([x.name for x in row.tag.all()])


admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
