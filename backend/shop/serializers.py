from rest_framework import serializers

from .models import Item, Review, ProductGallery, Category, Favorite


class RecursiveSerializer(serializers.Serializer):
    """
    Return children of model
    """

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class FilterCategorySerializer(serializers.ListSerializer):
    """
    Return only categories without parents
    """

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class ReviewCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a review
    """

    def create(self, validate_data):
        review = Review.objects.create(
            author=validate_data.get('author'),
            product=validate_data.get('product'),
            text=validate_data.get('text'),
            rate=validate_data.get('rate'),
        )
        return review

    class Meta:
        model = Review
        fields = ('text', 'rate', 'product')


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying a review
    """

    author = serializers.SlugRelatedField(slug_field='username', read_only=True, many=False)

    class Meta:
        model = Review
        fields = ('text', 'rate', 'author', 'created_at')


class ImageListSerializer(serializers.ListSerializer):
    """
    Serializer to return a list of images
    """

    def to_representation(self, data):
        return [str(image.image) for image in data.all()]


class ImageSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying images
    """
    image = serializers.ImageField()

    class Meta:
        list_serializer_class = ImageListSerializer
        model = ProductGallery
        fields = ('image',)


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying items
    """
    category = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    image = ImageSerializer(many=True)

    class Meta:
        model = Item
        fields = ('title', 'description', 'price', 'get_avg_rate', 'image', 'category')


class ItemDetailSerializer(ItemSerializer):
    """
    Serializer for displaying a detail of items
    """
    review = ReviewSerializer(many=True)

    class Meta:
        model = Item
        fields = ('title', 'description', 'price', 'get_avg_rate', 'category', 'image', 'review')


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for displaying categories
    """
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCategorySerializer
        model = Category
        fields = ('name', 'children')


class FavoriteSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying favorites
    """
    class Meta:
        model = Favorite
        fields = ('item',)


class FavoriteDetailSerializer(FavoriteSerializer):
    """
    Serializer for displaying favorites with details
    """
    item = ItemSerializer()
