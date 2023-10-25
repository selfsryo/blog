from django.db.models import Q
from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets, pagination, response
from .models import Tag, Post
from .permissions import IsAdminOrReadOnly
from .serializers import TagSerializer, PostSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        """ページネーションをカスタマイズ"""
        return response.Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data,
        })


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(is_public=True)
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = CustomPagination
    lookup_field = 'slug'

    def get_queryset(self):
        """GETのパラメータに対応したクエリセットを返す"""
        queryset = super().get_queryset()

        tag = self.request.query_params.get('tag', None)
        if tag:
            queryset = queryset.filter(tag=tag)

        return queryset
