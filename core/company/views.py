from django.shortcuts import render
from django.views.generic import  ListView
from .models import Manager, Company
# Create your views here.


class AboutListView(ListView):
    template_name = 'about.html'
    context_object_name = 'data'
    
    def get_queryset(self):
        data = {}
        data['manager'] = Manager.objects.all()
        data['agent'] = Company.objects.all()

        return data


