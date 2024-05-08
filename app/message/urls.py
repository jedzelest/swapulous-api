"""
URL mapping for the message app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter
from message import views

router = DefaultRouter()
router.register('message', views.MessageViewSet)

app_name = 'message'

urlpatterns = [
    path('', include(router.urls)),
]
