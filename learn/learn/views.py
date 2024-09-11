from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. You're at the learn Home index page.")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, world. You're at the learn About index page.")

def contact(request):
    return HttpResponse("Hello, world. You're at the learn Contact index page.")