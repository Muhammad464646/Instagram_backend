# social/serializers.py
from rest_framework import serializers
from .models import Follow
from django.contrib.auth import get_user_model

User = get_user_model()

class FollowSerializer(serializers.ModelSerializer):
    follower_username = serializers.CharField(source='following.username', read_only=True)

    class Meta:
        model = Follow
        fields = ['following', 'follower_username', 'created_at']
        read_only_fields = ['follower_username']
   
    def validate(self, attrs):
        request = self.context["request"]
        follower = request.user
        following = attrs.get("following")
        print('aasasdasd',attrs)

        if self.context['request'].user == attrs.get('following'):
            raise serializers.ValidationError(["You cannot follow yourself."])

        if Follow.objects.filter(follower=follower, following=following).exists():
            raise serializers.ValidationError(["You are already subscribed to this user."])

        return attrs


class FollowingSerializer(serializers.ModelSerializer):
    following_username = serializers.CharField(source='follower.username', read_only=True)

    class Meta:
        model = Follow
        fields = ['follower','following_username', 'created_at']