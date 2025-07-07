from django.shortcuts import render
from rest_framework import generics
from apis.genricviews.models import Item
from apis.genricviews.serializers import ItemSerializer

# Create your views here.
class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer