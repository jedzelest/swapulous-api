# database models
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.conf import settings
from helpers.models import TrackingModel
import uuid


class UserManager(BaseUserManager):
    # manager for users

    def create_user(self, email, password=None, **extra_fields):
        # Create, save and return a new user
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # creates a new superuser
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class UserType (TrackingModel):
    """Types of User in the system."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin, TrackingModel):
    """User in the system."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    cover_photo_path = models.CharField(max_length=255)
    profile_image_path = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    is_first_login = models.BooleanField(default=True)
    is_email_confirmed = models.BooleanField(default=False)
    is_profile_changed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=10)
    user_type = models.ForeignKey('UserType', on_delete=models.CASCADE)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Category(TrackingModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Sub_Category(TrackingModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Item(TrackingModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_available = models.BooleanField(default=True)
    condition = models.CharField(max_length=255, choices=[
        ('New', 'New'),
        ('Old', 'Old'),
        ('Used', 'Used'),
        ('Used(Like New)', 'Used(Like New)'),
    ])
    description = models.CharField(max_length=255)
    display_image_path = models.CharField(max_length=255)
    isFree = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    sub_category = models.ForeignKey('Sub_Category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    short_info = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=[
        ('Active', 'Active'),
        ('Draft', 'Draft'),
        ('Swapped', 'Swapped'),
    ])
    version = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
