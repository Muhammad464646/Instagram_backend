from django.shortcuts import render
from rest_framework import viewsets
from .models import Chat,Message
from .serializer import ChatsSerializer,MessageSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
# Create your views here.

class ChatView(viewsets.ModelViewSet):
    serializer_class=ChatsSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Chat.objects.filter(Q(user_1=self.request.user)| Q(user_2=self.request.user))
    
    def perform_create(self, serializer):
        return serializer.save(user_1=self.request.user)

class MessageView(viewsets.ModelViewSet):
    queryset=Message.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=MessageSerializer

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(
            Q(chat__user_1=user) | Q(chat__user_2=user)
        )
    def perform_create(self, serializer):
        return serializer.save(sender=self.request.user)
