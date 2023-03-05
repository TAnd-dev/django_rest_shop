from django.urls import path

from user_profile.views import UserView

urlpatterns = [
    path('profile/', UserView.as_view(), name='profile')
]
