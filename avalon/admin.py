from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from avalon.models import RegisteredUser, Appointment, Date, Time, Registration


class RegisteredUserAdmin(UserAdmin):
    pass


admin.site.register(RegisteredUser, RegisteredUserAdmin)
admin.site.register(Registration)
admin.site.register(Appointment)
admin.site.register(Date)
admin.site.register(Time)
