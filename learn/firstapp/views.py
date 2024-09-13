from django.shortcuts import render
from .models import User
from django.shortcuts import get_object_or_404

# Create your views here.
def all_firstapp(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'firstapp/all_firstapp.html', context)

def details_firstapp(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'firstapp/details_firstapp.html', {'user': user})