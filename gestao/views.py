from django.http import HttpResponse
from django.shortcuts import render
#from django.contrib.auth.models import User
from users.models import User
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator


@has_role_decorator('administrador')
def home(request):
    return HttpResponse("Estou na area de acesso de administrador")

def criar_usuario(request):
    user = User.objects.create_user(username='marcelo', password='1234')
    user.save()
    assign_role(user, 'administrador')
    return HttpResponse('Usuário criado com sucesso')
    
