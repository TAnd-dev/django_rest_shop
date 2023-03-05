from django.db import models


class UserProfile(models.Model):
    """
    UserProfile model that stores additional information about a user.
    """
    user = models.OneToOneField(
        'auth.User',
        verbose_name='User Profile',
        related_name='profile',
        on_delete=models.CASCADE,
        unique=True
    )
    is_confirm = models.BooleanField(
        verbose_name='Confirm Email',
        default=False
    )
    country = models.CharField(
        max_length=64,
        verbose_name='Country',
        null=True,
        blank=True
    )
    city = models.CharField(
        max_length=24,
        verbose_name='City',
        null=True,
        blank=True
    )
    street = models.CharField(
        max_length=128,
        verbose_name='Street',
        null=True,
        blank=True
    )
    phone = models.BigIntegerField(
        verbose_name='Phone',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.user}'
