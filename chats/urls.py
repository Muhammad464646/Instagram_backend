from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ChatView,MessageView
router=DefaultRouter()

router.register('chats',ChatView,basename='chats')
router.register('message',MessageView,basename='message')

urlpatterns=[
    path('',include(router.urls))
]