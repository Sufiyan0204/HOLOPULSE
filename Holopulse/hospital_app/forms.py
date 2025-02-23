from django import forms
from .models import Appointment, Emergency, Consultation, MedicineOrder

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

class EmergencyForm(forms.ModelForm):
    class Meta:
        model = Emergency
        fields = '__all__'

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = '__all__'

class MedicineOrderForm(forms.ModelForm):
    class Meta:
        model = MedicineOrder
        fields = '__all__'