from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'notifications')
    actor = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'actor_notifications')
    verb = models.CharField(max_length = 255)
    target_content_type = models.ForeignKey(ContentType, on_delete = models.CASCADE)
    target_object_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_content_type', 'target_object_id')
    iss_read = models.BooleanField(default = False)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.actor} {self.verb} {self.target} to {self.recipient}"