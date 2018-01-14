from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import FoodSerializer
from .serializers import CategorySerializer
from .models import Food
from .models import Category

# Create your views here.

class FoodViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Food.objects.filter(available=True)
    serializer_class = FoodSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FilteredFoodViewSet(viewsets.ViewSet):
    def list(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        serializer = FoodSerializer(category.food.filter(available=True), many=True)
        return Response(serializer.data)

    def retrieve(self, request, slug, pk):
        category = get_object_or_404(Category, slug=slug)
        food = get_object_or_404(category.food.filter(available=True), pk=pk)
        serializer = FoodSerializer(food)
        return Response(serializer.data)
