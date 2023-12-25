from django.urls import path

from . import views

app_name = "customers_data"
urlpatterns = [
    path("", views.customer_demo, name="dashboard"),
]
