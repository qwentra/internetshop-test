from django.urls import re_path, path
from . import views

app_name = 'ordersapp'

urlpatterns = [
    path('payment/<int:order>', views.payment, name='payment'),
    re_path(r'^create/$', views.order_create, name='order_create'),
]