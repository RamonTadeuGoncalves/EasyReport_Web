from django.urls import path
from .import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logar/', views.logar, name='logar'),
    path('sair/', views.sair, name="sair"),
    path('ativar_conta/<str:token>/', views.ativar_conta, name="ativar_conta"),
    path('alterar_senha/', views.alterar_senha, name='alterar_senha'),
]
