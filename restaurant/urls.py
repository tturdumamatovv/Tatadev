from django.urls import path
from .views import RegisterView, LoginView, RestaurantListCreateView, RestaurantRetrieveUpdateDestroyView, ReviewListCreateView, ReviewRetrieveUpdateDestroyView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('restaurants/', RestaurantListCreateView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantRetrieveUpdateDestroyView.as_view(), name='restaurant-detail'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail'),

]
