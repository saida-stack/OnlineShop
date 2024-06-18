from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ProductsListView.as_view(), name='products_list'),
    path('detail/<int:pk>/', views.product_detail_view, name='product_detail'),
    path('create/', views.ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
]