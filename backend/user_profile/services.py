from django.contrib.auth.models import User


def get_user_by_id(user_id: int):
    return User.objects.get(id=user_id)


def update_profile(context: dict, instance: User):
    country = context.get('country') if context.get('country') is not None else instance.profile.country
    city = context.get('city') if context.get('city') is not None else instance.profile.city
    street = context.get('street') if context.get('street') is not None else instance.profile.street
    try:
        phone = int(context.get('phone')) if context.get('phone') is not None else instance.profile.phone
    except ValueError:
        phone = None
    instance.profile.country = country
    instance.profile.city = city
    instance.profile.street = street
    instance.profile.phone = phone
