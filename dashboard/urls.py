from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('solicitacoes/',views.solicitacoes, name='solicitacoes'),
    path('pagamentos/',views.pagamentos, name='pagamentos'),
    path('relatorios/',views.relatorios, name='relatorios')
]