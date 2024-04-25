# """
# Test for Category APIs.
# """
# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient

# from core.models import Category, UserType
# from django.contrib.auth import get_user_model
# from category.serializers import CategorySerializer


# CATEGORY_URL = reverse('category:category-list')
# ME_URL = reverse('user:me')

# def create_category(**params):
#     """Create and return a sample recipe."""
#     defaults = {
#         'name': 'Sample Category Name',
#     }
#     defaults.update(params)

#     category = Category.objects.create(**defaults)
#     return category


# class PublicCategoryAPITests(TestCase):
#     """Test unauthenticated category requests."""

#     def setUp(self):
#         self.client = APIClient()

#     def test_auth_required(self):
#         """Test auth is required to call API."""
#         res = self.client.get(CATEGORY_URL)

#         self.assertEqual(res.status_code, 401)


# class PrivateCategoryAPITests(TestCase):
#     """Test authenticated category requests."""

#     def setUp(self):
#         self.client = APIClient()
#         usertype = UserType.objects.create(name='Admin')
#         user_details = {
#             'email': 'test@example.com',
#             'password': 'testpass123',
#             'first_name': 'Test',
#             'last_name': 'User',
#             'birth_date': '08/18/1999',
#             'gender': 'Male',
#             'phone_number': '1211231',
#             'cover_photo_path': 'test_cover',
#             'profile_image_path': 'test_image',
#             'bio': 'test_bio',
#             'city': 'test_city',
#             'address': 'test_address',
#             'country': 'test_country',
#             'state': 'test_state',
#             'street': 'test_street',
#             'zip_code': '8000',
#             'verification_code': '12112',
#             'user_type': usertype,
#         }
#         self.user = get_user_model().objects.create_user(**user_details)
#         self.client.force_authenticate(self.user)

#     def test_if_logged_in_user_is_admin(self):
#         """Test if the current authenticated user is of type Admin."""
#         res = self.client.get(ME_URL)

#     def test_retrieve_categories(self):
#         """Test for retrieving a list of recipes."""
#         create_category()
#         create_category(name='Test 2 Category')

#         res = self.client.get(CATEGORY_URL)

#         categories = Category.objects.all().order_by('-id')
#         serializer = CategorySerializer(categories, many=True)
#         self.assertEqual(res.status_code, 200)
#         self.assertEqual(res.data, serializer.data)

#     def test_category_list_limited_to_user(self):
#         """Test list of categories is limited to authenticated user."""
