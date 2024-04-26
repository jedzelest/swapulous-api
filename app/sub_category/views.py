"""
Views for the sub-category APIs.
"""

from rest_framework import viewsets
from core.models import Sub_Category
from sub_category import serializers


class SubCategoryViewSet(viewsets.ModelViewSet):
    """View for managing sub-category APIs."""
    serializer_class = serializers.SubCategoryDetailSerializer
    queryset = Sub_Category.objects.all()

    def get_queryset(self):
        """Retrieve sub-categories."""
        return self.queryset.order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.SubCategorySerializer

        return self.serializer_class
