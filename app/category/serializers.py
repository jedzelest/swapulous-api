"""
Serializers for category APIs.
"""
from rest_framework import serializers
from core.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Categories."""

    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']


class CategoryDetailSerializer(CategorySerializer):
    """Serializer for category detail view."""

    class Meta(CategorySerializer.Meta):
        fields = CategorySerializer.Meta.fields
