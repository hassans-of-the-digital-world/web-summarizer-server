from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import User
from user.serializers import UserSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request):


    if request.method == 'GET':
        serializer = UserSerializer(bbs)
        return Response(serializer.data)

    elif request.method == 'PUT':
        print(request.data)
        serializer = UserSerializer()
        serializer.create(request.data)

        return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
