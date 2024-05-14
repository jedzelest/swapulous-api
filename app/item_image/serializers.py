"""
Serializers for the Item Image APIs.
"""
from rest_framework import serializers

from core.models import ItemImage


class ImagesSerializer(serializers.ModelSerializer):
    """Serializer for Item Image."""

    class Meta:
        model = ItemImage
        fields = ['id', 'image', 'item', 'user']
        read_only_fields = ['id', 'user']
