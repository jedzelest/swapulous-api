"""
URL mappings for the sub-category app
"""

from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter
from sub_category import views

router = DefaultRouter()
router.register('sub_category', views.SubCategoryViewSet)

app_name = 'sub_category'

urlpatterns = [
    path('', include(router.urls)),
]
