from django.contrib.auth.views import LoginView
from django.urls import path

from . import views


app_name = "customers_data"
urlpatterns = [
    path('', views.CustomerDemoView.as_view(), name='dashboard'),
    path('api/sales-by-season/', views.SalesBySeason.as_view(), name='sales-by-season'),
    path('api/sales-by-category/', views.SalesByCategory.as_view(), name='sales-by-category'),


]
