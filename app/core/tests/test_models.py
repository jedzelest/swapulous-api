"""
Test for models.
"""
from unittest.mock import patch
from django.test import TestCase
from django.contrib.auth import get_user_model
from core.models import UserType
from core import models
from django.urls import reverse
from rest_framework.test import APIClient

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

    def test_create_category(self):
        """Test for creating a category is successful."""
        category = models.Category.objects.create(
            name='Computer Parts',
        )

        self.assertEqual(str(category), category.name)

    def test_create_sub_category(self):
        """Test for creating a sub-category is successful."""
        category = models.Category.objects.create(
            name='Computer Parts',
        )
        sub_category = models.Sub_Category.objects.create(
            category=category,
            name='Hard Drive',
        )

        self.assertEqual(str(sub_category), sub_category.name)

    def setUp(self):
        self.client = APIClient()
        usertype = UserType.objects.create(name='User')
        payload = {
            'email': 'nayeonnyny@example.com',
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
        self.user = get_user_model().objects.create_user(**payload)
        self.category = models.Category.objects.create(name="Computer Parts")
        self.sub_category = models.Sub_Category.objects.create(
            category=self.category,
            name='Hard Drive'
        )

    def test_create_item(self):
        """Test for creating an item is successful."""
        item = models.Item.objects.create(
            is_available=False,
            condition='New',
            description='Test Description',
            isFree=False,
            name='Test Item',
            category=self.category,
            sub_category=self.sub_category,
            price='20.99',
            short_info='Test info',
            state='Test state',
            status='Active',
            version='1.3',
            user=self.user
        )

        self.assertEqual(str(item), item.name)

    def test_create_review(self):
        """Test for creating a review is successful."""
        item = models.Item.objects.create(
            is_available=False,
            condition='New',
            description='Test Description',
            isFree=False,
            name='Test Item',
            category=self.category,
            sub_category=self.sub_category,
            price='20.99',
            short_info='Test info',
            state='Test state',
            status='Active',
            version='1.3',
            user=self.user
        )
        review = models.Review.objects.create(
            comment='Test Comment',
            item=item,
            rating="10",
            user=self.user,
        )

        self.assertEqual(str(review), review.comment)

    @patch('core.models.uuid.uuid4')
    def test_item_file_name_uuid(self, mock_uuid):
        """Test generating image path."""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.item_image_file_path(None, 'example.jpg')

        self.assertEqual(file_path, f'uploads/item/{uuid}.jpg')

    @patch('core.models.uuid.uuid4')
    def test_user_file_name_uuid(self, mock_uuid):
        """Test generating image path."""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.user_images_file_path(None, 'example.jpg')

        self.assertEqual(file_path, f'uploads/user/{uuid}.jpg')

    def test_create_chat_connection(self):
        """Test for creating a chat connection is successful."""
        usertype = UserType.objects.create(name='User')
        payload = {
            'email': 'sender@example.com',
            'password': 'testpass123',
            'first_name': 'Test',
            'last_name': 'User',
            'birth_date': '08/18/1999',
            'gender': 'Female',
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
        sender = get_user_model().objects.create_user(**payload)
        payload_2 = {
            'email': 'receiver@example.com',
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
        receiver = get_user_model().objects.create_user(**payload_2)
        category = models.Category.objects.create(name="Computer Parts")
        sub_category = models.Sub_Category.objects.create(
            category=category,
            name='Hard Drive'
        )
        item = models.Item.objects.create(
            is_available=False,
            condition='New',
            description='Test Description',
            isFree=False,
            name='Test Item',
            category=category,
            sub_category=sub_category,
            price='20.99',
            short_info='Test info',
            state='Test state',
            status='Active',
            version='1.3',
            user=sender
        )
        chat_conn = models.Chat_Connection.objects.create(
            item=item,
            sender=sender,
            receiver=receiver,
        )

        self.assertEqual(str(chat_conn), chat_conn.item.name)

    def test_create_message(self):
        """Test for creating a message model is successful."""
        usertype = UserType.objects.create(name='User')
        payload = {
            'email': 'sender@example.com',
            'password': 'testpass123',
            'first_name': 'Test',
            'last_name': 'User',
            'birth_date': '08/18/1999',
            'gender': 'Female',
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
        sender = get_user_model().objects.create_user(**payload)
        payload_2 = {
            'email': 'receiver@example.com',
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
        receiver = get_user_model().objects.create_user(**payload_2)
        category = models.Category.objects.create(name="Computer Parts")
        sub_category = models.Sub_Category.objects.create(
            category=category,
            name='Hard Drive'
        )
        item = models.Item.objects.create(
            is_available=False,
            condition='New',
            description='Test Description',
            isFree=False,
            name='Test Item',
            category=category,
            sub_category=sub_category,
            price='20.99',
            short_info='Test info',
            state='Test state',
            status='Active',
            version='1.3',
            user=sender
        )
        chat_conn = models.Chat_Connection.objects.create(
            item=item,
            sender=sender,
            receiver=receiver,
        )
        message = models.Message.objects.create(
            content='Test Content',
            status='Sent',
            sender=sender,
            receiver=receiver,
            chat_connection=chat_conn,
        )

        self.assertEqual(str(message), message.sender.first_name)
