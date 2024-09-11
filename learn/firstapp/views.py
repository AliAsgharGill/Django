from django.shortcuts import render

# Create your views here.
def all_firstapp(request):
    return render('request', 'firstapp/all_firstapp.html')

def details_firstapp(request):
    return render('request', 'firstapp/details_firstapp.html')