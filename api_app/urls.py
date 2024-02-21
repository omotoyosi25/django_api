from django.urls import path
from . import views




urlpatterns=[
    path('users', views.UserRegistrationEndpoint.as_view(), name='all-users'),
    path('categories', views.UpgradedCategoryEndpoint.as_view(), name='category'),
    path('category/<int:pk>/delete', views.CategoryDeleteEndpoint.as_view(), name='category_delete'),
    path('category/<int:pk>', views.SingleCategoryEndpoint.as_view(), name='category_single'),
    path('products/', views.UpdateProductEndpoint.as_view(), name='products'),
    path('products/<int:pk>',views.SingleProductEndpoint.as_view(),name="productss"),
    path('products/<int:pk>/delete', views.ProductDeleteEndpoint.as_view, name= 'product_delete'),
    path('products-list', views.ProductListEndpoint.as_view(), name="product-list"),
    path('product/<int:product_id>/', views.ProductDetaillEndpoint.as_view(), name="product"),
]