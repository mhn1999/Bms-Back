from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .serializer import RegisterSerializer

from rest_framework.response import Response
\
from rest_framework import permissions, status, generics

from django.conf import settings
from rest_framework.views import APIView
from .models import LeaderBoardMember

# Create your views here.
class PostLeaderBoardData(APIView):
    def post(self, request):
        print(request)
        print("*******")
        serializer = RegisterSerializer(data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": serializer.data}, status=status.HTTP_201_CREATED)
class get_leaderboard_elements(APIView):
    def get(self,requst):
        reviews=LeaderBoardMember.objects.order_by('playTime')
        serializer=RegisterSerializer(reviews,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)