

from celery import shared_task
from django.core.mail import send_mail

from customers_data.models import Customer


@shared_task
def send_weekly_email():
    """
    Weekly mail to all customers.
    """
    subject = "Subject"
    message = "Content"
    from_email = 'email_host_user@mail.com'  # EMAIL_HOST_USER en settings.py
    recipient_list = Customer.objects.values_list('email', flat=True).filter(email__isnull=False)

    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
    )