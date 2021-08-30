from django.urls import path
from .views import *

urlpatterns = [
    path('use/<int:hero_id>/<int:thing_id>/', put_on_inventory,
         name='put_on'),
    path('unuse/<int:hero_id>/<int:thing_id>/', take_off_inventory,
         name='take_off'),
    path('detail/<int:hero_id>/', person_detail,
         name='person_detail'),
    path('', index,
         name='index')
]
