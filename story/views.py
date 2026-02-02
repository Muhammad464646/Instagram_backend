from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import Story, StoryView
from .serializers import StorySerializer, StoryViewSerializer

class StoryViewSet(viewsets.ModelViewSet):
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        now = timezone.now()
        return Story.objects.filter(expires_at__gt=now).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class StoryViewViewSet(viewsets.ModelViewSet):
    serializer_class = StoryViewSerializer
    permission_classes = [IsAuthenticated]
    queryset = StoryView.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
