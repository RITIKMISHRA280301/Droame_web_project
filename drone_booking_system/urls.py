"""drone_booking_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drone_booking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('add_customers',views.add_customers,name='add_customers'),
    path('edit_customers_deatils/<slug:id>',views.edit_customers_deatils,name='edit_customers_deatils'),
    path('delete_customers_details/<slug:id>',views.delete_customers_details,name='delete_customers_details'),
    path('delete_drone_booking/<slug:id>',views.delete_drone_booking,name='delete_drone_booking'),
    path('edit_drone_booking/<slug:id>',views.edit_drone_booking,name='edit_drone_booking'),
    path('book_drone',views.book_drone,name='book_drone'),
    path('login_user',views.login_user,name='login_user'),
    path('log_out',views.log_out,name='log_out'),
    path('dashbord',views.dashbord,name='dashbord'),
    path('customer',views.customer,name='customer'),
    path('booking_details/<slug:id>',views.booking_details,name='booking_details'),
    path('customer_details/<slug:id>',views.customer_details,name='customer_details'),
]
