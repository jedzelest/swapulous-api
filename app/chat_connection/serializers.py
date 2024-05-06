"""
Serializers for the chat connection APIs.
"""

from rest_framework import serializers

from core.models import Chat_Connection


class ChatConnectionSerializer(serializers.ModelSerializer):
    """Serializer for Chat Connections."""

    class Meta:
        model = Chat_Connection
        fields = ['id', 'item', 'sender', 'receiver']
        read_only_fields = ['id', 'sender']
