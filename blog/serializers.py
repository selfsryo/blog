from rest_framework import serializers

from .models import Post, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class PostSerializer(serializers.HyperlinkedModelSerializer):
    tag = TagSerializer(read_only=True, many=True)
    main_text = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Post
        exclude = (
            "title_en",
            "lead_text_en",
            "main_text_en",
        )
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}

    def get_main_text(self, obj):
        return obj.convert_markdown_to_html()

    def get_created_at(self, obj):
        return obj.build_date(obj.created_at)

    def get_updated_at(self, obj):
        return obj.build_date(obj.updated_at)


class PostEnglishSerializer(PostSerializer):
    title = serializers.SerializerMethodField()
    lead_text = serializers.SerializerMethodField()
    main_text = serializers.SerializerMethodField()

    class Meta:
        model = Post
        exclude = (
            "title_en",
            "lead_text_en",
            "main_text_en",
        )
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug", "view_name": "post_en_detail"}}

    def get_title(self, obj):
        return obj.title_en if obj.title_en is not None else obj.title

    def get_lead_text(self, obj):
        return obj.lead_text_en if obj.lead_text_en is not None else obj.lead_text

    def get_main_text(self, obj):
        return obj.convert_english_markdown_to_html()
