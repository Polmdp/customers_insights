from django.db import models

class Customer(models.Model):
    customer_id = models.CharField(max_length=50, unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    mail = models.EmailField()

class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item_purchased = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    purchase_amount = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    size = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    season = models.CharField(max_length=50)
    review_rating = models.IntegerField()
    subscription_status = models.BooleanField()
    payment_method = models.CharField(max_length=50)
    shipping_type = models.CharField(max_length=50)
    discount_applied = models.BooleanField()
    promo_code_used = models.CharField(max_length=50, blank=True, null=True)
    previous_purchases = models.IntegerField()
    frequency_of_purchases = models.CharField(max_length=50, blank=True, null=True)
