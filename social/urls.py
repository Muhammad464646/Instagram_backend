from rest_framework.routers import DefaultRouter
from .views import FollowViewSet,FollowersViewSet
from django.urls import path, include


urlpatterns = [
    path("following",FollowViewSet.as_view(),name='following'),
    path("followers",FollowersViewSet.as_view(),name='followers'),
]