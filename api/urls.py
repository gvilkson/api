from django.urls import path
from . import views

urlpatterns = [
    path('cpf-info/', views.pesquisar_cpf, name='cpf-info'),
]