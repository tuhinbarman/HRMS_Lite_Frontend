from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "employee_id",
            "full_name",
            "email",
            "department"
        ]

    def validate_email(self, value):

        if Employee.objects.filter(email=value).exists():
            raise serializers.ValidationError("Employee with this email already exists")

        return value

    def validate_employee_id(self,value):

        if Employee.objects.filter(employee_id=value).exists():
            raise serializers.ValidationError("Employee with this employee_id already exists")

        return value