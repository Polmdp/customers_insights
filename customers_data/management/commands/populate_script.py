import pandas as pd
from django.core.management.base import BaseCommand

from customers_data.models import Customer, Purchase


class Command(BaseCommand):
    help = "Load a csv file (dateset) into de db"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        data = pd.read_csv(csv_file)

        for _, row in data.iterrows():
            customer, _ = Customer.objects.get_or_create(
                customer_id=row['Customer ID'],
                age=row['Age'],
                gender=row['Gender']
            )

            Purchase.objects.create(
                customer=customer,
                item_purchased=row['Item Purchased'],
                category=row['Category'],
                purchase_amount=row['Purchase Amount (USD)'],
                location=row['Location'],
                size=row.get('Size', ''),
                color=row.get('Color', ''),
                season=row['Season'],
                review_rating=row['Review Rating'],
                subscription_status=row['Subscription Status'] in ['True', 'true', 1, '1'],
                payment_method = row.get('Preferred Payment Method', 'default_value'),
                shipping_type=row['Shipping Type'],
                discount_applied=row['Discount Applied'] in ['True', 'true', 1, '1'],
                promo_code_used=row.get('Promo Code Used', ''),
                previous_purchases=row['Previous Purchases'],
                frequency_of_purchases=row['Frequency of Purchases']
            )
