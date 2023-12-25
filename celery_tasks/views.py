from celery import shared_task
from django.db.models import Sum
from django.shortcuts import render

from customers_data.models import Purchase


# Create your views here.


@shared_task
def sumarizar_ventas():
    total_ventas = Purchase.objects.all().aggregate(Sum('purchase_amount'))['purchase_amount__sum']
    return total_ventas
