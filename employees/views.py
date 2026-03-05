from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils import format_serializer_errors

from .models import Employee
from .serializers import EmployeeSerializer


# Create your views here.
class AddEmployeeView(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = EmployeeSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"data": "Employee added successfully"},
                    status=status.HTTP_201_CREATED
                )

            return Response({'data' : format_serializer_errors(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)


        except Exception as err:
            return Response(
                {"data": "Something went wrong!!!"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
class EmployeeListView(APIView):

    def get(self, request):
        try:
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            return Response({'data' : serializer.data}, status=status.HTTP_200_OK)

        except Exception as err:
            return Response({'data' : 'Something went wrong!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class DeleteEmployeeView(APIView):

    def delete(self, request):
        try:
            id = request.data.get('id',None)
            try:
                employee = Employee.objects.get(pk=id)
                employee.delete()

                return Response(
                    {"message": "Employee deleted successfully"},
                    status=status.HTTP_200_OK
                )

            except Employee.DoesNotExist:
                return Response(
                    {"data": "Employee not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

        except Exception as err:
            return Response(
                {"data": "Something went wrong"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
            


        

        