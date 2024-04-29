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
                  'description', 'display_image_path',
                  'isFree', 'name', 'category', 'sub_category',
                  'price', 'short_info', 'state', 'status',
                  'version', 'user']
        read_only_fields = ['id']
