from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import status

class List_Mixin:
    model_type = None
    serializer = None

    @api_view(['GET'])
    def List(request):
        events = List_Mixin.model_type.objects.all()
        serializer = serializer(events, many=True)
        return Response(serializer.data)

class Update_Mixin:
    model_type = None
    serializer = None

    @api_view(['POST'])
    def Update(request, pk):
        events = Update_Mixin.model_typeobjects.get(id=pk)
        serializer = serializer(instance=events, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class Delete_Mixin:
    model_type = None
    serializer = None

    @api_view(['DELETE'])
    def Delete(request, pk):
        events = Delete_Mixin.model_type.objects.get(id=pk)
        events.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Get_Mixin:
    model_type = None
    serializer = None 

    @api_view(['GET'])
    def Detail(request, pk):
        events = Get_Mixin.model_type.objects.get(id=pk)
        serializer = serializer(events, many=False)
        return Response(serializer.data)

class Post_Mixin:
    serializer = None

    @api_view(['POST'])
    def Create(request):
        serializer = serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)