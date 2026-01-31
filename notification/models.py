from django.db import models
from users.models import User
from posts.models import Post

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_notifications")
    type = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
