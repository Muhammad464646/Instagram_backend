from django.db import models
from users.models import User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    gender = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
