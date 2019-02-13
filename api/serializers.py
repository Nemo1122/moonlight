from rest_framework import serializers
from .models import User, Budget, WasteBook, Category1, Category2, TYPE_CHOICE, ATTR_CHOICES


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    # budgets = BudgetSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'


class Category2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category2
        fields = ('id', 'name', 'fast_code', 'parent', 'icon', 'ordering')


class Category1Serializer(serializers.ModelSerializer):
    c2 = Category2Serializer(many=True, read_only=True)

    class Meta:
        model = Category1
        fields = ('id', 'name', 'fast_code', 'attr', 'c2', 'icon', 'ordering')


class WasteBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteBook
        fields = '__all__'

