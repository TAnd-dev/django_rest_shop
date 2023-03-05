from django.contrib.auth.models import User
from rest_framework import serializers

from user_profile.models import UserProfile
from user_profile.services import update_profile


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for user profile
    """
    class Meta:
        model = UserProfile
        fields = ('is_confirm', 'country', 'city', 'street', 'phone')


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user data
    """
    profile = UserProfileSerializer(required=False)
    username = serializers.CharField(allow_blank=True, required=False)

    def update(self, instance, validated_data):
        update_profile(self.context, instance)
        return super().update(instance, validated_data)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'profile')
