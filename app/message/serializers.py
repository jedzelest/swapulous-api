"""
Serializers for the message APIs.
"""

from rest_framework import serializers

from core.models import Message


class MessageSerializer(serializers.ModelSerializer):
    """Serializer for Message."""

    class Meta:
        model = Message
        fields = ['id', 'content', 'status', 'sender', 'chat_connection']
        read_only_fields = ['id', 'sender']
