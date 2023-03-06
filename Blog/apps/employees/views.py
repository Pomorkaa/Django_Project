from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def test(request):
    return HttpResponse('test')

def companyUSER(request):
    return HttpResponse('Раздел с информацией о сотрудниках компании')

# Create your views here.
