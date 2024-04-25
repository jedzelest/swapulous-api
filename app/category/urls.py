"""
URL mappings for the category app
"""

from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter
from category import views

router = DefaultRouter()
router.register('category', views.CategoryViewSet)

app_name = 'category'

urlpatterns = [
    path('', include(router.urls)),
]
