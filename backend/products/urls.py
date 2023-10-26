from django.urls import path
from . import views

# .../api/products/
urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view()), # leave the path empty because in our cfehome/urls.py we already have the path declared as /api/products and this would create it as /api/products//
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/destroy/', views.ProductDestroyAPIView.as_view())
]