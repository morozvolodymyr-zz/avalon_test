from avalon.models import RegisteredUser


def get_user_appointments(username):
    return RegisteredUser.objects.filter(username=username).first().appointments.all()
