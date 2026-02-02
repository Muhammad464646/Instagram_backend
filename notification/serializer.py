from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    from_user = serializers.CharField(source='from_user.username', read_only=True)
    post_id = serializers.IntegerField(source='post.id', read_only=True)  

    class Meta:
        model = Notification
        fields = ['id', 'user', 'from_user', 'type', 'post_id', 'is_read', 'created_at']
        read_only_fields = ['user', 'from_user', 'post_id', 'type', 'created_at', 'is_read']
