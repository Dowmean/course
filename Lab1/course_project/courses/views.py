# courses/views.py
from django.shortcuts import render
from .models import Course  # หรือโมเดลที่คุณใช้

def course_list(request):
    courses = Course.objects.all()  # ดึงข้อมูลจากฐานข้อมูล
    return render(request, 'courses/course_list.html', {'courses': courses})
