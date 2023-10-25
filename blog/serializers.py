from django.utils.safestring import mark_safe
from markdownx.utils import markdownify
from rest_framework import serializers
from .models import Tag, Post


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class PostSerializer(serializers.HyperlinkedModelSerializer):
    tag = TagSerializer(read_only=True, many=True)
    main_text = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

    def get_main_text(self, obj):
        return obj.convert_markdown_to_html()

    def get_created_at(self, obj):
        return obj.build_date(obj.created_at)

    def get_updated_at(self, obj):
        return obj.build_date(obj.updated_at)
