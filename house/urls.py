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
    url(r'^chores/all_chores.html', 'chores.views.all_chores', name='all_chores'),
    url(r'^chores/all_categories.html', 'chores.views.all_categories', name='all_categories'),
    url(r'^chores/view_chores_history.html', 'chores.views.view_chores_history', name='view_chores_history'),
    url(r'^chores/rewards.html', 'chores.views.rewards', name='rewards'),
    url(r'^(?P<slug>[^\.]+)/delete_reward/$', 'chores.views.delete_reward', name='delete_reward'),
    url(r'^(?P<slug>[^\.]+)/redeem_reward/$', 'chores.views.redeem_reward', name='redeem_reward'),

    url(r'^mark_chore_done/$', 'chores.views.mark_chore_done', name='mark_chore_done'),
    url(r'^clear_all_chores_filter/$', 'chores.views.clear_all_chores_filter', name='clear_all_chores_filter'),
    url(r'^clear_view_history_filter/$', 'chores.views.clear_view_history_filter', name='clear_view_history_filter'),
    url(r'^(?P<slug>[^\.]+)/delete_category/$', 'chores.views.delete_category', name='delete_category'),

]


urlpatterns += [
    # Auth-related URLs
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^accounts/loggedin/$', 'chores.views.loggedin', name='loggedin'),
    url(r'^accounts/notauthorized/$', 'chores.views.notauthorized', name='notauthorized'),
    url(r'^chores/loggedout/$', 'chores.views.loggedout', name='loggedout'),
]
