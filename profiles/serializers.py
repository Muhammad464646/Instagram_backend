from rest_framework import serializers
from .models import Profile

class ProfileSerializers(serializers.ModelSerializer):
    email=serializers.EmailField(source='user.email')
    class Meta:
        model=Profile
        fields=['gender','bio','is_private','email']

    
    
    def update(self, instance, validated_data):
        user=validated_data.pop('user',{})
        email=user.get('email')
        if email:
            instance.user.email=email
            instance.user.save()
        return super().update(instance, validated_data)