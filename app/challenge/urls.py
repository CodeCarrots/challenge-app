from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

import accounts.views

import tasks.views

urlpatterns = patterns(
    '',

    url(r'^$', TemplateView.as_view(template_name='home.html'),
        name='home'),

    url(r'^account/login/$', accounts.views.LoginView.as_view(),
        name='account_login'),

    url(r'^account/signup/$', accounts.views.SignupView.as_view(),
        name='account_signup'),

    url(r'^account/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='account_logout'),

    url(r'^account/', include('account.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^task/$', tasks.views.tasks_home, name='tasks_home'),
    url(r'^task/(.*)/task.py$', tasks.views.task_files, name='task_files'),
    url(r'^task/(.*)/?$', tasks.views.task, name='task_view'),
)
