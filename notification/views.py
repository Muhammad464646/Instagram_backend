from django.shortcuts import render
from rest_framework.views import APIView
from .models import Notification
from .serializer import NotificationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class NotificationView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        notify=Notification.objects.filter(user=request.user)
        serializer=NotificationSerializer(notify,many=True)
        return Response(serializer.data)

@api_view(['DELETE',"GET"])
def NotifyDetailView(request,pk):
    permission_classes=[IsAuthenticated]
    try:
        notify=Notification.objects.get(pk=pk)
    except Notification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    
    if request.method=="GET":
        serializer=NotificationSerializer(notify)
        return Response(serializer.data)
    

    elif request.method=='DELETE':
        notify.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)