from django.contrib import  admin
from django.urls import path
from .views import *

urlpatterns = [
   path('HomePage' , HomePage , name='EventHomePage'),
   path('testId/<int:id>' , testId , name='Test'),
   path("renderlist", RenderList, name="RenderList")
] 