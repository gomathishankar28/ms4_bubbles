from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contactform', views.contactform, name='contactform'),
    path('contact_ack/', views.contact_ack, name='contact_ack'),
]