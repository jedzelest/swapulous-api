"""
URL mappings for Item app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter
from item import views

router = DefaultRouter()
router.register('item', views.ItemViewSet)

app_name = 'item'

urlpatterns = [
    path('', include(router.urls)),
]
