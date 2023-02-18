from django.db.models import Avg
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Item
from .serializers import ItemListSerializer, ItemDetailSerializer, ReviewCreateSerializer


class ItemFilter(filters.FilterSet):
    price = filters.RangeFilter()

    class Meta:
        model = Item
        fields = ['price']


class ItemListView(ListAPIView):
    """
    Displaying a list of items
    """

    queryset = Item.objects.all().annotate(avg_rate=Avg('review__rate')).all()
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

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
