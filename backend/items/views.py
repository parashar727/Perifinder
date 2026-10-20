from django.shortcuts import render
from .models import Item, Keyboard, Vendor, Listing
from .serializers import ItemSerializer
from rest_framework import viewsets

# Create your views here.

class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()