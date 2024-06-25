from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path('', views.login),
    # path('',views.login , name='login'),

    path('interface_technicien',views.interface_technicien , name='interface_technicien'),
    path('interface_employee',views.interface_employee , name='interface_employee'),
    path('interface_admin',views.interface_admin , name='interface_admin'),
    path('register',views.register , name='register'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    #path('',auth_views.LoginView.as_view(template_name='index/index.html'),name='login'),
    path('',views.MyLoginView.as_view(template_name='home_page/index.html'),name='login'),
    path('gestintervention',views.gestintervention,name='gestintervention'),
    path('gestutilisateur',views.gestutilisateur,name='gestutilisateur'),
    path('paramsys',views.paramsys,name='paramsys'),
    path('rapp_stat',views.rapp_stat,name='rapp_stat'),
    path('signalementproblem',views.signalementproblem,name='signalementproblem'),
    path('suividemande',views.suividemande,name='suividemande'),
    path('consuletintervention',views.consuletintervention,name='consuletintervention'),
    path('mizajour',views.mizajour,name='mizajour'),
    path('rapportintervention',views.rapportintervention,name='rapportintervention'),
   



]
