from unicodedata import name
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('muktomoncho/', views.muktomoncho, name="muktomoncho"),
    path('guestroom/', views.guestroom, name="guestroom"),
    path('organisation_details/<str:pk>/', views.organisation, name="organisationDetails"),

    path('update_sitting/<str:pk>/', views.updateSitting, name="updatesitting"),

    path('add_event/', views.addEvent, name="addevent"),
    path('update_event/<str:pk>/', views.updateEvent, name="updateevent"),
    path('delete_event/<str:pk>/', views.deleteEvent, name="deleteevent"),

    path('add_guestroom/', views.bookGuestRoom, name="bookguestroom"),
    path('delete_guestroom/<str:pk>/', views.cancelBooking, name="cancelbooking"),
]