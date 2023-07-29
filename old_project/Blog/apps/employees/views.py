from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import employees

def employee(request):
    employee = employees.objects.all()
    return render(request, 'employees/list.html', {'employee': employee})


# Create your views here.
