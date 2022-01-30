from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import context

from . forms import *

from .models import *

# Create your views here.


def home(request):

    organisations = Organisation.objects.all()
    context = { 
        'organisations':organisations,
     }
    return render(request, 'office/dashboard.html', context)


def updateSitting(request, pk):

    organisations = Organisation.objects.get(id=pk)
    form = sittingStatus(request.POST)

    if request.method == 'POST':
        form = sittingStatus(request.POST, instance=organisations)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'organisation':organisation, 'form':form}

    return render(request, 'office/updatesitting.html', context)



def muktomoncho(request):

    muktomoncho = Muktomoncho.objects.all()
    context = {
        'muktomoncho' : muktomoncho,
    }
    return render(request, 'office/muktomoncho.html', context)

def guestroom(request):

    guestroom = Guest.objects.all()
    context = {
        'guestroom':guestroom,
    }

    return render(request, 'office/guestroom.html', context)


def organisation(request, pk):
    organisation = Organisation.objects.get(id=pk)

    context = {'organisation':organisation}

    return render(request, 'office/organisations.html', context)


def addEvent(request):

    form = addEventForm()
    if request.method == 'POST':
        form = addEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form}

    return render(request, 'office/addevent.html', context)


def updateEvent(request, pk):
    event = Muktomoncho.objects.get(id=pk)
    form = addEventForm(instance=event)

    if request.method == 'POST':
        form = addEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'event':event, 'form':form}

    return render(request, 'office/addevent.html', context)


def deleteEvent(request, pk):

    event = Muktomoncho.objects.get(id=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('/')

    context = {'name':event}
    return render(request, 'office/delete.html', context)


def bookGuestRoom(request):

    form = addGuestRoomBooking()
    if request.method == 'POST':
        form = addGuestRoomBooking(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form}

    return render(request, 'office/guestroombooking.html', context)


def cancelBooking(request, pk):

    guest = Guest.objects.get(id=pk)
    if request.method == 'POST':
        guest.delete()
        return redirect('/')

    context = {'name':guest}
    return render(request, 'office/delete.html', context)