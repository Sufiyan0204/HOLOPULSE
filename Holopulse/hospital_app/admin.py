from django.contrib import admin
from .models import Appointment, Emergency, Consultation, MedicineOrder

# Customizing the admin interface
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'date', 'time']  # Display specific fields in the list view

class EmergencyAdmin(admin.ModelAdmin):
    list_display = ['description', 'contact_number']

class ConsultationAdmin(admin.ModelAdmin):
    list_display = ['name', 'query']

class MedicineOrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'medicine_details']

# Register models with custom admin options
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Emergency, EmergencyAdmin)
admin.site.register(Consultation, ConsultationAdmin)
admin.site.register(MedicineOrder, MedicineOrderAdmin)
