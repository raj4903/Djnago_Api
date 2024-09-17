from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from APi_App.models import *
from APi_App.serializer import *

class Company_Viewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    
class Employee_Viewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    