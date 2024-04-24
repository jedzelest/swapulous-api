"""
Tests for ther user API.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from core.models import UserType

from rest_framework.test import APIClient


CREATE_USER_URL = reverse('user:create')


def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the public features of the user API."""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test creating a user is successful."""
        usertype = UserType.objects.create(name='User')
        payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'first_name': 'Test',
            'last_name': 'User',
            'birth_date': '08/18/1999',
            'gender': 'Male',
            'phone_number': '1211231',
            'cover_photo_path': 'test_cover',
            'profile_image_path': 'test_image',
            'bio': 'test_bio',
            'city': 'test_city',
            'address': 'test_address',
            'country': 'test_country',
            'state': 'test_state',
            'street': 'test_street',
            'zip_code': '8000',
            'verification_code': '12112',
            'user_type': usertype.id,
        }
        res = self.client.post(CREATE_USER_URL, payload)
        print(res.json())
        self.assertEqual(res.status_code, 201)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_with_email_exists_error(self):
        """Test error returned if user with email exists."""
        usertype = UserType.objects.create(name='User')
        payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'first_name': 'Test',
            'last_name': 'User',
            'birth_date': '08/18/1999',
            'gender': 'Male',
            'phone_number': '1211231',
            'cover_photo_path': 'test_cover',
            'profile_image_path': 'test_image',
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
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, 400)

    def test_password_too_short_error(self):
        """Test an error is returned if password is less than 5 chars."""
        usertype = UserType.objects.create(name='User')
        payload = {
            'email': 'test@example.com',
            'password': 'pw',
            'first_name': 'Test',
            'last_name': 'User',
            'birth_date': '08/18/1999',
            'gender': 'Male',
            'phone_number': '1211231',
            'cover_photo_path': 'test_cover',
            'profile_image_path': 'test_image',
            'bio': 'test_bio',
            'city': 'test_city',
            'address': 'test_address',
            'country': 'test_country',
            'state': 'test_state',
            'street': 'test_street',
            'zip_code': '8000',
            'verification_code': '12112',
            'user_type': usertype.id,
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, 400)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)
