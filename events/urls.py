
# events/urls.py


# events/urls.py
#from django.urls import path

# events/urls.py
from django.urls import path
from .views import home, who_we_are, our_mission, our_vision, our_values, our_team, service_providers, contact
from .views import events_detail
app_name = 'events'

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/',events_detail,name='detail'),
    path('who-we-are/', who_we_are, name='who_we_are'),
    path('our-mission/', our_mission, name='our_mission'),
    path('our-vision/', our_vision, name='our_vision'),
    path('our-values/', our_values, name='our_values'),
    path('our-team/', our_team, name='our_team'),
    path('service-providers/<str:category>/', service_providers, name='service_providers'),
    path('contact/', contact, name='contact'),
]

