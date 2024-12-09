from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from myapp.models import course
# Create your views here.
def courselist(request):
    allcourse = course.objects.all()
    return render(request, "courselist.html",{"allcourse":allcourse})
