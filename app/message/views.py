"""
Views for the Message API
"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Message
from message import serializers


class MessageViewSet(viewsets.ModelViewSet):
    """View for managing Message APIs."""
    serializer_class = serializers.MessageSerializer
    queryset = Message.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    def get_queryset(self):
        """Retrieve chat connections for authenticated user."""
        return self.queryset.filter(sender=self.request.user).order_by('-id')