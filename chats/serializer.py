from rest_framework import serializers
from .models import Chat,Message
from django.db.models import Q

class ChatsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chat
        fields=['id','user_2','user_1']
        read_only_fields=['user_1']

    
    def validate(self,attrs):
        user_1=self.context['request'].user
        user_2=attrs.get('user_2')       
        if Chat.objects.filter(Q(user_1=user_1,user_2=user_2)| Q(user_1=user_2,user_2=user_1)).exists():
            raise serializers.ValidationError('You already chat with him')
        return attrs



class MessageSerializer(serializers.ModelSerializer):
    sender=serializers.CharField(source='sender.username',read_only=True)
    class Meta:
        model=Message
        fields=['text','media_url','chat','sender']
    
    
    def validate_chat(self, value):
        user = self.context['request'].user
        if value.user_1 != user and value.user_2 != user:
            raise serializers.ValidationError("You are not a member of this chat")
        return value
    