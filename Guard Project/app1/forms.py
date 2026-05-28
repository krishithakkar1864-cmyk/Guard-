from django import forms
from .models import Employee, Booking

class Employeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields='__all__'

        # New Booking form
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'customer_name', 'customer_email', 'booking_date', 'booking_time', 'additional_notes']
        widgets = {
            'service': forms.Select(attrs={'class': 'form-control'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'booking_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'booking_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'additional_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Any special instructions...'}),
        }