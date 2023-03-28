from django.contrib import admin
from .models import customers,drone_booking
# Register your models here.

@admin.register(customers)
class Student_accountAdmin(admin.ModelAdmin):
    list_display=('id','customer_name','email')
    search_fields=('id','customer_name','email')

@admin.register(drone_booking)
class drone_bookingAdmin(admin.ModelAdmin):
    list_display=('id','drone_shot_id','booking_date','location_id')
    search_fields=('id','drone_shot_id','booking_date','location_id')

