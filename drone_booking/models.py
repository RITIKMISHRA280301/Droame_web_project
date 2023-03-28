from django.db import models
from django.utils import timezone
# Create your models here.


# customers details data table or models
class customers(models.Model):
    id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=13)
    address=models.CharField(max_length=255,blank=True)
    create_deta=models.DateTimeField(default=timezone.now,blank=True)
    def __str__(self):
        data=str(self.id)
        return data


# drone booking data table
class drone_booking(models.Model):
    id=models.AutoField(primary_key=True)
    customer_id=models.ForeignKey(
        "customers", on_delete=models.CASCADE)
    location_id=models.CharField(max_length=255)
    drone_shot_id=models.CharField(max_length=255)
    booking_date=models.DateField()
    create_deta=models.DateTimeField(default=timezone.now,blank=True)
