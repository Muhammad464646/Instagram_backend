from django.db import models
from users.models import User
from django.utils import timezone
from datetime import timedelta
class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stories")
    media_url = models.URLField()
    media_type = models.CharField(max_length=20)
    expires_at = models.DateTimeField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        now = timezone.now()
        if not self.expires_at:
            self.expires_at = now + timedelta(hours=24)
        super().save(*args, **kwargs)


class StoryView(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="views")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="story_views")
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("story", "user")
