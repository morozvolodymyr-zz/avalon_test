from django.conf.urls import url
from django.views.generic import TemplateView

from avalon.views import login_view, logout_view, personal_page_view, appointment_view

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^login/$', TemplateView.as_view(template_name='login.html'), name='login'),
    url(r'^login_handler/$', login_view, name='login_handler'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^personal_page/$', TemplateView.as_view(template_name='personal_page.html'), name='personal-page'),
    url(r'^appointment/$', TemplateView.as_view(template_name='appointment.html'), name='appointment'),

    url(r'^api/personal_page/$', personal_page_view, name='personal-page-api'),
    url(r'^api/appointment/$', appointment_view, name='appointment-api'),
]
