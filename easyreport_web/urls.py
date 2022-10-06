from re import sub
from unicodedata import name
from django.urls import path
from django.views.generic import RedirectView

from authentication.views import cadastro, logar
from easyreport_web.views import *

urlpatterns = [
    path('/index/', RedirectView.as_view(url='index/')),
    path('index/', index, name='index'),
    path('', logar, name='logar'),
    path('login/', login_user, name='login_user'),
    path('login/submit', submit_login, name='submit_login'),
    path('logout/', logout_user, name='logout_user'),
    path('cadastrar_funcionario/', cadastro, name='cadastrar_funcionario'),
    path('cadastrar_veiculo/', cadastrar_veiculo, name='cadastrar_veiculo'),
    path('cadastrar_cliente/', cadastrar_cliente, name='cadastrar_cliente'),
    path('cadastrar_os/', cadastrar_os, name='cadastrar_os'),
    path('listar_funcionario/', listar_funcionario, name='listar_funcionario'),
    path('listar_veiculo/', listar_veiculo, name='listar_veiculo'),
    path('listar_cliente/', listar_cliente, name='listar_cliente'),
    path('listar_os/', listar_os, name='listar_os'),
    path('listar_relatorio/', listar_relatorio, name='listar_relatorio'),
    path('funcionario/<int:nr_item>/', funcionario, name='funcionario'),
    path('veiculo/<int:nr_item>/', veiculo, name='veiculo'),
    path('cliente/<int:nr_item>/', cliente, name='cliente'),
    path('ordem_servico/<int:nr_item>/', ordem_servico, name='ordem_servico'),
    path('relatorio_servico/<int:nr_item>/', relatorio_servico, name='relatorio_servico'),
    path('editar_funcionario/<int:nr_item>/', editar_funcionario, name='editar_funcionario'),
    path('editar_veiculo/<int:nr_item>/', editar_veiculo, name='editar_veiculo'),
    path('editar_cliente/<int:nr_item>/', editar_cliente, name='editar_cliente'),
    path('editar_os/<int:nr_item>/', editar_os, name='editar_os'),
    path('excluir_funcionario/<int:nr_item>/', excluir_funcionario, name='excluir_funcionario'),
    path('excluir_veiculo/<int:nr_item>/', excluir_veiculo, name='excluir_veiculo'),
    path('excluir_cliente/<int:nr_item>/', excluir_cliente, name='excluir_cliente'),
    path('excluir_os/<int:nr_item>/', excluir_os, name='excluir_os'),
    path('excluir_relatorio/<int:nr_item>/', excluir_relatorio, name='excluir_relatorio'),
    path('cadastrar_tipo_servico/', cadastrar_tipo_servico, name='cadastrar_tipo_servico'),
    path('listar_tipo_servico/', listar_tipo_servico, name='listar_tipo_servico'),
    path('tipo_servico/<int:nr_item>/', tipo_servico, name='relatorio_tipo_servico'),
    path('excluir_tipo_servico/<int:nr_item>/', excluir_tipo_servico, name='excluir_tipo_servico'),
    path('editar_tipo_servico/<int:nr_item>/', editar_tipo_servico, name='editar_tipo_servico'),
]
