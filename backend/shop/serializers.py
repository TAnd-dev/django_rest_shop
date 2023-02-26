from rest_framework import serializers

from .models import Item, Review, ProductGallery, Category


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
    Add a review
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
    Displaying a review
    """

    author = serializers.SlugRelatedField(slug_field='username', read_only=True, many=False)

    class Meta:
        model = Review
        fields = ('text', 'rate', 'author', 'created_at')


class ImageListSerializer(serializers.ListSerializer):
    """
    Displaying a list of images
    """

    def to_representation(self, data):
        return [str(image.image) for image in data.all()]


class ImageSerializer(serializers.ModelSerializer):
    """
    Displaying an image
    """
    image = serializers.ImageField()

    class Meta:
        list_serializer_class = ImageListSerializer
        model = ProductGallery
        fields = ('image',)


class ItemListSerializer(serializers.ModelSerializer):
    """
    Displaying a list of items
    """
    category = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    image = ImageSerializer(many=True)
    avg_rate = serializers.IntegerField()

    class Meta:
        model = Item
        fields = ('title', 'description', 'price', 'avg_rate', 'image', 'category',)


class ItemDetailSerializer(serializers.ModelSerializer):
    """
    Displaying a detail of items
    """
    category = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    review = ReviewSerializer(many=True)
    image = ImageSerializer(many=True)
    avg_rate = serializers.IntegerField()

    class Meta:
        model = Item
        fields = ('title', 'description', 'price', 'avg_rate', 'category', 'image', 'review')


class CategorySerializer(serializers.ModelSerializer):
    """
    Displaying categories
    """
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCategorySerializer
        model = Category
        fields = ('name', 'children')
