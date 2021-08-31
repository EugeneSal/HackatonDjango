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
         name='index'),
    path('choice/', choice_the_pair,
         name='choice_the_pair'),
    path('arena/<int:hero1_id>/<int:hero2_id>/', arena,
         name='arena'),
]
