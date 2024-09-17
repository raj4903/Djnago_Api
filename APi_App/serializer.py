from rest_framework import serializers
from APi_App.models import *
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    compmpany_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__"
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
