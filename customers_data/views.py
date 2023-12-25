import pandas as pd
import plotly.express as px
from django.shortcuts import render
from customers_data.models import Customer, Purchase

def purchase_trend_plot():
    # Obtains and processes purchase data for trend analysis
    purchases = Purchase.objects.all().values('category', 'season', 'location', 'purchase_amount')
    df_purchases = pd.DataFrame(purchases)
    trend_analysis = df_purchases.groupby(['season', 'category', 'location']).sum().reset_index()

    # Generates line and heatmap plots using Plotly
    fig_line = px.line(trend_analysis, x='season', y='purchase_amount', color='category',
                       title="Shopping Trends by Category and Season")
    fig_heatmap = px.density_heatmap(trend_analysis, x='location', y='category', z='purchase_amount',
                                     title='Mapa de Calor de Compras por Ubicación y Categoría')

    return fig_line.to_html(full_html=False), fig_heatmap.to_html(full_html=False)

def demographic_analysis_plot():
    # Analyzes and visualizes customer demographics
    customer = Customer.objects.all().values('age', 'gender')
    df_customer_demo = pd.DataFrame(customer)
    demographic_analysis = df_customer_demo.groupby(['age', 'gender']).size().reset_index(name='count')

    fig_demo = px.bar(demographic_analysis, x='age', y='count', color='gender', barmode="group",
                      title='Customers by Age and Gender')
    return fig_demo.to_html(full_html=False)

def generate_aggregated_data():
    # Aggregates sales data for the top 5 locations
    df_purchases = pd.DataFrame(Purchase.objects.all().values('category', 'season', 'location', 'purchase_amount'))
    total_sales_by_location = df_purchases.groupby('location')['purchase_amount'].sum()
    top_5_locations = total_sales_by_location.sort_values(ascending=False).head(5).index
    df_top_locations = df_purchases[df_purchases['location'].isin(top_5_locations)]

    return df_top_locations

def parallel_categories_plot_aggregated():
    # Visualizes aggregated sales data using parallel categories plot
    df = generate_aggregated_data()
    fig = px.parallel_categories(df, dimensions=['season', 'category', 'location'],
                                 color="purchase_amount", color_continuous_scale=px.colors.sequential.Inferno,
                                 title="Análisis de Categorías Paralelas para las 5 Mejores Localidades")
    return fig.to_html(full_html=False)

def customer_demo(request):
    # Main view that renders all plots in the dashboard
    plot_demo = demographic_analysis_plot()
    plot_trend_line, plot_trend_heat = purchase_trend_plot()
    plot_parallel_categories = parallel_categories_plot_aggregated()

    context = {'plot_demo': plot_demo,
               'plot_trend_line': plot_trend_line,
               'plot_trend_heatmap': plot_trend_heat,
               'plot_parallel_categories': plot_parallel_categories}
    return render(request, 'customers_data/dashboard.html', context)
