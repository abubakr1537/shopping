from django.shortcuts import render
from .models import *
# Create your views here.

def showStudents(request):
    result = Students.objects.all()
    return render(request, 'students.html', {'results': result})
