from django.urls import path
from . import views

app_name = 'articles'
urlpatterns =[
    path('', views.index, name='index'),
    path('company', views.company, name='company'),
    path('<int:article_id>/', views.detail, name='detail')]
