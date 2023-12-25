Customers_Insights Project

The Customers_Insights project is a comprehensive Django web application designed for analyzing and visualizing customer data and sales trends. This project leverages the power of Django, Plotly for interactive visualizations, and Celery for handling asynchronous tasks and scheduled jobs.
Features
Customers Data Analysis App (customers_data)

    Demographic Analysis: Visualizes customer demographics by age and gender.
    Purchase Trend Analysis: Examines purchase trends across different seasons, categories, and locations.
    Aggregated Sales Analysis: Identifies and analyzes the top-selling locations.

Visualizations

    Line Charts and Heatmaps: For purchase trends analysis.
    Bar Charts: For demographic analysis.
    Parallel Categories Diagrams: For aggregated sales data visualization.

Celery Integration

    Asynchronous Tasks Execution: Handles operations that are not required to be performed in real-time.
    Scheduled Tasks: Manages periodic tasks like weekly email notifications.

Setup and Configuration
Prerequisites

    Ensure RabbitMQ is installed and running.
    Verify Django and Plotly configurations.

Running the Application

    Start Django Server:    

    python manage.py runserver

    Access Visualizations:
    Navigate to the customer_demo view in a web browser to see the visualizations.

Using Celery
Launching Celery Worker and Beat

    Start Celery Worker:
    

celery -A celery_tasks worker -l info

Listens for and executes asynchronous tasks.

Start Celery Beat Scheduler:



    celery -A celery_tasks beat -l info

    Schedules and executes periodic tasks.

Task Definition

Tasks are defined in celery_tasks/tasks.py. Each task is a Python function decorated with @shared_task.
Adding Scheduled Tasks

Scheduled tasks are configured in the celery.py file in the celery_tasks app.
Example Task


# celery_tasks/tasks.py

from celery import shared_task

@shared_task
def example_task():
    # Task logic
    pass

Scheduled in celery.py:



# celery_tasks/celery.py

app.conf.beat_schedule = {
    'example-scheduled-task': {
        'task': 'celery_tasks.tasks.example_task',
        'schedule': crontab(hour=8, minute=0, day_of_week=1),
    },
}