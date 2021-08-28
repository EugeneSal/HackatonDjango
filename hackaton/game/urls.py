from django.urls import path
from .views import *

urlpatterns = [
    path('', use_inventory, name='use'),
    path('1/', print_stats, name='print_stats')
]
