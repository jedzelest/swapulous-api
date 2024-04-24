# TESTS for the Django admin modifications
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client
from core.models import UserType


class AdminSiteTests(TestCase):
    # tests for django admin

    def setUp(self):
        """ Create user and client. """
        self.client = Client()

        usertype = UserType.objects.create(name='User')
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User',
            birth_date='08/18/1999',
            gender='Male',
            phone_number='1211231',
            cover_photo_path='test_cover',
            profile_image_path='test_image',
            bio='test_bio',
            city='test_city',
            address='test_address',
            country='test_country',
            state='test_state',
            street='test_street',
            zip_code='8000',
            verification_code='12112',
            user_type=usertype,
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User',
            birth_date='08/18/1999',
            gender='Male',
            phone_number='1211231',
            cover_photo_path='test_cover',
            profile_image_path='test_image',
            bio='test_bio',
            city='test_city',
            address='test_address',
            country='test_country',
            state='test_state',
            street='test_street',
            zip_code='8000',
            verification_code='12112',
            user_type=usertype,
        )

    def test_users_list(self):
        """ Test that users are listed on page. """
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.first_name)
        self.assertContains(res, self.user.last_name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """ Test the edit user page works. """
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """ Test the create user page works. """
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
