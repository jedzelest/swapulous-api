"""
URL mapping for chat connection app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter
from chat_connection import views

router = DefaultRouter()
router.register('chat_connection', views.ChatConnectionViewSet)

app_name = 'chat_connection'

urlpatterns = [
    path('', include(router.urls)),
]
