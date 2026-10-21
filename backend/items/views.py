from django.shortcuts import render
from .models import Item, Keyboard, Vendor, Listing
from .serializers import ItemSerializer, KeyboardSerializer, ListingSerializer, KeyboardDetailSerializer
from rest_framework import viewsets

# Create your views here.

class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class KeyboardViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = KeyboardSerializer
    queryset = Keyboard.objects.all()

class ListingViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()

class KeyboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return KeyboardDetailSerializer

        return KeyboardSerializer