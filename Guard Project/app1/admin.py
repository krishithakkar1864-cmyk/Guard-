from django.contrib import admin

# Register your models here.

from app1.models import *

class ContactsAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','message']
admin.site.register(Contacts,ContactsAdmin)

class AboutGuard(admin.ModelAdmin):
    list_display = ['guardImg','guardName','guardDesignation']
admin.site.register(Guard,AboutGuard)

class OurServices(admin.ModelAdmin):
    list_display = ['servicesImg','servicesName','servicesDescription']
admin.site.register(Services,OurServices)

class OurRegistration(admin.ModelAdmin):
    list_display = ['fname','lname','email','password']
admin.site.register(Registration,OurRegistration)

class EmpList(admin.ModelAdmin):
    list_display = ('eid','ename', 'eemail','econtact')

admin.site.register(Employee,EmpList)

class BookingAdmin(admin.ModelAdmin):
    list_display = ['service', 'customer_name', 'customer_email', 'booking_date', 'booking_time', 'additional_notes']
admin.site.register(Booking, BookingAdmin)