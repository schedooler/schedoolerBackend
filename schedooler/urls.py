from django.urls import path

from schedooler.views import registry_schedool

urlpatterns = [
    path('schedool', registry_schedool, name='resitry_schedool')
]