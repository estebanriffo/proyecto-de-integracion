from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def home(request):
    return render(request, 'autentificacion/home.html')

@login_required
def actividades(request):
    return render(request, 'autentificacion/actividades.html')

def exit(request):
    logout(request)
    return redirect('home')
