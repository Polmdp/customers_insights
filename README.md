Customers_Insights Project

The Customers_Insights project is a comprehensive Django web application designed for analyzing and visualizing customer data and sales trends. This project not only leverages the power of Django and Plotly for interactive visualizations but also incorporates Django REST Framework to provide a robust API interface. It is equipped with Celery for handling asynchronous tasks and scheduled jobs, enhancing the application's efficiency and user experience.

Features


Customers Data Analysis App (customers_data)

    Demographic Analysis: Visualizes customer demographics by age and gender using interactive Plotly charts.
    Purchase Trend Analysis: Examines purchase trends across different seasons, categories, and locations, offering insights through dynamic visualizations.
    Aggregated Sales Analysis: Identifies and analyzes the top-selling locations to provide strategic business insights.

RESTful API Interface

    API Integration: Utilizes Django REST Framework 


Asynchronous Task Processing with Celery

    Asynchronous Execution: Implements Celery to manage tasks that do not require real-time processing, improving the application's performance.
    Scheduled Jobs: Uses Celery Beat for regular, scheduled tasks like automated data updates or periodic notifications.

Setup and Configuration
Prerequisites

    Ensure RabbitMQ and Celery are installed and correctly configured as part of the project setup.
    Verify the setup for Django REST Framework and ensure it aligns with the application's requirements.

Running the Application

    Start Django Server: Run the Django server to access the web application and API.
    Access Visualizations: Navigate to the customer_demo view in a web browser to view the interactive data visualizations.
    Utilize API: Interact with the RESTful API endpoints for custom data requests and actions.

Using Celery

    Start Celery Worker: Launch the Celery worker to process asynchronous tasks.
    Start Celery Beat Scheduler: Initiate the Celery Beat scheduler for executing periodic tasks.