from django.shortcuts import render, redirect
from django.contrib import auth

# Create your views here.


def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return render(request, '00inicio/base.html')
    return render(request, '00inicio/inicio_sesion.html')
