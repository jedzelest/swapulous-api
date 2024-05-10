"""
Tests for the Message APIs.
"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from core.models import UserType

MESSAGE_URL = reverse('message:message-list')


class PublicMessageAPITests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call the API."""
        res = self.client.get(MESSAGE_URL)

        self.assertEqual(res.status_code, 401)


class PrivateMessageAPITests(TestCase):
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

    def test_retrieve_message(self):
        """Test retrieving list of messages."""

        res = self.client.get(MESSAGE_URL)

        self.assertEqual(res.status_code, 200)
