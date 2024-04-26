"""
Test for Sub_Category APIs.
"""
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from core.models import Category, Sub_Category
from sub_category.serializers import (
    SubCategorySerializer,
    SubCategoryDetailSerializer,
    )


SUB_CATEGORY_URL = reverse('sub_category:sub_category-list')


def detail_url(sub_category_id):
    """Create and return a sub_category detail URL."""
    return reverse('sub_category:sub_category-detail', args=[sub_category_id])


def create_sub_category(**params):
    """Create and return a sample sub_category."""
    category = Category.objects.create(name='Sample Category')
    defaults = {
        'name': "Sample sub-category name",
        'category': category
    }
    defaults.update(params)

    sub_category = Sub_Category.objects.create(**defaults)
    return sub_category


class PublicSubCategoryAPITests(TestCase):
    """Test for sub_category requests."""

    def setUp(self):
        self.category = Category.objects.create(name='Sample Category')
        self.client = APIClient()

    def test_create_sub_category(self):
        """Test for creating a sub_category."""
        payload = {
            'name': 'sample sub-category',
            'category': self.category.id,
        }
        res = self.client.post(SUB_CATEGORY_URL, payload)
        self.assertEqual(res.status_code, 201)
        sub_category = Sub_Category.objects.get(id=res.data['id'])
        self.assertEqual(sub_category.name, res.data['name'])
        self.assertTrue(res.data['category'])

    def test_retrieve_sub_categories(self):
        """Test for retrieving a list of sub-categories."""
        create_sub_category()
        create_sub_category(name='Test name')

        res = self.client.get(SUB_CATEGORY_URL)

        sub_categories = Sub_Category.objects.all().order_by('-id')
        serializer = SubCategorySerializer(sub_categories, many=True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_sub_category_detail(self):
        """Test for retrieving sub_category detail."""
        sub_category = create_sub_category(name='Test name')

        url = detail_url(sub_category.id)
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        serializer = SubCategoryDetailSerializer(sub_category)
        self.assertEqual(res.data, serializer.data)

    def test_update_sub_category(self):
        """Test for updating a single instance of sub_category."""
        data = {
            'name': 'Sample sub_category',
            'category': self.category.id,
        }
        create_response = self.client.post(
            SUB_CATEGORY_URL, data, format='json')
        self.assertEqual(create_response.status_code, 201)
        created_id = create_response.data['id']

        updated_data = {
            'name': 'Updated sub_category',
            'category': self.category.id,
        }
        update_url = f'{SUB_CATEGORY_URL}{created_id}/'
        update_response = self.client.put(
            update_url, updated_data, format='json')

        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.data['name'], 'Updated sub_category')

    def test_delete_sub_category(self):
        """Test for deleting an instance from sub-category."""
        data = {
            'name': 'Sample sub-category',
            'category': self.category.id,
        }
        create_response = self.client.post(
            SUB_CATEGORY_URL, data, format='json')
        self.assertEqual(create_response.status_code, 201)
        created_id = create_response.data['id']

        delete_url = f'{SUB_CATEGORY_URL}{created_id}/'
        delete_response = self.client.delete(delete_url)

        self.assertEqual(delete_response.status_code, 204)
        retrieve_response = self.client.get(delete_url)
        self.assertEqual(retrieve_response.status_code, 404)
