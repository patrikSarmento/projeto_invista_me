from django.shortcuts import render, redirect,HttpResponse
from .models import Investimento  # traz as informaçoes do banco de dados para passar para nossa pagina
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required # vai permitir que soment usuarios cadastrados acessem certas partes da pagina

# Create your views here.

# passo 1 para exibir uma nova pagina para um usuario
def investimentos (request):
    # ↓ passando os dados para nossa pagina atravez de um dicionario
    dados = {
        'dados': Investimento.objects.all()   
    }   # ↑ chave 'dados' que ira receber as informaçoes extraidas de investimento.objects.all()...estamos dizendo para entrar para ir no banco de dados na tabela investimento encontr todos os objetos ou seja todos os registros e dentro de todos os registros retorne para mim all(retorne todos eles) guardei essas informaçoes dentr da chave dados do dicionario dados
    return render(request,'investimentos/investimentos.html',context=dados)  # peguei os dados da linha 12 e passe como parametro dentro do return como context=dados

# exibir detalhe dos investimentos
def detalhe(request,id_investimento):
    dados = {
        'dados':Investimento.objects.get(pk=id_investimento)}
    return render(request,'investimentos/detalhe.html',dados)

# cria um novo investimento
@login_required
def criar(request):
    if request.method == 'POST':
      investimento_form = InvestimentoForm(request.POST)
      if investimento_form.is_valid():
        investimento_form.save()
        return redirect('investimentos')
    else:
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request,'investimentos/novo_investimento.html',context=formulario)


# editar um investimento, permite entra em um investimento e edita-lo
@login_required
def editar(request,id_investimento):# define uma funçao view chamada editar, recebe dois parametros request: a requisiçao http. id_investimento: o id que sera alterado, o nome id_investimento foi dado por mim msm
    investimento = Investimento.objects.get(pk=id_investimento) # busca no banco de dados um objeto da model INVESTIMENTO coom o id(chave primaria) igual ao id_investimento fornecido, se nao encontra essa linha lançara um erro
    if request.method == 'GET': # verifica se a requisiçao HTTP e do tipo GET, o que normalmente significa que o usuarioquer ver o formulario de ediçao
        formulario = InvestimentoForm(instance=investimento) # cria um formulario (investimentoform) ja preenchido com os dados atuais do investimento buscado. o parametro instance=investimento serve para ligar o formulario ao objeto existente, permitindo a ediçao
        return render(request,'investimentos/novo_investimento.html',{'formulario':formulario}) # renderiza o template novo_investimento.html, passando o formulario preenchido para ele. assim o usuario pode editar os dados ja existentes
    else: # caso a requisiçao nao seja um get assume-se que e um POST (ou seja o formulario foi enviado para salvar as alteraçoes)
        formulario = InvestimentoForm(request.POST,instance=investimento) # cria um novo formulario com os dados enviados pelo usuario(request,POST) e ainda vincula ao objeto investimento. isso indica que estamos atualizando registros existentes
        if formulario.is_valid():# verifica se os dados enviados no formulario sao validos (de acordo com as regras da model e do form)
            formulario.save() # salva as alteraçoes feitas no objeto investimento no banco de dados
            return redirect('investimentos') # redireciona o usuario para view chamada INVESTIMENTOS(geralmente uma lista de todos os investimentos)
                                            # o nome investimentos deve estar definido na urls.py como name='investimentos'

# excluir um investimento
@login_required
def excluir(request,id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request,'investimentos/confirma_exclusao.html',{'item':investimento})
    











#🔍 Por que sempre tem request na função def?
#Porque o Django chama automaticamente essa função quando uma URL é acessada, e ele passa um objeto HttpRequest como primeiro argumento.
#Esse objeto request contém todos os dados da requisição, por exemplo:



 # O que é um Model no Django?
#📌 Definição:
#Um Model é uma representação de uma tabela do banco de dados em Python.
#Cada model vira uma tabela no banco, e cada atributo do model vira uma coluna.

# 🧱 Exemplo:
#python
# Copiar código
# from django.db import models

#class Investimento(models.Model):
 #   nome = models.CharField(max_length=100)
  #  valor = models.DecimalField(max_digits=10, decimal_places=2)
   # data = models.DateField()
#🧠 Isso cria uma tabela chamada investimento com as colunas:

# nome (texto),

# valor (decimal),

# data (data).

# -------------------------------------------------

# 🗂 Usos do Model:
# Um Model representa uma tabela do banco de dados.
# Com ele é possível criar, consultar, editar e deletar dados.

# Exemplo de uso na view:
# invest = Investimento.objects.create(nome="Ações", valor=1000, data="2025-06-01")

# ✅ O que é um Form no Django?
# 📌 Definição:
# Um Form (formulário) é uma classe que:
# - Define quais campos o usuário pode preencher.
# - Valida os dados enviados.
# - Pode estar ligada a um Model (ModelForm) ou não.

# 🧾 Exemplo de ModelForm:
# from django import forms
# from .models import Investimento

# class InvestimentoForm(forms.ModelForm):
#    class Meta:
#        model = Investimento
#        fields = ['nome', 'valor', 'data']

# Esse formulário:
# - Cria um formulário baseado no model Investimento.
# - Permite que o usuário preencha os campos: nome, valor e data.

# 🛠 Usos do Form:
# Na view:
# formulario = InvestimentoForm(request.POST)

# if formulario.is_valid():
#    formulario.save()  # Salva no banco

# No template (HTML), o formulário seria exibido assim (exemplo Django):
'''
<form method="POST">
    {{ formulario.as_p }}
    <button type="submit">Salvar</button>
</form>
'''
