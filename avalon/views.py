from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('personal_page')
    else:
        return render(request, 'login.html', {'error': 'error in login'})


def logout_view(request):
    logout(request)
    return redirect('index')


def personal_page_view(request):
    if request.user.is_authenticated():
        username = request.user.username
        appointments = get_user_appointments()
        # if request.method == 'POST':

    else:
        return render(request, 'login.html', {'error': 'error in login'})
