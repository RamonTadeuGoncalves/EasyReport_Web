from django.urls import path
from api_rest import views

urlpatterns = [
    path('funcionario/', views.funcionarioApi),
    path('funcionario/<int:id>/', views.funcionarioApi),
    path('veiculo/', views.veiculoApi),
    path('veiculo/<int:id>/', views.veiculoApi),
    path('cliente/', views.clienteApi),
    path('cliente/<int:id>/', views.clienteApi),
    path('ordem_servico/', views.OSApi),
    path('ordem?servico/<int:id>/', views.OSApi),

]
