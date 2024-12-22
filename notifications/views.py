from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class NotificationListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.filter(is_read=False)
        data = [
            {
                'id': notification.id,
                'actor': notification.actor.username,
                'verb': notification.verb,
                'target': str(notification.target),
                'timestamp': notification.timestamp,
                'is_read': notification.is_read
            }
            for notification in notifications
        ]
        return Response(data)
    

class MarkNotificationAsReadAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        notification = Notification.object.get(pk = pk, recipient = request.user)
        notification.is_read = True
        notification.save()

        return Response({'message', 'Notification marked as read'})
