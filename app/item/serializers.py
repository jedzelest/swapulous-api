"""
Serializers for the item APIs.
"""

from rest_framework import serializers

from core.models import Item


class ItemSerializer(serializers.ModelSerializer):
    """Serializer for items."""

    class Meta:
        model = Item
        fields = ['id', 'is_available', 'condition',
                  'description', 'isFree', 'name',
                  'category', 'sub_category',
                  'price', 'short_info', 'state', 'status',
                  'version']
        read_only_fields = ['id']


class ItemDetailSerializer(ItemSerializer):
    """Serializer for item detail view."""

    class Meta(ItemSerializer.Meta):
        fields = ItemSerializer.Meta.fields + ['image']


class ItemImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading image to an item."""

    class Meta:
        model = Item
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image': {'required': 'True'}}
