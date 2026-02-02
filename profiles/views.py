from django.shortcuts import render
from rest_framework.views import APIView
from .models import Profile
from .serializers import ProfileSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class ProfileViewSet(APIView):
    def get(self,request):
        profile=Profile.objects.filter(user=request.user)
        serializer=ProfileSerializers(profile,many=True)
        return Response(serializer.data)

@swagger_auto_schema(
          method='put',
          request_body=ProfileSerializers,
          responses={
          200: ProfileSerializers(),
          204: "Not found",
          400: "Validation error"  })
@api_view(["GET","PUT","DELETE"])
def ProfileDetailView(request,pk):
    try:
        profile=Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=="GET":
        profile=Profile.objects.get(pk=pk)
        serializer=ProfileSerializers(profile)
        return Response(serializer.data)
    
    elif request.method=="PUT":
        serializer=ProfileSerializers(profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
