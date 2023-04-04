[![wakatime](https://wakatime.com/badge/user/3bd24664-869f-460a-94e1-b98da8136504/project/84b221e2-7b66-4ea3-b381-f11d8513afe0.svg)](https://wakatime.com/badge/user/3bd24664-869f-460a-94e1-b98da8136504/project/84b221e2-7b66-4ea3-b381-f11d8513afe0)

<h2 align="center">FastAPI - CRUD Faculdade 🏫 </h2>

## Índice

- [Sobre](#-sobre)
- [Tecnologias utilizadas](#-tecnologias-utilizadas)
- [Como executar o projeto](#-como-executar-o-projeto)
- [Como baixar o projeto](#-como-baixar-o-projeto)
- [Endpoints](#-endpoints)
- [Bibliotecas](#-bibliotecas)
- [Autor](#-autor)

## 📖 Sobre

Esta API é um exemplo de como usar a modelagem e estruturação para futuras aplicações.

O projeto **API FastAPI** é uma API desenvolvida em Python com o ‘framework’ FastAPI, cujo objetivo é realizar o
CRUD de um banco de dados dos cursos da faculdade.

A API utiliza o banco de dados PostgreSQL configurado no Docker, e o ORM utilizado foi o SQLAlchemy.

## 🔗 Tecnologias utilizadas

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white)
![Git](https://img.shields.io/badge/-Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white)
![PyCharm](https://img.shields.io/badge/-PyCharm-000000?style=flat-square&logo=pycharm&logoColor=white)

## ⚙️ Como executar o projeto

#### 💻 Pré-requisitos

Antes de começar, você vai precisar ter instalado na sua máquina as seguintes ferramentas:

- Você precisa ter o [Python](https://www.python.org/downloads/) instalado na sua máquina.
- Você precisa ter o [Docker](https://www.docker.com/products/docker-desktop) instalado na sua máquina.
- Ter instalado o [Git](https://git-scm.com/downloads) para clonar o projeto.
- Possuir um editor de código, como o [PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=windows)
  ou [VSCode](https://code.visualstudio.com/download).
- Ter um terminal para executar os comandos, como o [Git Bash](https://gitforwindows.org/) ou
  o [CMD](https://docs.microsoft.com/pt-br/windows-server/administration/windows-commands/cmd).
- Ter um cliente para realizar as requisições, como o [Insomnia](https://insomnia.rest/download/) ou
  o [Postman](https://www.postman.com/downloads/), ou dentro do próprio projeto há uma pasta chamada **collection** na
  raiz do projeto, onde você pode executar as requisições do arquivo .http.
- Ter um banco de dados PostgreSQL local ou utilizar no Docker, podendo utilizar o arquivo `docker-compose.yml` que está
  na raiz do projeto, para criar o banco de dados.

Com tudo em mãos e devidamente instalado, você poderá seguir o próximo tópico.

## 🎯 Como baixar o projeto

Atente-se aos passos a seguir para executar o projeto:

#### 📁 Clonar o repositório

```bash
# Clonar o repositório
git clone https://github.com/matheus-feu/FastAPI-JWT-Security.git

# Entrar no diretório
cd FastAPI-CRUD-Faculdade 
```

#### 🐳 Docker

```bash
# Criar o container do banco de dados
docker-compose up -d
```

#### 🐍 Python

```bash
# Criar um ambiente virtual
python -m venv venv
 
# Ativar o ambiente virtual
venv\Scripts\activate

# Instalar as dependências
pip install -r requirements.txt

# Criar as tabelas no banco de dados
python create_tables.py

# Executar o projeto
uvicorn main:app --reload
```

## 📌 Endpoints

Após concluir as etapas anteriores, você poderá acessar a documentação da API no endereço http://localhost:8000/docs.

![documentacao](https://imgur.com/E3MTlQH.png)

Basicamente a API possui 4 endpoints, neles você poderá realizar o CRUD de um curso da faculdade.

O fluxo de autenticação é o seguinte:

- Você precisa criar um curso na rota **/api/v1/cursos**, passando o título do curso, descrição, quantidade aulas e
  horas.

```bash
{
    "titulo": "Curso de Python",
    "descricao": "Curso de Python",
    "aulas": 10,
    "horas": 10
}
```

- Após criar o curso, na rota **/api/v1/cursos/{id}**, você poderá visualizar o curso criado pelo respectivo ID.

```bash
{
  "id": 1
}
```

Saída:

```bash
{
    "id": 1,
    "titulo": "Curso de Python",
    "descricao": "Curso de Python",
    "aulas": 10,
    "horas": 10
}
```

- Assim da mesma forma poderá pegar todos os cursos cadastrados na rota **/api/v1/cursos**.

Saída:

```bash
[
    {
        "id": 1,
        "titulo": "Curso de Python",
        "descricao": "Curso de Python",
        "aulas": 10,
        "horas": 10
    },
    
    {
        "id": 2,
        "titulo": "curso de Java",
        "descricao": "Curso sobre java",
        "aulas": 5,
        "horas": 10
    }        
]
```

- Permite que possa atualizar o curso na rota **/api/v1/cursos/{id}**, passando o título do curso, descrição, quantidade
  aulas e horas.

```bash
{
    "titulo": "Curso de Python",
    "descricao": "Curso sobre orientação a objetos",
    "aulas": 30,
    "horas": 65
}
```

- Por fim, permite que possa deletar o curso na rota **/api/v1/cursos/{id}**, passando o respectivo ID do curso,
  para saber qual o curso deseja deletar, vá na rota **/api/v1/cursos** e pegue o ID do curso que deseja deletar.

```bash
{
  "id": 1
}
```

## 📚 Bibliotecas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Uvicorn](https://www.uvicorn.org/)
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
- [asyncpg](https://pypi.org/project/asyncpg/)

## 👨‍💻 Autor

- [Email](mailto:matheusfeu@gmail.com)
- [Linkedin](https://www.linkedin.com/in/matheus-feu-558558186/)
- [Github](https://github.com/matheus-feu)
- [Instagram](https://www.instagram.com/math_feu/)
