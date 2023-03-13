from django.db.models import Avg, QuerySet

from shop.models import Item, Category, Favorite


def get_items_with_avg_rate() -> QuerySet[Item]:
    return Item.objects.annotate(
        avg_rate=Avg('review__rate')). \
        prefetch_related('category'). \
        prefetch_related('image')


def get_item_detail_with_avg_rate() -> QuerySet[Item]:
    return get_items_with_avg_rate(). \
        prefetch_related('review'). \
        prefetch_related('review__author')


def get_all_categories() -> QuerySet[Category]:
    return Category.objects.all()


def get_user_favorite_by_item_id(user_id, item_id) -> Favorite:
    return Favorite.objects.filter(user=user_id, item=item_id).first()


def get_user_favorites_by_user_id(user_id) -> QuerySet[Favorite]:
    return Favorite.objects.filter(user=user_id). \
        annotate(avg_rate=Avg('item__review__rate')). \
        prefetch_related('item__category'). \
        prefetch_related('item__image').all()
