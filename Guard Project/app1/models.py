from django.db import models

# Create your models here.

class Contacts(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=20)
    phone=models.CharField(max_length=10)
    message=models.TextField(null=True)

class Guard(models.Model):
    guardImg=models.ImageField(upload_to="static/images")
    guardName=models.CharField(max_length=255)
    guardDesignation=models.CharField(max_length=255)

class Services(models.Model):
    servicesImg=models.ImageField(upload_to="static/images")
    servicesName=models.CharField(max_length=255)
    servicesDescription=models.TextField(max_length=255)

class Registration(models.Model):
    fname=models.CharField(max_length=255,null=True)
    lname=models.CharField(max_length=255,null=True)
    email=models.EmailField(max_length=20,null=True)
    password=models.CharField(max_length=20,null=True)

class Employee(models.Model):
    eid=models.IntegerField(max_length=7)
    ename=models.CharField(max_length=50)
    eemail=models.EmailField(max_length=255)
    econtact=models.CharField(max_length=10)

class Booking(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=100)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    additional_notes = models.TextField(blank=True, null=True)

class Book(models.Model):
    name = models.CharField(max_length=100)
    phone =models.CharField(max_length=10,null=True)
    email = models.EmailField(max_length=25)
    modelselection = models.CharField(max_length=20)
    amount = models.CharField(max_length=5)
    message = models.TextField()
    order_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
 
    def __str__(self):
        if self.paid == True:
            return self.name + " paid"
        else:
            return self.name + " not paid"
