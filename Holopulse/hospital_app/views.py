

# Create your views here.
from django.shortcuts import render, redirect
from .forms import AppointmentForm, EmergencyForm, ConsultationForm, MedicineOrderForm

def index(request):
    return render(request, 'index.html')

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})

def emergency(request):
    if request.method == 'POST':
        form = EmergencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmergencyForm()
    return render(request, 'emergency.html', {'form': form})

def consultation(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ConsultationForm()
    return render(request, 'consultation.html', {'form': form})

def order_medicine(request):
    if request.method == 'POST':
        form = MedicineOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MedicineOrderForm()
    return render(request, 'order_medicine.html', {'form': form})



from .models import Appointment, Emergency, Consultation, MedicineOrder

def index(request):
    return render(request, 'index.html')

def data_page(request):
    # Retrieve the data from all the forms
    form1_data = Appointment.objects.all()
    form2_data = Emergency.objects.all()
    form3_data = Consultation.objects.all()
    form4_data = MedicineOrder.objects.all()

    # Pass the data to the template
    context = {
        'form1_data': form1_data,
        'form2_data': form2_data,
        'form3_data': form3_data,
        'form4_data': form4_data,
    }

    return render(request, 'data.html', context)

