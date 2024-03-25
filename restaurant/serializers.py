from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Review, Restaurant


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class TokenPairSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def validate(self, attrs):
        return attrs


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())  

    class Meta:
        model = Review
        fields = ['id', 'owner', 'restaurant', 'rating', 'comment']

    def validate_user(self, value):
        if not value:
            raise serializers.ValidationError("Invalid user.")
        return value


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['comment']
    

class RestaurantSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    average_rating = serializers.SerializerMethodField()
    reviews = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'description', 'reviews', 'average_rating', 'owner', 'latitude', 'longitude']

    def validate_created_by(self, value):
        if not value:
            raise serializers.ValidationError("Invalid user.")
        return value

    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            total_ratings = sum(review.rating for review in reviews)
            return total_ratings / len(reviews)
        return None
    