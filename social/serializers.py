# social/serializers.py
from rest_framework import serializers
from .models import Follow
from django.contrib.auth import get_user_model

User = get_user_model()

class FollowSerializer(serializers.ModelSerializer):
    following_username = serializers.CharField(source='following.username', read_only=True)

    class Meta:
        model = Follow
        fields = ['following', 'following_username', 'created_at']
        read_only_fields = ['follower','follower_username']
   
    def validate(self, attrs):
        if self.context['request'].user == attrs.get('following'):
            raise serializers.ValidationError("You cannot follow yourself.")
        return attrs

