"""
URL patterns for the views included in ``django.contrib.auth``.

Including these URLs (via the ``include()`` directive) will set up the
following patterns based at whatever URL prefix they are included
under:

* User login at ``login/``.

* User logout at ``logout/``.

* The two-step password change at ``password/change/`` and
  ``password/change/done/``.

* The four-step password reset at ``password/reset/``,
  ``password/reset/confirm/``, ``password/reset/complete/`` and
  ``password/reset/done/``.

The default registration backend already has an ``include()`` for
these URLs, so under the default setup it is not necessary to manually
include these views. Other backends may or may not include them;
consult a specific backend's documentation for details.

"""

from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url

from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
                       url(r'^login/$',
                           auth_views.login,
                           {'template_name': 'registration/login.html'},
                           name='auth_login'),
                       url(r'^logout/$',
                           auth_views.logout,
                           {'template_name': 'registration/logout.html'},
                           name='auth_logout'),
                       url(r'^password_change/$',
                           auth_views.password_change,
                           name='auth_password_change'),
                       url(r'^password_change/done/$',
                           auth_views.password_change_done,
                           name='password_change_done'),
                       url(r'^password_reset/$',
                           auth_views.password_reset,
                           name='auth_password_reset'),
                       url(r'^password_reset/done/$',
                           auth_views.password_reset_done,
                           name='password_reset_done'),
                       url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                           auth_views.password_reset_confirm,
                           name='auth_password_reset_confirm'),
                       url(r'^reset/done/$',
                           auth_views.password_reset_complete,
                           name='password_reset_complete'),
)
