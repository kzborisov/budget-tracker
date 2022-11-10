from rest_framework import generics as api_views

from budget_tracker_api.api.models import Expense, Category
from budget_tracker_api.api.serializers import ExpenseSerializer, CategorySerializer


class ExpenseView(api_views.ListCreateAPIView):
    """POST/GET requests on on api/expenses/"""
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class SingleExpenseView(api_views.RetrieveUpdateDestroyAPIView):
    """PUT/DELETE/GET on api/expenses/<id>"""
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class CategoryView(api_views.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SingleCategoryView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
