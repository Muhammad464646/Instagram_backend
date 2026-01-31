from django.db import models
from users.models import User
class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stories")
    media_url = models.URLField()
    media_type = models.CharField(max_length=20)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


class StoryView(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="views")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="story_views")
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("story", "user")
