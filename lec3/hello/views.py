from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request , "hello/index.html")

def me(request):
    return HttpResponse("Hello, memememememe.")
def david(request):
    return HttpResponse(10*80*3022222, "asdasdasdas")

def greet ( request , name):
    return render (request , "hello/greet.html", {
        "name": name.capitalize()
    })

