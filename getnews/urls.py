from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('home/',TemplateView.as_view(template_name = 'home.html'), name = 'home'),
    path('mainpage/', views.mainpage, name = 'mainpage'),
    path('signup/', views.signup, name = 'signup'),
    path('country/',views.country, name = 'country'),
    path('source/', views.source, name = 'source'),
    path('date/', views.date, name = 'date')
]