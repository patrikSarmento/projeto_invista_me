from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm


# criando um novo usuario
def novo_usuario(request):
    # verificar tipo requisiçao,validar,infromar se foi criado usuario ou nao, salvar no banco de dados
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST) # estou pegando as informaçoes que foram enviadas do site pro meu servidor e populando essa classe e assim vou ter um usuario criado e ele vai ser passado para ess variavel formulario
        if formulario.is_valid():
            formulario.save() # caso o formulario esteja certo vamos validar
            # informa o site o nome do usuario que acaba de ser criado
            usuario = formulario.cleaned_data.get('username') # o cleaned_data possui todas as infromaçoes que estao dentro daquela requisiçao
            messages.success(request,f'usuario {usuario} criado com sucesso!') # exibindo de forma dinamica um usuario que acaba de ser criado
            return redirect('login')

    else:
        formulario = UserRegisterForm()

    return render(request,'usuarios/registrar.html',{'formulario':formulario}) # aqui e passada a pagina responsavel por conter as iformaçoes dos ususarios a pagina html)
















