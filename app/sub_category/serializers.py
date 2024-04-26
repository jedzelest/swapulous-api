"""
Serializers for sub-category APIs.
"""
from rest_framework import serializers
from core.models import Sub_Category


class SubCategorySerializer(serializers.ModelSerializer):
    """Serializer for Sub-Categories."""

    class Meta:
        model = Sub_Category
        fields = ['id', 'name', 'category']
        read_only_fields = ['id']


class SubCategoryDetailSerializer(SubCategorySerializer):
    """Serializer for sub-category detail view."""

    class Meta(SubCategorySerializer.Meta):
        fields = SubCategorySerializer.Meta.fields
