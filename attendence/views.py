from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils import format_serializer_errors
from .models import Attendance
from .serializers import AttendanceSerializer,AttendanceCreateSerializer

# Create your views here.

class MarkAttendanceView(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = AttendanceCreateSerializer(data=data)

            if serializer.is_valid():
                validated_data = serializer.validated_data
                if Attendance.objects.filter(employee = validated_data['employee_id'],
                                             date = validated_data['date'] ).exists():
                    return Response(
                    {"data": "Attendance already marked"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                
                Attendance.objects.create(
                    employee =  validated_data['employee_id'],
                    date = validated_data['date'],
                    status = validated_data['status']
                )

                return Response(
                    {"data": "Attendance marked successfully"},
                    status=status.HTTP_201_CREATED
                )

            return Response({'data' :  format_serializer_errors(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            print(err)
            return Response({'data' : 'Something went wrong!!'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    

class EmployeeAttendanceView(APIView):

    def post(self, request):
        try:
            employee_id = request.data.get('employee_id',None)
            attendance = Attendance.objects.filter(
                employee_id__employee_id=employee_id
            )
            serializer = AttendanceSerializer(attendance, many=True)

            return Response({'data' : serializer.data}, status=status.HTTP_200_OK)
        except Exception as err:
            print('err',err)
            return Response({'data' : 'Something went wrong!!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
