"""
Views for the category APIs.
"""

from rest_framework import viewsets
from core.models import Category
from category import serializers


class CategoryViewSet(viewsets.ModelViewSet):
    """View for manage category APIs."""
    serializer_class = serializers.CategoryDetailSerializer
    queryset = Category.objects.all()

    def get_queryset(self):
        """Retrieve categories."""
        return self.queryset.order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.CategorySerializer

        return self.serializer_class
