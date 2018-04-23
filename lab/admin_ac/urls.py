from django.conf.urls import include, url
import admin_ac.views as views


urlpatterns = [

    url(r'^$', views.login),
    url(r'^user/', views.page),
    url(r'^club/', views.club),
    url(r'^logs/', views.logs),
    url(r'^match/', views.match),
    url(r'^logout/', views.logout),
    url(r'^userprop/(?P<id>[0-9]+)', views.user_spec),
    url(r'^del/user/(?P<id>[0-9]+)',views.del_user),
    url(r'^locks/user/(?P<id>[0-9]+)',views.locks_user),
    url(r'^unlocks/user/(?P<id>[0-9]+)',views.unlocks_user),
    url(r'^create_club/', views.create_club),
    url(r'^del_club/(?P<id>[0-9]+)', views.del_club),
    url(r'^match_create/', views.match_create),
    url(r'^match_spec/(?P<id>[0-9]+)',views.match_spec),
    url(r'^del_match/(?P<id>[0-9]+)',views.match_del),
    url(r'^bets/',views.bets),
]
