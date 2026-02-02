from rest_framework import serializers
from .models import Story, StoryView

class StorySerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    views_count = serializers.IntegerField(source='views.count', read_only=True) 

    class Meta:
        model = Story
        fields = ['id', 'user', 'media_url', 'media_type', 'created_at','expires_at', 'views_count']
        read_only_fields=['expires_at']


class StoryViewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = StoryView
        fields = ['id', 'story', 'user', 'viewed_at']
        read_only_fields = ['user', 'viewed_at']
