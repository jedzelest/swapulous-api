"""
Views for the Item APIs.
"""

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Item, Sub_Category
from item import serializers


class ItemViewSet(viewsets.ModelViewSet):
    """View for manage Item APIs."""
    serializer_class = serializers.ItemDetailSerializer
    queryset = Item.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Override to set the creation of item accordingly."""
        category_id = self.request.data.get('category')
        requested_sub_category_id = self.request.data.get('sub_category')
        sub_categories = Sub_Category.objects.filter(category=category_id)
        for sub_category in sub_categories:
            if str(sub_category.id) == requested_sub_category_id:
                # print("Found!")
                serializer.save(user=self.request.user)

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request,  pk=None):
        """Upload an image to item."""
        item = self.get_object()
        serializer = self.get_serializer(item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=400)

    def get_queryset(self):
        """Retrieve items for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.ItemSerializer
        elif self.action == 'upload_image':
            return serializers.ItemImageSerializer

        return self.serializer_class
