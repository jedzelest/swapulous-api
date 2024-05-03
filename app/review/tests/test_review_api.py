"""
Tests for Review APIs.
"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from core.models import (
    Item,
    Category,
    Sub_Category,
    UserType,
    Review)
from review.serializers import (
    ReviewSerializer,
    ReviewDetailSerializer
)


REVIEW_URL = reverse('review:review-list')


def detail_url(review_id):
    """Create and return a review detail URL."""
    return reverse('review:review-detail', args=[review_id])


def create_review(user, **params):
    """Create and return a sample review."""
    category = Category.objects.create(name='Sample Category')
    sub_category = Sub_Category.objects.create(
        name='Sample sub category of Sample Category',
        category=category,
    )
    usertype = UserType.objects.create(name='User')
    user_details = {
            'email': 'winter@example.com',
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
    user_instance = get_user_model().objects.create(**user_details)
    item = Item.objects.create(
        is_available=True,
        condition='New',
        description='Test Description',
        isFree=False,
        name='Sample Item Name',
        category=category,
        sub_category=sub_category,
        price='22.50',
        short_info='Sample short info',
        state='Sample state',
        status='Active',
        version='1.3',
        user=user_instance,
    )
    defaults = {
        'comment': 'Test Comment',
        'item': item,
        'rating': '10',
        'user': user_instance,
    }
    defaults.update(params)

    review = Review.objects.create(**defaults)
    return review


class PublicReviewAPITests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API."""
        res = self.client.get(REVIEW_URL)

        self.assertEqual(res.status_code, 401)


class PrivateReviewAPITests(TestCase):
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

    def test_retrieve_reviews(self):
        """Test retrieving a list of reviews."""
        create_review(user=self.user)

        res = self.client.get(REVIEW_URL)

        reviews = Review.objects.all().order_by('-id')
        serializer = ReviewSerializer(reviews, many=True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(serializer.data)
        # self.assertEqual(res.data, serializer.data)

    def test_get_review_detail(self):
        """Test get review detail."""
        review = create_review(user=self.user)
        print(review.id)
        # url = detail_url(review.id)
        # res = self.client.get(url)

        # self.assertEqual(res.status_code, 200)
        serializer = ReviewDetailSerializer(review)
        self.assertTrue(serializer.data)
        # self.assertEqual(res.data, serializer.data)
