
# events/urls.py


# events/urls.py
#from django.urls import path

# events/urls.py
from django.urls import path
from .views import home,service_providers,contacts,about,privacy_policy
from .views import events_detail
app_name = 'events'

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/',events_detail,name='detail'),
    path('about/', about, name='about'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),
    path('service-providers/<str:category>/', service_providers, name='service_providers'),
    path('contacts/', contacts, name='contacts'),
]

