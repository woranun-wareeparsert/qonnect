from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Item, User
from .serializers import ItemSerializer, UserSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def getData(request, format=None):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        items = Item.objects.all()
        serializer_all = ItemSerializer(items, many=True)
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer_all.data)

@csrf_exempt
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def getDataDetail(request, id):
    if id:
        item = Item.objects.get(id=id)
        if request.method == 'GET':
            serializer = ItemSerializer(item)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ItemSerializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        elif request.method == 'DELETE':
            item_value = Item.objects.filter(id=id)
            if item_value:
                item_value.delete()
            return Response('HTTP_204_NO_CONTENT')
    return Response(serializer.errors)
    
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def getUserData(request, format=None):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        users = User.objects.all()
        serializer_all = UserSerializer(users, many=True)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer_all.data)
    
