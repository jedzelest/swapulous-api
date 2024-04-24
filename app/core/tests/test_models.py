# Tests for models
# from django.test import TestCase
# from django.contrib.auth import get_user_model


# class ModelTests(TestCase):
#     """ Test models. """

#     def test_create_user_with_email_successful(self):
#         """ Test creating a user with an email is successful. """
#         email = "test@example.com"
#         password = "testpass123"
#         usertype = UserType.objects.create(name='Admin')
#         user = get_user_model().objects.create_user(
#             email=email,
#             password=password,
#             user_type=usertype,
#         )

#         self.assertEqual(user.email, email)
#         self.assertTrue(user.check_password(password))

#     def test_new_user_email_normalized(self):
#         """ Test email is normalized for new users. """

#         usertype = UserType.objects.create(name='Admin')
#         sample_emails = [
#             ['test1@EXAMPLE.com', 'test1@example.com'],
#             ['Test2@Example.com', 'Test2@example.com'],
#             ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
#             ['test4@example.COM', 'test4@example.com'],
#         ]
#         for email, expected in sample_emails:
#             user = get_user_model().objects.create_user(email, 'sample123')
#             self.assertEqual(user.email, expected)

#     def test_new_user_without_email_raises_error(self):
#         """Test that when creating a user
#         without an email raises a ValueError."""

#         usertype = UserType.objects.create(name='Admin')
#         with self.assertRaises(ValueError):
#             get_user_model().objects.create_user('', 'test123')

#     def test_create_superuser(self):
#         """ Test creating a superuser. """

#         usertype = UserType.objects.create(name='Admin')
#         user = get_user_model().objects.create_superuser(
#             'test@example.com',
#             'test123',
#         )

#         self.assertTrue(user.is_superuser)
#         self.assertTrue(user.is_staff)

#     def test_create_user_with_birth_date(self):
#         """ Test for creating a user with a birthdate. """
#         email = "test@example.com"
#         password = "testpass123"
#         birth_date = "August 18, 1999"
#         usertype = UserType.objects.create(name='Admin')
#         user = get_user_model().objects.create_user(
#             email=email,
#             password=password,
#             birth_date=birth_date,
#         )

#         self.assertEqual(user.email, email)
#         self.assertTrue(user.check_password(password))
#         self.assertEqual(user.birth_date, birth_date)
#         self.assertTrue(user.birth_date)
