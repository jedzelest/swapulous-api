"""
Views for the Item Image API
"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import ItemImage
from item_image import serializers


class ItemImageViewSet(viewsets.ModelViewSet):
    """View for managing Item Image APIs."""
    serializer_class = serializers.ImagesSerializer
    queryset = ItemImage.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve item images for authenticated user."""
        return self.queryset.order_by('-id')
