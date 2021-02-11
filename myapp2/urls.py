from django.urls import path,include
from . import views

urlspatterns=[

path('base',views.function,name="base"),

]