"""
URL mapping for the item image app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter
from item_image import views

router = DefaultRouter()
router.register('item_image', views.ItemImageViewSet)

app_name = 'item_image'

urlpatterns = [
    path('', include(router.urls)),
]
