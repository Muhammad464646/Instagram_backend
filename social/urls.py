from rest_framework.routers import DefaultRouter
from .views import FollowViewSet
from django.urls import path, include


urlpatterns = [
    path("followers",FollowViewSet.as_view(),name='followers'),
]