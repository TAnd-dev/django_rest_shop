from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .filters import ItemFilter
from .serializers import (ItemSerializer, ItemDetailSerializer, ReviewCreateSerializer, CategorySerializer,
                          FavoriteDetailSerializer, FavoriteSerializer)
from .services import (get_items_with_avg_rate, get_all_categories, get_user_favorite_by_item_id,
                       get_user_favorites_by_user_id, get_item_detail_with_avg_rate)


class ItemListView(ListAPIView):
    """
    Displaying a list of items
    """

    queryset = get_items_with_avg_rate()
    serializer_class = ItemSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ItemFilter


class ItemDetailView(RetrieveAPIView):
    """
    Displaying a detail of items
    """
    queryset = get_item_detail_with_avg_rate()
    serializer_class = ItemDetailSerializer


class ReviewCreateView(CreateAPIView):
    """
    Adding a review
    """
    serializer_class = ReviewCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoriesView(ListAPIView):
    """
    Displaying categories
    """
    queryset = get_all_categories()
    serializer_class = CategorySerializer


class AddDeleteFavoriteView(CreateAPIView):
    """
    Adding or removing a favorite item of user
    """
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        favorite = get_user_favorite_by_item_id(user_id=request.user.pk, item_id=request.POST.get('item'))
        if favorite:
            favorite.delete()
            return Response()
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoriteView(ListAPIView):
    """
    Displaying favorite items of user
    """
    serializer_class = FavoriteDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return get_user_favorites_by_user_id(self.request.user.pk)
