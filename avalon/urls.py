from django.conf.urls import url
from django.views.generic import TemplateView

from avalon.views import login_view, logout_view, personal_page_view

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^login/$', TemplateView.as_view(template_name='login.html'), name='login'),
    url(r'^login_handler/$', login_view, name='login_handler'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^personal_page/$', personal_page_view, name='personal_page')
]
