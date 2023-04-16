from django.shortcuts import render, HttpResponse

# Create your views here.
def index():
    return HttpResponse("Hello Im Home Page")