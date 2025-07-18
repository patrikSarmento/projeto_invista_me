"""
URL configuration for projeto_invista_me project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from invista_me import views
from usuarios import views as usuarios_views
from django.contrib.auth import views as auth_views


# essas serao as nossas urls para acessar as paginas ↓
urlpatterns = [
    path('admin/',admin.site.urls),
    path('conta/',usuarios_views.novo_usuario,name='novo_usuario'),
    path('login/',auth_views.LoginView.as_view(template_name='usuarios/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='usuarios/logout.html'),name='logout'),
    path('',views.investimentos,name='investimentos'), # esse passo 3, a pessoa vai entrar no nosso site e a primeira pagina que ela vai acessar e a pagina de listagem de investimentos
    path('novo_investimento/', views.criar,name='novo_investimento'),
    path('novo_investimento/<int:id_investimento>/',views.editar,name='editar'),
    path('excluir_investimento/<int:id_investimento>/',views.excluir,name='excluir'),
    path('<int:id_investimento>/',views.detalhe,name='detalhe')
]