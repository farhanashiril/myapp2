from django.urls import path,include
from . import views

urlpatterns = [
   path('base',views.function,name="base"),
]