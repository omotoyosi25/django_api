from django.urls import path
from . import views




urlpatterns=[
    path('category', views.AddCategoryEndpoint.as_view(), name='category'),
    path('products/', views.ProductEndpoint.as_view(), name='products'),
    path('product/<int:product_id>/', views.ProductDetaillEndpoint.as_view(), name="product"),
]