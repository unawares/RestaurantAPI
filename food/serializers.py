from rest_framework import serializers
from .models import Food
from .models import Category
from .models import FoodImage

class FoodImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodImage
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    images = FoodImageSerializer(many=True, read_only=True)

    class Meta:
        model = Food
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
