from django.urls import path

from budget_tracker_api.api.views import ExpenseView, SingleExpenseView, CategoryView, SingleCategoryView

urlpatterns = (
    # Expenses
    path('expenses/', ExpenseView.as_view(), name='expenses_list'),
    path('expenses/<int:pk>', SingleExpenseView.as_view(), name='single expense'),

    # Categories
    path('category/', CategoryView.as_view(), name='category'),
    path('category/<int:pk>', SingleCategoryView.as_view(), name='single category'),
)
