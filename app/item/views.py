"""
Views for the Item APIs.
"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Item
from item import serializers


class ItemViewSet(viewsets.ModelViewSet):
    """View for manage Item APIs."""
    serializer_class = serializers.ItemSerializer
    queryset = Item.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve items for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')
