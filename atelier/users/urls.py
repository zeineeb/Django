from .views import *
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
     path('login/', SignIn ,name="login"),
    path('logout/', LogoutView.as_view() ,name="logout"),
    path('register/', signUp ,name="Signup"),
]