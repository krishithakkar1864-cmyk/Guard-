from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index,name='index.html'),
    path ('about', views.about,name='about.html'),
    path ('contact', views.contact,name='contact.html'),
    path ('guard', views.guard,name='guard.html'),
    path ('service', views.service,name='service.html'),
    path ('registration', views.registration,name='registration.html'),
    path ('login', views.login,name='login.html'),
    path ('displaydata', views.displaydata,name='displaydata.html'),
    path ('insertdata', views.insertdata,name='insertdata.html'),
    path ('editdata/<int:id>', views.editdata,name='editdata.html'),
    path ('deletedata/<int:id>', views.deletedata,name='deletedata.html'),
    path ('myprofile', views.myprofile,name='myprofile.html'),
    path('success', views.success, name='payment_status')
]