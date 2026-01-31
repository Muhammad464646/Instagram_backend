from django.db import models
from users.models import User

class Chat(models.Model):
    user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chats_as_user1")
    user_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chats_as_user2")
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    text = models.TextField(blank=True)
    media_url = models.URLField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
