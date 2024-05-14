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

    def perform_create(self, serlializer):
        """Override creation of item images."""
        serlializer.save(user=self.request.user)

    def get_queryset(self):
        """Retrieve item images for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')
