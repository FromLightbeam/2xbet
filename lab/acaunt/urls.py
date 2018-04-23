from django.conf.urls import include, url
import acaunt.views as views


urlpatterns = [
    url(r'^signup/', views.signup),
    url(r'^login/',views.login),
    url(r'^user/', views.user_page),
    url(r'^logout/',views.logout),
    url(r'^addmoney/',views.addmoney),
    url(r'^withdrawmoney/',views.withdrawmoney),
    url(r'^user_log/', views.user_logs_mon),
]
