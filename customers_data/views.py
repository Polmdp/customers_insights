
import pandas as pd
import plotly.express as px
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from customers_data.models import Customer, Purchase

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Purchase
from django.db.models import Sum




class SalesBySeason(APIView):
    """
    API endpoint that shows sales totals by season.
    """
    def get(self, request, format=None):
        data = Purchase.objects.values('season').annotate(total_sales=Sum('purchase_amount')).order_by('season')
        return Response(data)

class SalesByCategory(APIView):
    """
    API endpoint that shows sales totals by category.
    """
    def get(self, request, format=None):
        data = Purchase.objects.values('category').annotate(total_sales=Sum('purchase_amount')).order_by('category')
        return Response(data)




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


class CustomLoginView(LoginView):
    template_name = "customers_data/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('customers_data:dashboard')

    def form_invalid(self, form):
        messages.error(self.request, "Usuario o contraseña incorrectos")
        return self.render_to_response(self.get_context_data(form=form))


class CustomerDemoView(TemplateView):
    template_name = 'customers_data/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plot_demo = demographic_analysis_plot()
        plot_trend_line, plot_trend_heat = purchase_trend_plot()
        plot_parallel_categories = parallel_categories_plot_aggregated()

        context['plot_demo'] = plot_demo
        context['plot_trend_line'] = plot_trend_line
        context['plot_trend_heatmap'] = plot_trend_heat
        context['plot_parallel_categories'] = plot_parallel_categories

        return context
