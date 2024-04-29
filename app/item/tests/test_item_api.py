"""
Tests for the Item APIs.
"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from core.models import Item, Category, Sub_Category, UserType
from item.serializers import (
    ItemSerializer,
    ItemDetailSerializer,
)


ITEM_URL = reverse('item:item-list')


def detail_url(item_id):
    """Create and return an item detail URL."""
    return reverse('item:item-detail', args=[item_id])


def create_item(user, **params):
    """Create and return a sample item."""
    category = Category.objects.create(name='Sample Category')
    sub_category = Sub_Category.objects.create(
        name='Sample sub category of Sample Category',
        category=category,
    )
    defaults = {
        'is_available': True,
        'condition': 'New',
        'description': 'Test Description',
        'display_image_path': 'path/samples/sample.jpeg',
        'isFree': False,
        'name': 'Sample Item Name',
        'category': category,
        'sub_category': sub_category,
        'price': '22.50',
        'short_info': 'Sample short info',
        'state': 'Sample state',
        'status': 'Active',
        'version': '1.3',
    }
    defaults.update(params)

    item = Item.objects.create(user=user, **defaults)
    return item


class PublicItemAPITests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API."""
        res = self.client.get(ITEM_URL)

        self.assertEqual(res.status_code, 401)


class PrivateItemAPITests(TestCase):
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
        self.user = get_user_model().objects.create(**user_details)
        self.client.force_authenticate(self.user)

    def test_retrieve_items(self):
        """Test retrieving a list of items."""
        create_item(user=self.user)
        create_item(user=self.user)

        res = self.client.get(ITEM_URL)

        items = Item.objects.all().order_by('-id')
        serializer = ItemSerializer(items, many=True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, serializer.data)

    def test_item_list_limited_to_user(self):
        """Test list of items is limited to authenticated user."""
        usertype = UserType.objects.create(name='User')
        user_details = {
            'email': 'otherUser@example.com',
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
        other_user = get_user_model().objects.create_user(**user_details)
        create_item(user=other_user)
        create_item(user=self.user)

        res = self.client.get(ITEM_URL)

        items = Item.objects.filter(user=self.user)
        serializer = ItemSerializer(items, many=True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, serializer.data)

    def test_get_item_detail(self):
        """Test get item detail."""
        item = create_item(user=self.user)

        url = detail_url(item.id)
        res = self.client.get(url)

        serializer = ItemDetailSerializer(item)
        self.assertEqual(res.data, serializer.data)
