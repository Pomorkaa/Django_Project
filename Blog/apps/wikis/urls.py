from django.urls import path
from . import views

app_name = 'wikis'
urlpatterns =[
    path('', views.index, name='index'),
    path('<int:wiki_id>/', views.detail,  name='detail')]
