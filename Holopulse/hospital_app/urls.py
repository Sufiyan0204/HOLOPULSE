from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('appointment/', views.appointment, name='appointment'),
    path('emergency/', views.emergency, name='emergency'),
    path('consultation/', views.consultation, name='consultation'),
    path('order_medicine/', views.order_medicine, name='order_medicine'),
    path('data/', views.data_page, name='data_page'),
]