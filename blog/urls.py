from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('posts', views.PostViewSet)
router.register('tags', views.TagViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
