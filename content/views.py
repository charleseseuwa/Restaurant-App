from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact
from .models import Subscriber
from .models import Service
from .models import Menu
from .forms import BookingForm
from .models import Booking
# Create your views here.
def index_page(request):
    if request.method == "GET":
        all_services = Service.objects.all()
        all_menu = Menu.objects.all()

        context = {
            'all_services' : all_services,
            'all_items' : all_menu

        }
        new_subscriber_email = request.GET
    elif request.method == "POST":
        new_subscriber_email = request.POST.get("email")
        Subscriber.objects.create(email=new_subscriber_email)
        return redirect("index.html")
    return render(request, 'content/index.html', context)

def about_page(request):
    return render(request, 'content/about.html')

def service_page(request):
    return render(request, 'content/service.html')

def team_page(request):
    return render(request, 'content/team.html')

def testimonial_page(request):
    return render(request, 'content/testimonial.html')

def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid(): 
           form.save()
           return HttpResponse("We have recieved your message")

    elif request.method == "GET":
        form = ContactForm()
    context = {
    "form": form
    }

    return render(request, 'content/contact.html', context)

    
 
def menu_page(request):

    return render(request, 'content/booking.html')
    

def booking_page(request):
   if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid(): 
           form.save()

   elif request.method == "GET":
        form = BookingForm()
        context = {
        "form": form
        }

        return render(request, 'content/booking.html', context)

   return HttpResponse("We have recieved your message")

    
    