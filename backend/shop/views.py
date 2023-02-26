from django.db.models import Avg
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import permissions
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Item, Category
from .serializers import ItemListSerializer, ItemDetailSerializer, ReviewCreateSerializer, CategorySerializer


class ItemFilter(filters.FilterSet):
    """
    Item filters
    """
    price = filters.RangeFilter()

    o = filters.OrderingFilter(
        fields=(
            ('price', 'price'),
            ('review__product', 'review'),
            ('avg_rate', 'rate'),
        )
    )

    class Meta:
        model = Item
        fields = ['price']


class ItemListView(ListAPIView):
    """
    Displaying a list of items
    """

    queryset = Item.objects.annotate(avg_rate=Avg('review__rate')).all()
    serializer_class = ItemListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ItemFilter


class ItemDetailView(RetrieveAPIView):
    """
    Displaying a detail of items
    """
    queryset = Item.objects.annotate(avg_rate=Avg('review__rate'))
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
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
