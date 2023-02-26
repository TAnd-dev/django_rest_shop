from django.urls import path

from shop.views import ItemListView, ItemDetailView, ReviewCreateView, CategoriesView, AddDeleteFavoriteView, \
    FavoriteView

urlpatterns = [
    path('items/', ItemListView.as_view()),
    path('item/<int:pk>/', ItemDetailView.as_view()),
    path('review/', ReviewCreateView.as_view()),
    path('categories/', CategoriesView.as_view()),
    path('add_delete_favorite/', AddDeleteFavoriteView.as_view()),
    path('favorite/', FavoriteView.as_view()),
]
