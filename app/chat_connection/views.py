"""
Views for Chat connection APIs.
"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Chat_Connection
from chat_connection import serializers


class ChatConnectionViewSet(viewsets.ModelViewSet):
    """View for manage Chat Connection APIs."""
    serializer_class = serializers.ChatConnectionSerializer
    queryset = Chat_Connection.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    def get_queryset(self):
        """Retrieve chat connections for authenticated user."""
        return self.queryset.filter(sender=self.request.user).order_by('-id')
