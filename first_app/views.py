from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("this is hime first app page")
def courses(request):
    return HttpResponse("this is courses page")

def about(request):
    return HttpResponse("This is about pagae first app")