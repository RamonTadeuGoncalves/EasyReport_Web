# EasyReport_Web
## _Aplicação web para gerenciamento de ordens de serviço. Utilizado na matéria TG (Trabalho de Graduação) da FATEC Indaiatuba_


Easy Report é uma aplicação web utilziada como requisito para a matéria TG (Trabalho de Graduação) da FATEC Indaiatuba.
Essa aplicação foi desenvolvida utilziando o framework Django.

- Django
- HTML
- CSS
- JS

## Caracteristicas

- Formulário simples para cadastro de funcionário, veículo, cliente e ordem de serviço
- Os dados são salvos no banco de dados postgreSQL, também podenendo ser gerenciado pelo Django Admin
- Listagem de funcionário, veículo, cliente, ordem de serviço e relatório de serviço
- A listagem de relatório de serviço é uma integração com o aplicativo para dispositivos móveis que também faz parte do escopo do projeto
- Edição e exclusão de cadastro

## Requisitos

- Python (https://www.python.org/)
- pip (https://pypi.org/project/pip/)
- Django (https://www.djangoproject.com/)
- Crispy_forms (https://django-crispy-forms.readthedocs.io/en/latest
- crispy_bootstrap5 (https://github.com/django-crispy-forms/crispy-bootstrap5)
- PsycoPG2 (https://pypi.org/project/psycopg2/)
- PostgreSQL (https://www.postgresql.org/)
- pgAdmin (https://www.pgadmin.org/)
- Necessário criar banco de dados conforme dados encontrados no arquivo settings.py

## Instalação

Após fazer o clone do prjeto, será necessário rodar os seguintes comandos: 
```sh
python manage.py migrate
python manage.py makemigrations
python manage.py runserver
```

Feito isso, a aplicação será exibida no navegador.

# Em desenvolvimento...

