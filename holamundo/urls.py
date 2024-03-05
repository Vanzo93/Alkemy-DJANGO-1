from django.urls import path
from .views import holamundo


urlpatterns = [
    path('', holamundo, name='hola mundo'),
]
