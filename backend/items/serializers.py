from .models import Item, Keyboard, Vendor, Listing
from rest_framework import serializers
import json

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'