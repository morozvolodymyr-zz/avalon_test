from avalon.models import RegisteredUser, Appointment, Date, Time, Registration


def get_user_appointments(username):
    registrations_obj = Registration.objects.filter(user_username=username)
    registrations = []
    for registration in registrations_obj:
        registrations.append({
            'name': registration.appointment.name,
            'description': registration.appointment.description,
            'date': registration.date.date,
            'time': registration.time.time
        })
    return registrations


def save_appointment(username, name, description, dates, times):
    appointment = Appointment.objects.create(name=name, description=description)
    RegisteredUser.objects.filter(username=username).first().appointments.add(appointment)
    for date in dates:
        Date.objects.create(date=date, appointment=appointment)
    for time in times:
        Time.objects.create(time=time, appointment=appointment)


def get_appointment(appointment_id):
    appointment_obj = Appointment.objects.filter(id=appointment_id).first()
    if appointment_obj:
        appointment = {'name': appointment_obj.name,
                       'description': appointment_obj.description}
        dates_obj = Date.objects.all().filter(appointment=appointment_obj)
        dates = [do.date for do in dates_obj]
        times_obj = Time.objects.all().filter(appointment=appointment_obj)
        times = [to.time for to in times_obj]
        return {
            'appointment': appointment,
            'dates': dates,
            'times': times
        }
    return None


def join_appointment(appointment_id, date, time, is_logined, username, email):
    appointment = Appointment.objects.filter(id=appointment_id).first()
    date = Date.objects.filter(date=date, appointment=appointment).first()
    time = Date.objects.filter(time=time, appointment=appointment).first()
    if is_logined:
        user = RegisteredUser.objects.filter(username=username)
        Registration.objects.create(appointment=appointment, date=date, time=time, username=user.username,
                                    email=user.email, user=user)
    else:
        Registration.objects.create(appointment=appointment, date=date, time=time, username=username, email=email)
