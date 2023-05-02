from django import forms
from .models import Contact
from .models import Booking



class ContactForm(forms.ModelForm):
    class Meta:

        model = Contact
        fields = '__all__'

    
class BookingForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    datetime = forms.DateTimeInput()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    
    class Meta:

        model = Booking
        fields = "__all__"