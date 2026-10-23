# items/views.py
from django.shortcuts import render
from .models import Item, Keyboard, Vendor, Listing
from .serializers import ItemSerializer, KeyboardSerializer, ListingSerializer, KeyboardDetailSerializer
from rest_framework import viewsets, filters

# Create your views here.

class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all().order_by('name')

    filter_backends = [filters.SearchFilter]

    search_fields = ['name', 'brand']

class ListingViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()

class KeyboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Keyboard.objects.all().order_by('name')
    serializer_class = KeyboardSerializer

    filter_backends = [filters.SearchFilter]
    
    search_fields = ['name', 'brand']

    def get_serializer_class(self):
        # Return listing embedded version if detail view (do this for Item too)
        if self.action == "retrieve":
            return KeyboardDetailSerializer

        return KeyboardSerializer