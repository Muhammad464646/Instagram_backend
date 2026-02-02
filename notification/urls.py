from django.urls import path
from .views import NotificationView,NotifyDetailView
urlpatterns=[
    path('notify',NotificationView.as_view(),name='notify'),
    path('notify/<int:pk>/',NotifyDetailView,name='notifyDetail')
]