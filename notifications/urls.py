from django.urls import path
from .views import NotificationListAPIView, MarkNotificationAsReadAPIView

urlpatterns = [
    path('', NotificationListAPIView.as_view(), name= 'notifications'),
    path('<int:pk>/read/', MarkNotificationAsReadAPIView.as_view(), name='mark_as_read'),
]
