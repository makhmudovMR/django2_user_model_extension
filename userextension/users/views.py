from django.shortcuts import render
from .forms import UserForm, MyAuthenticationForm
from django.http import HttpResponse
from .models import User
from django.contrib.auth import login, logout
# Create your views here.
def home(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            userform.save()
            return HttpResponse('OK')
    userform = UserForm()
    return render(request, 'home.html', context={'userform': userform})


def login_view(request):
    if request.method == 'POST':
        form = MyAuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = User.objects.get(email=email)
            print('*'*50)
            print(type(user))
            print('*'*50)
            if user is not None:
                login(request, user)
                return HttpResponse(f'hello {user.email}')
    form = MyAuthenticationForm()
    return render(request, 'login.html', context={'form': form})