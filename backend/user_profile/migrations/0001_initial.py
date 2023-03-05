# Generated by Django 4.1.7 on 2023-03-05 05:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_confirm', models.BooleanField(default=False, verbose_name='Confirm Email')),
                ('first_name', models.CharField(blank=True, max_length=24, null=True, verbose_name='First name')),
                ('second_name', models.CharField(blank=True, max_length=24, null=True, verbose_name='Second name')),
                ('country', models.CharField(blank=True, max_length=64, null=True, verbose_name='Country')),
                ('city', models.CharField(blank=True, max_length=24, null=True, verbose_name='City')),
                ('street', models.CharField(blank=True, max_length=128, null=True, verbose_name='Street')),
                ('phone', models.BigIntegerField(blank=True, null=True, verbose_name='Phone')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='User Profile')),
            ],
        ),
    ]
