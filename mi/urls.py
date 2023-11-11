from mi.views import *
from django.urls import path 

app_name='thing'

urlpatterns=[
    path('rohit/',rohit,name='rohit'),
]