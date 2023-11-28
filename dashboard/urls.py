from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('solicitacoes/',views.solicitacoes, name='solicitacoes'),
    path('entregadores/',views.entregadores, name='entregadores'),
    path('relatorios/',views.relatorios, name='relatorios'),
    path('config/', views.config, name='config'),
    path('change_password/', views.change_password, name='change_password'),
]