from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('login_page', views.login_page, name='login_page'),
    path('registration_page', views.registration_page, name='registration_page'),
    path('registrate', views.registrate_user, name='registrate_user'),
    path('logout/', views.logout_page, name='logout_page'),
]