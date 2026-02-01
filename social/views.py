# social/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Follow
from .serializers import FollowSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

class FollowViewSet(APIView):
    def get(self,request):
        follow=Follow.objects.filter(follower=request.user)
        serializer=FollowSerializer(follow,many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
    request_body=FollowSerializer,
     responses={201: "Created", 400: "Validation error"})
    def post(self,request):
        serializer=FollowSerializer(data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save(follower=request.user)   
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
