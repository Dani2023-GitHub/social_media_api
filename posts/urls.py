from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostViewSet, CommentViewSet, UserFeedView,
    LikePostAPIView, UnlikePostAPIView
)

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', UserFeedView.as_view(), name='user_feed'),
    path('<int:pk>/like/', LikePostAPIView.as_view, name = 'like_post'),
    path('<int:pk>/unlike/', UnlikePostAPIView.as_view(), name= 'unlike_post')
]
