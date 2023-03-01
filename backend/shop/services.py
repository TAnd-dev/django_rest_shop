from django.db.models import Avg, QuerySet

from shop.models import Item, Category, Favorite


def get_items_with_avg_rate() -> QuerySet:
    return Item.objects.annotate(avg_rate=Avg('review__rate'))


def get_all_categories() -> QuerySet:
    return Category.objects.all()


def get_user_favorite_by_item_id(user_id, item_id) -> Favorite:
    return Favorite.objects.filter(user=user_id, item=item_id).first()


def get_user_favorites_by_user_id(user_id) -> QuerySet:
    return Favorite.objects.filter(user=user_id)


