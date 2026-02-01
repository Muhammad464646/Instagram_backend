from django.urls import path,include
from .views import ProfileViewSet,ProfileDetailView
urlpatterns=[
    path('profile',ProfileViewSet.as_view(),name='profile'),
    path('profile/<int:pk>/',ProfileDetailView,name='profileInfo')
]