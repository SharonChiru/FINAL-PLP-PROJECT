#from django.shortcuts import render

# Create your views here.
# events/views.py
from django.shortcuts import render,get_object_or_404
from .models import Category,Vendor
def home(request):
    vendors=Vendor.objects.all()
    context=context={'vendors':vendors}

    return render(request, 'events/home.html',context)

def events_detail(request,pk):
    event=get_object_or_404(Vendor,pk=pk)
    context={'event':event}
    return render (request, 'events/detail.html',context)

def about(request):
    return render(request, 'events/about.html')

def privacy_policy(request):
    return render(request, 'events/privacy_policy.html')




# events/views.py

#from django.shortcuts import render

def service_providers(request, category):
    
    providers = [
        {'name': 'provider name', 'contact': 'provider contact'},
        {'name': 'Provider name', 'contact': 'provider contact'},
        {'name': 'Provider name', 'contact': 'provider contact'},
        {'name': 'Provider name', 'contact': 'provider contact'},
        {'name': 'Provider name', 'contact': 'provider contact'},

        
    ]

    context = {'category': category, 'providers': providers}
    return render(request, 'events/service_providers.html', context)

# events/views.py
#from django.shortcuts import render

def contacts(request):
    return render(request, 'events/contacts.html')



