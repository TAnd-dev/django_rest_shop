from django_filters import rest_framework as filters
from .models import Item


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
