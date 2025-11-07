from django.urls import path
from .views import *

name_app = 'hopitalapp'
urlpatterns =[
    path('',indexPage,name='home')
]