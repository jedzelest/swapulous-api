"""
URL mappings for Review app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter
from review import views

router = DefaultRouter()
router.register('review', views.ReviewViewSet)

app_name = 'review'

urlpatterns = [
    path('', include(router.urls)),
]