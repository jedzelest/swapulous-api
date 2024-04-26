"""
Serializers for category APIs.
"""
from rest_framework import serializers
from core.models import Category
from sub_category.serializers import SubCategorySerializer


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Categories."""

    sub_categories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'sub_categories']
        read_only_fields = ['id']


class CategoryDetailSerializer(CategorySerializer):
    """Serializer for category detail view."""

    class Meta(CategorySerializer.Meta):
        fields = CategorySerializer.Meta.fields
