from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from avalon.models import RegisteredUser, UnregisteredUser, Appointment, Date, Time


class RegisteredUserAdmin(UserAdmin):
    pass


admin.site.register(RegisteredUser, RegisteredUserAdmin)
admin.site.register(UnregisteredUser)
admin.site.register(Appointment)
admin.site.register(Date)
admin.site.register(Time)
