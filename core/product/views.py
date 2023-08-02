from django.shortcuts import render
from django.views.generic import DetailView, ListView
from product.models import Trip
from company.models import Company , Manager, Document, Contacts
import random
from django.http import HttpResponse, Http404


    
class ShowProductListView(ListView):
    template_name = 'index.html'
    context_object_name = 'data'
    
    def get_queryset(self):
        data = {}
        data['trip'] = Trip.objects.all()[:10]
        data['manager'] = random.sample(list(Manager.objects.all()), 2)
        data['agent'] = random.sample(list(Company.objects.all()), 2)
        data['bonus'] = Company.objects.filter(referal=True)
        data['documents'] = Document.objects.all() 
        data['contacts'] = Contacts.objects.all() 
        
          

        return data
    
    
class TripListView(ListView):
    template_name = 'trip.html'
    context_object_name = 'data'
    
    def get_queryset(self):
        data = {}
        data['trip'] = Trip.objects.all()
        return data
    
def detail_trip(request, id):
    try:
        trip = Trip.objects.get(id=id)
    except Exception:
        return Http404('Экскурсия не найдена!')
    return render(request, 'trip-product.html', {'item': trip})
