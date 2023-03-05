from django.db.models.signals import post_save
from django.dispatch import receiver

from user_profile.models import UserProfile


@receiver(post_save, sender='auth.User')
def create_profile(sender, instance, created, **kwargs):
    """
    Create a user profile when registering a new account
    """
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender='auth.User')
def save_profile(sender, instance, created, **kwargs):
    """
    Save a user profile when registering a new account
    """
    instance.profile.save()
