
from django.contrib import admin
from django.urls import path,include
from APi_App.views import Company_Viewset,Employee_Viewset
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r"company",Company_Viewset)
route.register(r"Employee",Employee_Viewset)
urlpatterns = [
    path("",include(route.urls))
]
