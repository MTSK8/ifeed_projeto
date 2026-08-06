from django.urls import path
from .views import listar_doacoes

urlpatterns = [

    path('doacoes/', listar_doacoes, name='listar_doacoes'),
]