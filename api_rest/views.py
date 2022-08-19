from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from easyreport_web.models import Funcionario, Veiculo, Cliente, OrdemDeServico
from api_rest.serializers import FuncionarioSerializer, VeiculoSerializer, ClienteSerializer, OSSerializer


# Create your views here.

@csrf_exempt
def funcionarioApi(request, id=0):
    if request.method == 'GET':
        funcionario = Funcionario.objects.all()
        funcionario_serializer = FuncionarioSerializer(funcionario, many=True)
        return JsonResponse(funcionario_serializer.data, safe=False)
    elif request.method == 'POST':
        funcionario_data = JSONParser().parse(request)
        funcionario_serializer = FuncionarioSerializer(data=funcionario_data)
        if funcionario_serializer.is_valid():
            funcionario_serializer.save()
            return JsonResponse("Adicionado com Sucesso", safe=False)
        return JsonResponse("Falha ao Adicionar", safe=False)
    elif request.method == 'PUT':
        funcionario_data = JSONParser().parse(request)
        funcionario = Funcionario.objects.get(funcRegistro=funcionario_data['funcRegistro'])
        funcionario_serializer = FuncionarioSerializer(funcionario, data=funcionario_data)
        if funcionario_serializer.is_valid():
            funcionario_serializer.save()
            return JsonResponse("Atualizado com Sucesso", safe=False)
        return JsonResponse("Falha ao Atualizar", safe=False)
    elif request.method == 'DELETE':
        funcionario = Funcionario.objects.get(funcRegistro=id)
        funcionario.delete()
        return JsonResponse("Apagado com Sucesso", safe=False)

@csrf_exempt
def veiculoApi(request, id=0):
    if request.method == 'GET':
        veiculo = Veiculo.objects.all()
        veiculo_serializer = VeiculoSerializer(veiculo, many=True)
        return JsonResponse(veiculo_serializer.data, safe=False)
    elif request.method == 'POST':
        veiculo_data = JSONParser().parse(request)
        veiculo_serializer = VeiculoSerializer(data=veiculo_data)
        if veiculo_serializer.is_valid():
            veiculo_serializer.save()
            return JsonResponse("Adicionado com Sucesso", safe=False)
        return JsonResponse("Falha ao Adicionar", safe=False)
    elif request.method == 'PUT':
        veiculo_data = JSONParser().parse(request)
        veiculo = Veiculo.objects.get(funcRegistro=veiculo_data['veicRegistro'])
        veiculo_serializer = VeiculoSerializer(veiculo, data=veiculo_data)
        if veiculo_serializer.is_valid():
            veiculo_serializer.save()
            return JsonResponse("Atualizado com Sucesso", safe=False)
        return JsonResponse("Falha ao Atualizar", safe=False)
    elif request.method == 'DELETE':
        veiculo = Veiculo.objects.get(veicRegistro=id)
        veiculo.delete()
        return JsonResponse("Apagado com Sucesso", safe=False)

@csrf_exempt
def clienteApi(request, id=0):
    if request.method == 'GET':
        cliente = Cliente.objects.all()
        cliente_serializer = ClienteSerializer(cliente, many=True)
        return JsonResponse(cliente_serializer.data, safe=False)
    elif request.method == 'POST':
        cliente_data = JSONParser().parse(request)
        cliente_serializer = ClienteSerializer(data=cliente_data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return JsonResponse("Adicionado com Sucesso", safe=False)
        return JsonResponse("Falha ao Adicionar", safe=False)
    elif request.method == 'PUT':
        cliente_data = JSONParser().parse(request)
        cliente = Cliente.objects.get(funcRegistro=cliente_data['clienteRegistro'])
        cliente_serializer = ClienteSerializer(cliente, data=cliente_data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return JsonResponse("Atualizado com Sucesso", safe=False)
        return JsonResponse("Falha ao Atualizar", safe=False)
    elif request.method == 'DELETE':
        cliente = Cliente.objects.get(clienteRegistro=id)
        cliente.delete()
        return JsonResponse("Apagado com Sucesso", safe=False)

@csrf_exempt
def OSApi(request, id=0):
    if request.method == 'GET':
        ordemDeServico = OrdemDeServico.objects.all()
        ordemDeServico_serializer = OSSerializer(ordemDeServico, many=True)
        return JsonResponse(ordemDeServico_serializer.data, safe=False)
    elif request.method == 'POST':
        ordemDeServico_data = JSONParser().parse(request)
        ordemDeServico_serializer = OSSerializer(data=ordemDeServico_data)
        if ordemDeServico_serializer.is_valid():
            ordemDeServico_serializer.save()
            return JsonResponse("Adicionado com Sucesso", safe=False)
        return JsonResponse("Falha ao Adicionar", safe=False)
    elif request.method == 'PUT':
        ordemDeServico_data = JSONParser().parse(request)
        ordemDeServico = OrdemDeServico.objects.get(funcRegistro=ordemDeServico_data['osNumero'])
        ordemDeServico_serializer = OSSerializer(ordemDeServico, data=ordemDeServico_data)
        if ordemDeServico_serializer.is_valid():
            ordemDeServico_serializer.save()
            return JsonResponse("Atualizado com Sucesso", safe=False)
        return JsonResponse("Falha ao Atualizar", safe=False)
    elif request.method == 'DELETE':
        ordemDeServico = OrdemDeServico.objects.get(osNumero=id)
        ordemDeServico.delete()
        return JsonResponse("Apagado com Sucesso", safe=False)
