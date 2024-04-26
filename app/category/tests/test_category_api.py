"""
Test for Category APIs.
"""
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from core.models import Category
from category.serializers import (
    CategorySerializer,
    CategoryDetailSerializer,
    )


CATEGORY_URL = reverse('category:category-list')


def detail_url(category_id):
    """Create and return a category detail URL."""
    return reverse('category:category-detail', args=[category_id])


def create_category(**params):
    """Create and return a sample category."""
    defaults = {
        'name': 'Sample Category Name',
    }
    defaults.update(params)

    category = Category.objects.create(**defaults)
    return category


class PublicCategoryAPITests(TestCase):
    """Test category requests."""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_categories(self):
        """Test for retrieving a list of categories."""
        create_category()
        create_category(name='Test 2 Category')

        res = self.client.get(CATEGORY_URL)

        categories = Category.objects.all().order_by('-id')
        serializer = CategorySerializer(categories, many=True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, serializer.data)

    def test_get_category_detail(self):
        """Test get category detail."""
        category = create_category(name='Test Category')

        url = detail_url(category.id)
        res = self.client.get(url)

        serializer = CategoryDetailSerializer(category)
        self.assertEqual(res.data, serializer.data)

    def test_create_category(self):
        """Test creating a category."""
        payload = {
            'name': 'Test Category',
        }
        res = self.client.post(CATEGORY_URL, payload)
        self.assertEqual(res.status_code, 201)
        category = Category.objects.get(id=res.data['id'])
        for k, v in payload.items():
            self.assertEqual(getattr(category, k), v)

    def test_update_category(self):
        """Test updating a category."""
        category_data = {'name': 'Test Category'}
        create_response = self.client.post(
            CATEGORY_URL, category_data, format='json')
        self.assertEqual(create_response.status_code, 201)
        created_category_id = create_response.data['id']

        updated_data = {'name': 'Updated Category Name'}
        update_url = f'{CATEGORY_URL}{created_category_id}/'
        update_response = self.client.put(
            update_url, updated_data, format='json')

        self.assertEqual(update_response.status_code, 200)
        updated_category_data = update_response.data
        self.assertEqual(
            updated_category_data['name'],
            'Updated Category Name')

    def test_delete_category(self):
        """Test when deleting a category."""
        category_data = {'name': 'Test Category'}
        create_response = self.client.post(
            CATEGORY_URL, category_data, format='json')
        self.assertEqual(create_response.status_code, 201)
        created_category_id = create_response.data['id']

        delete_url = f'{CATEGORY_URL}{created_category_id}/'
        delete_response = self.client.delete(delete_url)

        # Check if the delete was successful
        self.assertEqual(delete_response.status_code, 204)

        retrieve_response = self.client.get(delete_url)
        self.assertEqual(retrieve_response.status_code, 404)
