from django.shortcuts import render,redirect,get_object_or_404
from .models import customers,drone_booking
from .forms import customersForm,drone_bookingForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import Group,Permission
from django.contrib.auth import get_user_model

#project home/index page function
def index(request):
    return render(request,'index.html')


# customers details added form function 
@login_required(login_url='/login_user')
@permission_required('drone_booking.add_customers',login_url='/login_user')
def add_customers(request):
    if request.method=="POST":
        form=customersForm(request.POST)
        email=request.POST.get('email',)
        if customers.objects.filter(email=email).count()==0:
            if form.is_valid():
                form.save()
                messages.success(request,'customers details added successfuly')
                return redirect('/customer')
            else:
                messages.error(request,'your data is unvalid please try again')
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request,'customer email already regitsered !')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return render(request,'add_customers.html')
    
#edit customers details
@login_required(login_url='/login_user')
@permission_required('drone_booking.add_customers',login_url='/login_user')
def edit_customers_deatils(request,id):
    get_customer=get_object_or_404(customers,id=id)
    data_list={'customer':get_customer}
    if request.method=="POST":
        form=customersForm(request.POST,instance=get_customer)
        if form.is_valid():
            form.save()
            messages.success(request,'customers details update successfuly')
            return redirect('/customer')
        else:
            messages.error(request,'your data is unvalid please try again')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return render(request,'edit_customers.html',data_list)
        
#def delete customers details
@login_required(login_url='/login_user')
@permission_required('drone_booking.add_customers',login_url='/login_user')
def delete_customers_details(request,id):
    get_customer=get_object_or_404(customers,id=id)
    get_customer.delete()
    messages.success(request,'customers details delete successfuly')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

#booking drone shoot details
@login_required(login_url='/login_user')
@permission_required('drone_booking.add_drone_booking',login_url='/login_user')
def book_drone(request):
    customer=customers.objects.all().order_by('-id')
    data_list={'customer':customer,}
    if request.method=="POST":
        form=drone_bookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'drone booking successfuly book next booking')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request,'your data is unvalid please try again')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return render(request,'drone_booking.html',data_list)
    
#edit drone booking details
@login_required(login_url='/login_user')
@permission_required('drone_booking.add_drone_booking',login_url='/login_user')
def edit_drone_booking(request,id):
    customer=customers.objects.all().order_by('-id')
    get_booking=get_object_or_404(drone_booking,id=id)
    data_list={'booking':get_booking,
               'customer':customer}
    if request.method=="POST":
        form=drone_bookingForm(request.POST,instance=get_booking)
        if form.is_valid():
            form.save()
            messages.success(request,'drone booking details update successfuly')
            return redirect('/dashbord')
        else:
            messages.error(request,'your data is unvalid please try again')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return render(request,'edit_drone_booking.html',data_list)
    
#delete drone booking details
@login_required(login_url='/login_user')
@permission_required('drone_booking.add_drone_booking',login_url='/login_user')
def delete_drone_booking(request,id):
    get_booking=get_object_or_404(drone_booking,id=id)
    get_booking.delete()
    messages.success(request,'drone booking delete successfuly')
    return redirect('/dashbord')

#login page
def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return HttpResponseRedirect('/')
            else:
                logout(request)
                messages.error(request,'Unvaild User id / password . Try again')
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request,'Unvaild User id / password . Try again')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return render(request,'login.html')
    
#log out user
@login_required(login_url='/login_user')
def log_out(request):
    try:
        logout(request)
    except KeyError:
        pass
    return redirect('/')

#user dashbord for booking
@login_required(login_url='/login_user')
@permission_required('drone_booking.add_drone_booking',login_url='/login_user')
def dashbord(request):
    booking=drone_booking.objects.all().order_by('-booking_date')
    customer=customers.objects.all().order_by('-id')
    data_list={'booking':booking,
               'customer':customer}
    return render(request,'dashbord.html',data_list)

@login_required(login_url='/login_user')
@permission_required('drone_booking.add_drone_booking',login_url='/login_user')
def customer(request):
    customer=customers.objects.all().order_by('-id')
    data_list={'customer':customer}
    return render(request,'customer.html',data_list)

@login_required(login_url='/login_user')
@permission_required('drone_booking.add_drone_booking',login_url='/login_user')
def booking_details(request,id):
    get_booking=get_object_or_404(drone_booking,id=id)
    customer_id=str(get_booking.customer_id)
    get_customer=get_object_or_404(customers,id=customer_id)
    data_list={'customer':get_customer,
               'booking':get_booking}
    return render(request,'booking_details.html',data_list)

@login_required(login_url='/login_user')
@permission_required('drone_booking.add_drone_booking',login_url='/login_user')
def customer_details(request,id):
    get_customer=get_object_or_404(customers,id=id)
    customer_id=str(get_customer.id)
    get_booking=drone_booking.objects.filter(customer_id=customer_id)
    data_list={'customer':get_customer,
               'all_booking':get_booking}
    return render(request,'customer_details.html',data_list)