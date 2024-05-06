"""
Tests for the Chat Connection APIs.
"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from core.models import UserType


CHAT_CONNECTION_URL = reverse('chat_connection:chat_connection-list')


def create_chat_connection(user, **params):
    """Create and return a sample chat connection."""


class PublicChatConnectionAPITests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API."""
        res = self.client.get(CHAT_CONNECTION_URL)

        self.assertEqual(res.status_code, 401)


class PrivateChatConnectionAPITests(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.client = APIClient()
        usertype = UserType.objects.create(name='User')
        user_details = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'first_name': 'Test',
            'last_name': 'User',
            'birth_date': '08/18/1999',
            'gender': 'Male',
            'phone_number': '1211231',
            'bio': 'test_bio',
            'city': 'test_city',
            'address': 'test_address',
            'country': 'test_country',
            'state': 'test_state',
            'street': 'test_street',
            'zip_code': '8000',
            'verification_code': '12112',
            'user_type': usertype,
        }
        self.user = get_user_model().objects.create(**user_details)
        self.client.force_authenticate(self.user)

    def test_retrieve_chat_connections(self):
        """Test retrieving list of Chat Connections."""
