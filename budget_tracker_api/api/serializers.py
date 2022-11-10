from rest_framework import serializers

from budget_tracker_api.api.models import Expense, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class ExpenseSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Expense
        fields = '__all__'
