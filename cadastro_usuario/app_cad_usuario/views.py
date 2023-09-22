from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    #salvando no banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome= request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #Exibindo dados em nova pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'usuarios/usuarios.html', usuarios)
