from django.urls import path
from .views import *


urlpatterns = [
    path('', index_page, name= 'index.html'),
    path('about.html/', about_page, name= 'about.html'),
    path('service.html/', service_page, name='service.html'),
    path('team.html/', team_page, name='team.html'),
    path('testimonial.html/', testimonial_page, name='testimonial.html'),
    path('contact.html/', contact_page, name='contact.html'),
    path('booking.html/', booking_page, name='booking.html'),
    path('menu.html/', menu_page, name='menu.html')
]