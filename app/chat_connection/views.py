"""
Views for Chat connection APIs.
"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from core.models import Chat_Connection, Item
from chat_connection import serializers


class ChatConnectionViewSet(viewsets.ModelViewSet):
    """View for manage Chat Connection APIs."""
    serializer_class = serializers.ChatConnectionSerializer
    queryset = Chat_Connection.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        receiver_id = self.request.data.get('receiver')  # fetch the user id in the req body
        item_id = self.request.data.get('item')  # fetch the item id in the req body
        items = Item.objects.filter(user=receiver_id)  # get all items under the user
        for item in items:  # iterate in the items that is within that user
            if str(item.id) == item_id:  # if it is equal to the item id in the req body
                print('Item Found')  # print
                receiver = get_user_model().objects.get(id=receiver_id)
                receiver_copy = Chat_Connection.objects.create(  # noqa
                    item=item,
                    receiver=self.request.user,
                    sender=receiver
                )
                serializer.save(sender=self.request.user)

    def get_queryset(self):
        """Retrieve chat connections for authenticated user."""
        return self.queryset.filter(sender=self.request.user).order_by('-id')
