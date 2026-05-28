from django.shortcuts import render,redirect
from app1.models import *
from .forms import BookingForm, Employeeform
from django.contrib import messages
import razorpay

# Create your views here.

def index(request):
    listguardData=Guard.objects.all()
    listservicesData=Services.objects.all()
    listdataserver={
        'listdata1':listguardData,
        'listdata2':listservicesData,
    }
    return render(request,'index.html',listdataserver)
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        formdata=Contacts(name=name,email=email,phone=phone,message=message)
        formdata.save()
    return render(request,'contact.html')
def guard(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking has been submitted successfully!")
            return redirect('guard.html')  # same page
    else:
        form = BookingForm()

    guarddata = Guard.objects.all()
    servicedata = Services.objects.all()
    context = {
        'guarddata1': guarddata,
        'servicedata1': servicedata,
        'form': form
    }
    return render(request,'guard.html')
def service(request):
    return render(request,'service.html')
def registration(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        formdata=Registration(fname=fname,lname=lname,email=email,password=password)
        formdata.save()
        return redirect('login.html')
    return render(request,'registration.html')
def displaydata(request):
    listform=Employee.objects.all()
    # lsdata={
    #     'listformdata':listform
    # }
    return render(request,"displaydata.html",{'listformdata':listform})
def insertdata(request):
    form=Employeeform
    lsdata={
            'formfield':form
        }
    if request.method == 'POST':
            submitform=Employeeform(request.POST)
            submitform.save()
            messages.success(request,"Successfully inserted data!")
            return redirect('displaydata.html')
    
    return render(request,"insertdata.html",lsdata)
def editdata(request,id):   
    listform=Employee.objects.get(eid=id)
    if request.method == 'POST':
            listform=Employee.objects.get(eid=id)
            submitform=Employeeform(request.POST,instance=listform)
            submitform.save()
            messages.success(request," Data edited Successfully !")
            return redirect('displaydata.html')
    else:
            return render(request,"editdata.html",{'editdata':listform})
def deletedata(request,id):
    listform=Employee.objects.all().filter(eid=id)
    listform.delete()
    messages.success(request," Data Deleted Successfully !")
    return redirect('displaydata.html')
def myprofile(request):
    if request.session.has_key('IS_LOGIN'):
        if request.method=="POST":
            rname=request.POST['pname']
            runame = request.POST['puname']
            rpass = request.POST['ppassword']
            emp=Registration.objects.get(email=request.session['email'])
            emp.firstname=rname
            emp.lastname=runame
            emp.password=rpass
            emp.save()
        if "email" in request.session:
                emp=Registration.objects.get(email=request.session['email'])
                listdata10={'emp': emp}
    else:
          return redirect("login")
    return render(request, 'myprofile.html',listdata10)
def login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        formdata=Registration.objects.all().filter(email=email,password=password).count()
        return redirect('index.html')
    return render(request,'login.html')
def booki(request): 
   error_message = None        
   if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        modelselection = request.POST.get('modelselection')
        amount = request.POST.get('amount')
        message = request.POST.get('message')
        client = razorpay.Client(
                auth=('rzp_test_VQhEfe2NCXbbwI', '2ibreCYL78DA3kjOhobCvz0f'))

        razorpay_payment = client.order.create(
                dict(amount=(int(amount)*100), currency='INR'))

        order_id = razorpay_payment['id']

        booking= Book.objects.create(
            name=name,
            phone=phone,
            email = email,
            modelselection = modelselection,
            amount = amount,
            message =message,
            order_id = order_id

        )
        booking.save()
        razorpay_payment['name'] = name
        razorpay_payment['amount']= amount 
        razorpay_payment['order_id'] = order_id
        form = Book(request.POST or None)
        return render(request, 'payment.html', {'razorpay_payment': razorpay_payment})
   form = Book()
   return render(request,'payment.html', {'form': form, 'error_message':error_message})

def success(request):
    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature'],
    }

    client = razorpay.Client(
        auth=('rzp_test_VQhEfe2NCXbbwI', '2ibreCYL78DA3kjOhobCvz0f'))

    try:
        status = client.utility.verify_payment_signature(params_dict)
        razorpay_save = Book.objects.get(
            order_id=response['razorpay_order_id'])
        razorpay_save.razorpay_payment_id = response['razorpay_payment_id']
        razorpay_save.paid = True
        razorpay_save.save()
        
    except Exception as e:
        # Handle exceptions, for example, logging the error
        print(f"Error occurred: {str(e)}")
    return render(request, 'success.html', {'status': False})
