from django.urls import path
from timeapp import views

urlpatterns = [
    path('greeting', views.get_greeting),
]