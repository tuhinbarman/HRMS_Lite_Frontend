from rest_framework import serializers
from .models import Attendance
from employees.models import Employee
from employees.serializers import EmployeeSerializer


class AttendanceCreateSerializer(serializers.ModelSerializer):

    employee_id = serializers.SlugRelatedField(
        slug_field="employee_id",
        queryset=Employee.objects.all()
    )

    class Meta:
        model = Attendance
        fields = [
            "employee_id",
            "date",
            "status"
        ]

    
    

    

class AttendanceSerializer(serializers.ModelSerializer):

    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = Attendance
        fields = [
            "employee",
            "date",
            "status"
        ]


