from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view  # views baseadas em funções
from rest_framework.response import Response
from .serializers import TodoTaskSerializer
from .models import TodoTask


# Overview da API mostrando todas as rotas disponíveis
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/todo-list/',
        'Detail': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }

    return Response(api_urls)


# Listagem de todas as tarefas
@api_view(['GET'])
def todo_list(request):
    tasks = TodoTask.objects.all()
    serializer = TodoTaskSerializer(tasks, many=True)

    return Response(serializer.data)


# Visualisação detalhada de apenas uma tarefa
@api_view(['GET'])
def task_detail(request, pk):
    task = TodoTask.objects.get(id=pk)
    serializer = TodoTaskSerializer(task, many=False)

    return Response(serializer.data)


# Criar uma nova tarefa
@api_view(['POST'])
def task_create(request):
    serializer = TodoTaskSerializer(data=request.data)

    if serializer.is_valid():
        # TODO tratamento de exceções
        serializer.save()

    return Response(serializer.data)


# Atualizar uma tarefa existente
@api_view(['POST'])
def task_update(request, pk):
    task = TodoTask.objects.get(id=pk)
    serializer = TodoTaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        # TODO tratamento de exceções
        serializer.save()

    return Response(serializer.data)


# Deletar uma tarefa existente
@api_view(['DELETE'])
def task_delete(request, pk):
    task = TodoTask.objects.get(id=pk)
    task.delete()

    return Response('Task deleted')
