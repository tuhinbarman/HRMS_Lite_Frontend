from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('add',AddEmployeeView.as_view(),name = 'add-employee' ),
    path('list',EmployeeListView.as_view(),name = 'list-employee' ),
    path('delete',DeleteEmployeeView.as_view(),name = 'delete-employee' ),
]
