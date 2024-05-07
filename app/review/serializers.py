"""
Serializers for the review APIs.
"""

from rest_framework import serializers

from core.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for reviews."""

    class Meta:
        model = Review
        fields = ['id', 'comment', 'item', 'rating']
        read_only_fields = ['id', 'user']


class ReviewDetailSerializer(ReviewSerializer):
    """Serializer view for detail review."""

    class Meta(ReviewSerializer.Meta):
        fields = ReviewSerializer.Meta.fields + ['user']
