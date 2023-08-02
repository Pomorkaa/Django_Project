from django.shortcuts import render
from django.views.generic import DetailView, ListView
from product.models import Trip
import random
from django.http import HttpResponse, Http404
# Create your views here.
# class ShowProductListView(ListView):
#     """вывод экскурсий"""
#     paginate_by = 9
#     template_name = 'index.html'
#     queryset = Trip.objects.all()
    
    
# class ProducDetailView(DetailView):
#     """вывод детали экскурсии"""
#     template_name = 'product-item.html'
#     model = Trip

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         other_posts=  Trip.objects.order_by('-data').exclude(id=context['name'].id)[:10]
#         if len(other_posts) < 3:                                                #добавила проверку если меньше 3 обьектов, чтобы выводил все
#             context['other_posts'] = other_posts
#         else:
#             context['other_posts'] = random.sample(list(other_posts), 3)
#         return context
    
    
class ShowProductListView(ListView):
    template_name = 'index.html'
    context_object_name = 'data'
    
    def get_queryset(self):
        data = {}
        data['trip'] = Trip.objects.all()[:10]

        return data
    
    
class TripListView(ListView):
    template_name = 'trip.html'
    context_object_name = 'data'
    
    def get_queryset(self):
        data = {}
        data['trip'] = Trip.objects.all()[:10]

        return data
    
def detail_trip(request, id):
    try:
        trip = Trip.objects.get(id=id)
    except Exception:
        return Http404('Экскурсия не найдена!')
    return render(request, 'trip-product.html', {'item': trip})
