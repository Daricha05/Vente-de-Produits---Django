from django.shortcuts import redirect, render
from .forms import CreateRegisterForm
from django.contrib.auth import authenticate, login, logout


def Register(request):
    form = CreateRegisterForm()

    if request.method == 'POST':
        form = CreateRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            return redirect('login')

    return render(request, 'app_auth/register.html', {'form': form})


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homeProduct')

    return render(request, 'app_auth/login.html')


def Logout(request):
    logout(request)
    return redirect('login')
