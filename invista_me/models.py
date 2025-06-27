from django.db import models
from datetime import datetime # importa o horario atual
# Create your models here.

# classe que representa as informaçoes , investimento, valor, pago e data, essa classe ira se torna uma tabela num banco de dados(model)
class Investimento(models.Model):# nos devemos herdar da classe model.models para que nos possamos usar as funcionalidades de uma banco de dados
    investimento = models.TextField(max_length=253) # tamanho maximo para essa coluna
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now) # vai pegar o horario atual que foi feito o cadastro das infromaçoes


# 1 - caso eu queira adicionar mais infromaçoes eu faço a alteraçao ou adiciono ou deleto uma coluna
# 2 - depois abro o terminal e digito: python manage.py makemigrations aperto enter depois ele adiciona
# para que essa nova infromaçao seja enviada a um banco de dados
# 1 - digito: python manage.py migrate aperto enter e pronto

# para ver as alteraçoes no banco de dados e so abrir o db browser abrir a pasta do arquivo que contem o banco de dados sqlite e ver

# para remover a coluna e so excluir do codigo no vs code depois rodar: python manage.py makemigrations
# depois passo as alteraçoes para o banco de dados: python manage.py migrate