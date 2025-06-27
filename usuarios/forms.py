from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# vamos criar uma nova classe que sera uma nova forma de criar usuarios noa vamos usar a padrao que e a usercreationfrom porem vamos estar herdando dela todas as funcionalidades que estao prontas
class UserRegisterForm(UserCreationForm):
    Email = forms.EmailField

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        