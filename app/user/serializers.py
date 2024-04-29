"""
Serializers for the user API view.
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
    )
from rest_framework import serializers
from rest_framework.response import Response
from django.utils.translation import gettext as _


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user subject."""

    class Meta:
        model = get_user_model()
        fields = [
            'id', 'email', 'password', 'first_name', 'last_name',
            'birth_date', 'gender', 'phone_number', 'cover_photo_path',
            'profile_image_path', 'bio', 'city', 'address', 'country',
            'state', 'street', 'zip_code', 'verification_code', 'user_type']
        read_only_fields = ['id']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

    def delete(self, request, *args, **kwargs):
        """Delete the user."""
        user = self.get_object()
        user.delete()
        return Response({"message": "User deleted successfully"}, status=204)


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
