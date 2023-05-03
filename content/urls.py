from django.urls import path
from .views import *


urlpatterns = [
    path('', index_page, name= 'index'),
    path('about/', about_page, name= 'about'),
    path('service/', service_page, name='service'),
    path('team/', team_page, name='team'),
    path('testimonial/', testimonial_page, name='testimonial'),
    path('contact/', contact_page, name='contact'),
    path('booking/', booking_page, name='booking'),
    path('menu/', menu_page, name='menu')
]
