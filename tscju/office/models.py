from django.db import models

# Create your models here.

class Room (models.Model):
    roomNo = models.CharField(max_length=3, null=True)
    roomType = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.roomNo



class Organisation (models.Model):

    ACCESSORIES = (
        ('Musical', 'Musical'),
        ('Computer', 'Computer'),
        ('Technology', 'Technology'),
        ('Travelling', 'Travelling'),
        ('Others', 'Others')
    )

    name = models.CharField(max_length=200, blank=True)
    id = models.IntegerField(max_length=7, primary_key=True)
    roomNo = models.ForeignKey(Room, on_delete=models.CASCADE, max_length=3, null=True)
    accessories = models.CharField(max_length=200, null=True, choices=ACCESSORIES)
    sitting = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.name


class Guest (models.Model):
    name = models.CharField(max_length=200, null=True)
    id = models.AutoField(max_length=3, primary_key=True)
    address = models.CharField(max_length=300, null=True)
    phone = models.IntegerField(max_length=12, null=True)
    roomNo = models.ForeignKey(Room, on_delete=models.CASCADE, max_length=3, null=True)
    bookingDate = models.DateField(null=True)
    stayingStart = models.DateField(null=True)
    stayingEnd = models.DateField(null=True)


    def __str__(self):
        return self.name

class Teacher (models.Model):
    name = models.CharField(max_length=200, null=True)
    id = models.IntegerField(max_length=3, primary_key=True)
    phone = models.IntegerField(max_length=12, null=True)
    roomNo = models.IntegerField(max_length=3, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name


class Muktomoncho (models.Model):
    bookingDate = models.DateField(null=True)
    bookedBy = models.CharField(max_length=200, null=True)
    eventType = models.CharField(max_length=200, null=True)
    eventDate = models.DateField(null=True)
    eventName = models.CharField(max_length=200, null=True)
    id = models.AutoField(max_length=3, primary_key=True)

    def __str__(self):
        return self.eventName

class Appointment (models.Model):
    name = models.CharField(max_length=200, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    phone = models.IntegerField(max_length=12, null=True)
    time = models.DateTimeField()
    id = models.AutoField(max_length=3, primary_key=True)

    def __str__(self):
        return self.name