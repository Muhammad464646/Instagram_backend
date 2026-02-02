from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StoryViewSet, StoryViewViewSet

router = DefaultRouter()
router.register(r'stories', StoryViewSet, basename='story')
router.register(r'story-views', StoryViewViewSet, basename='storyview')

urlpatterns = [
    path('', include(router.urls)),
]
