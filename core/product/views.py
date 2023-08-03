from django.shortcuts import render , redirect
from django.views.generic import DetailView, ListView
from product.models import Trip
from company.models import Company , Manager, Document, Contacts
import random
from django.http import HttpResponse, Http404
from .forms import ContactForm ,FeedbackForm
from .models import Contact, Feedback

 
 
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
        data['feedback'] = Feedback.objects.all()[:10]      
              

        return data
    
    def post(self, request, *args, **kwargs):
        form = form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request, *args, **kwargs)
    
    
class TripListView(ListView):
    template_name = 'trip.html'
    context_object_name = 'data'
    
    def get_queryset(self):
        data = {}
        data['trip'] = Trip.objects.all()
        data['bonus'] = Company.objects.filter(referal=True)
        data['documents'] = Document.objects.all() 
        data['contacts'] = Contacts.objects.all()      
        return data
    
def detail_trip(request, id):
    try:
        trip = Trip.objects.get(id=id)
    except Exception:
        return Http404('Экскурсия не найдена!')

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FeedbackForm()

    return render(request, 'trip-product.html', {'item': trip, 'form': form})
