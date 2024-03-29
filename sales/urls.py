from django.urls import path
from django.urls.resolvers import URLPattern 
from .views import (home_view, SalesListView,SalesDetailView)

app_name = 'sales'

urlpatterns = [
    path('', home_view, name = 'home'),
    path('sales/', SalesListView.as_view(), name='list'),
    path('sales/<pk>/', SalesDetailView.as_view(), name='detail'),
]