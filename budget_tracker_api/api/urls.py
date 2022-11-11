from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from budget_tracker_api.api.views.expenses import ExpenseView, SingleExpenseView, CategoryView, SingleCategoryView
from budget_tracker_api.api.views.users import UserViewSet

urlpatterns = [
    # Register
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Expenses
    path('expense/', ExpenseView.as_view(), name='expenses_list'),
    path('expense/<int:pk>', SingleExpenseView.as_view(), name='single expense'),

    # Categories    
    path('category/', CategoryView.as_view(), name='category'),
    path('category/<int:pk>', SingleCategoryView.as_view(), name='single category'),
]

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')

urlpatterns += router.urls
