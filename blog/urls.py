from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("posts", views.PostViewSet)
router.register("tags", views.TagViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/en/posts/", views.PostEnglishViewSet.as_view({"get": "list"}), name="post_en_list"),
    path("api/en/posts/<str:slug>/", views.PostEnglishViewSet.as_view({"get": "retrieve"}), name="post_en_detail"),
    path("", views.Top.as_view(), name="top"),
    path("<path:path>", views.Top.as_view(), name="top_sub"),
]
