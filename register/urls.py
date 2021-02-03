from django.urls import path
from . import views

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout')
]