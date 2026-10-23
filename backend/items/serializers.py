# items/serializers.py
from .models import Item, Keyboard, Vendor, Listing
from rest_framework import serializers
import json

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'

class KeyboardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keyboard
        fields = '__all__'

class ListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = '__all__'

# Assume I have to make this for Item too
class KeyboardDetailSerializer(serializers.ModelSerializer):
    listings = ListingSerializer(
        source="listing_set",
        many=True,
        read_only=True
    )

    class Meta:
        model = Keyboard
        fields = "__all__"