from django.urls import path
from .views import *

urlpatterns = [
    path('use/<int:hero_id>/<int:thing_id>/', use_inventory, name='use'),
    path('unuse/<int:hero_id>/<int:thing_id>/', unuse_inventory, name='unuse'),
    path('detail/<int:hero_id>/', person_detail, name='person_detail'),
    path('', index, name='index')
]
