# Sistema de Investimentos

Este é um projeto web desenvolvido com Django para gerenciamento de investimentos pessoais o sistema permite:

- Criar novos investimentos com dados personalizados
- Excluir investimentos existentes
- Visualizar detalhes individuais de cada investimento
- Interface simples e funcional para controle financeiro

## Tecnologias utilizadas

- Python
- Django
- HTML/CSS (Bootstrap)
- SQLite (banco de dados padrão)

## Como rodar o projeto

```bash
git clone https://github.com/SEU_USUARIO/NOME_REPOSITORIO.git
cd NOME_REPOSITORIO
python -m venv venv
venv\Scripts\activate  # ou source venv/bin/activate no Linux/macOS
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
