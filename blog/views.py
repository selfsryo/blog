from django.views import generic
from rest_framework import pagination, response, viewsets

from .models import Post, Tag
from .permissions import IsAdminOrReadOnly
from .serializers import PostEnglishSerializer, PostSerializer, TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return response.Response(
            {
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "total_pages": self.page.paginator.num_pages,
                "current_page": self.page.number,
                "results": data,
            }
        )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(is_public=True)
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = CustomPagination
    lookup_field = "slug"

    def get_queryset(self):
        queryset = super().get_queryset()

        tag = self.request.query_params.get("tag", None)
        if tag:
            queryset = queryset.filter(tag=tag)

        return queryset


class PostEnglishViewSet(PostViewSet):
    serializer_class = PostEnglishSerializer


class Top(generic.TemplateView):
    template_name = "blog/index.html"
