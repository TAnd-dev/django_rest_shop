from django.urls import path

from shop.views import ItemListView, ItemDetailView, ReviewCreateView

urlpatterns = [
    path('items/', ItemListView.as_view()),
    path('item/<int:pk>/', ItemDetailView.as_view()),
    path('review/', ReviewCreateView.as_view()),
]
