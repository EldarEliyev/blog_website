from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, blog_list_view, post_detail_view

router = DefaultRouter()
router.register('blog_api', BlogViewSet, basename='blog')

urlpatterns = [
    path('api/', include(router.urls)),

    path('blog/posts/', blog_list_view, name='blog_list'),

    path('blog/posts/<int:pk>/', post_detail_view, name='post_detail'),
]
