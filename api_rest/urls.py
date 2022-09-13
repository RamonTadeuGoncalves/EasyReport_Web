from django.urls import path
from api_rest import views

urlpatterns = [
    path('usuario/', views.loginApi),
    path('usuario/<int:id>/', views.loginApi),
    path('funcionario/', views.funcionarioApi),
    path('funcionario/<int:id>/', views.funcionarioApi),
    path('veiculo/', views.veiculoApi),
    path('veiculo/<int:id>/', views.veiculoApi),
    path('cliente/', views.clienteApi),
    path('cliente/<int:id>/', views.clienteApi),
    path('ordem_servico/', views.OSApi),
    path('ordem_servico/<int:id>/', views.OSApi),
    path('relatorio_servico/', views.RelatorioDeServicoApi),
    path('relatorio_servico/<int:id>/', views.RelatorioDeServicoApi),

]
