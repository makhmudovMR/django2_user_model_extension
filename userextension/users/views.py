from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            userform.save()
            return HttpResponse('OK')
    userform = UserForm()
    return render(request, 'home.html', context={'userform': userform})