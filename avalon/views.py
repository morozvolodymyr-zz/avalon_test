from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from avalon.tools_ui import get_user_appointments, save_appointment, join_appointment, get_appointment


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


@csrf_exempt
@api_view(['POST', 'GET'])
def personal_page_view(request):
    if request.user.is_authenticated():
        username = request.user.username
        if request.method == 'POST':
            try:
                name = request.data['name']
                description = request.data['description']
                dates = request.data['dates']
                times = request.data['times']
                save_appointment(username, name, description, dates, times)
            except:
                return Response({'Error': 'You must fill all fields.'}, status=status.HTTP_400_BAD_REQUEST)
            return Response(get_user_appointments(username))
    else:
        return render(request, 'login.html', {'error': 'error in login'})


@csrf_exempt
@api_view(['POST', 'GET'])
def appointment_view(request):
    appointment_id = request.query_params.get('appointment_id', None)
    if not appointment_id:
        return Response({'Error': 'There is no appointment id'}, status=status.HTTP_400_BAD_REQUEST)
    appointment = get_appointment(appointment_id)
    if not appointment:
        return Response({'Error': 'There is no appointment with this id'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        try:
            if request.user.is_authenticated():
                is_logined = True
                username = None
                email = None
            else:
                is_logined = False
                username = request.data['username']
                email = request.data['email']
            date = request.data['date']
            time = request.data['time']
            join_appointment(appointment_id, date, time, is_logined, username, email)
        except:
            return Response({'Error': 'You must fill all fields.'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(appointment)
