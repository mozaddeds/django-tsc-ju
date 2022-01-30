from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from . models import Appointment, Muktomoncho, Guest, Organisation



class addEventForm(ModelForm) :
    class Meta:
        model = Muktomoncho
        fields = '__all__'


class addGuestRoomBooking(ModelForm) :
    class Meta:
        model = Guest
        fields = '__all__'

class sittingStatus(ModelForm):
    class Meta:
        model = Organisation
        fields = ['sitting']


class addAppointmentForm(ModelForm) :
    class Meta:
        model = Appointment
        fields = '__all__'