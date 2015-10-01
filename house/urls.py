"""house URL Configuration
"""

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'chores.views.index', name='index'),
    url(r'^chores/profile/(?P<slug>[^\.]+).html', 'chores.views.profile', name='profile'),
    url(r'^chores/category/(?P<slug>[^\.]+).html', 'chores.views.view_category', name='view_category'),
    url(r'^chores/edit_chore/(?P<slug>[^\.]+).html', 'chores.views.edit_chore', name='edit_chore'),
    url(r'^chores/search_results.html', 'chores.views.search', name='search'),
    url(r'^chores/all_chores.html', 'chores.views.all_chores', name='all_chores'),
    url(r'^(?P<slug>[^\.]+)/mark_chore_done/$', 'chores.views.mark_chore_done', name='mark_chore_done'),
]


urlpatterns += [
    # Auth-related URLs
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^accounts/loggedin/$', 'chores.views.loggedin', name='loggedin'),
    url(r'^accounts/notauthorized/$', 'chores.views.notauthorized', name='notauthorized'),
    url(r'^chores/loggedout/$', 'chores.views.loggedout', name='loggedout'),
]
