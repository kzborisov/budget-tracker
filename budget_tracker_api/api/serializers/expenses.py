from django.contrib.auth import get_user_model
from rest_framework import serializers

from budget_tracker_api.api.models.expenses import Expense, Category

UserModel = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class ExpenseSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Expense
        fields = '__all__'
