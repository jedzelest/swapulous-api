"""
Views for the review APIs.
"""

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Item,
    Review,
)
from review import serializers


class ReviewViewSet(viewsets.ModelViewSet):
    """View manage Review APIs."""
    serializer_class = serializers.ReviewSerializer
    queryset = Review.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Override to set the creation of review accordingly."""
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """Retrieve reviews for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.ReviewSerializer

        return self.serializer_class
