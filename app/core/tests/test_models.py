# Tests for models
from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import UserType
from django.urls import reverse

CREATE_USER_URL = reverse('user:create')


class ModelTests(TestCase):
    """ Test models. """

    def test_create_user_with_email_successful(self):
        """ Test creating a user with an email is successful. """
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

        user = get_user_model().objects.create_user(**payload)
        self.assertEqual(user.email, payload['email'])
        self.assertTrue(user.check_password(payload['password']))

    def test_new_user_email_normalized(self):
        """ Test email is normalized for new users. """

        usertype = UserType.objects.create(name='User')
        payload = {
            'email': '',
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
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            payload['email'] = email
            user = get_user_model().objects.create_user(**payload)
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that when creating a user
        without an email raises a ValueError."""

        usertype = UserType.objects.create(name='User')
        payload = {
            'email': '',
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
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(**payload)

    def test_create_superuser(self):
        """ Test creating a superuser. """

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
        user = get_user_model().objects.create_superuser(**payload)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_user_with_birth_date(self):
        """ Test for creating a user with a birthdate. """
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

        user = get_user_model().objects.create_user(**payload)

        self.assertEqual(user.email, payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertEqual(user.birth_date, payload['birth_date'])
        self.assertTrue(user.birth_date)
