# RASI - Docker com Aplicação Python/Flask

## Integrante

**Kennedy Vieira Teixeira**

## Sobre o projeto

Este projeto foi desenvolvido para a disciplina de **Redes e Administração de Sistemas (RASI)** do IFSP - Campus Campos do Jordão.

O projeto apresenta uma aplicação web desenvolvida utilizando **Python e Flask**, executada dentro de um container Docker.

A aplicação utiliza a imagem base:

```text
python:3.14-slim
```

## Tecnologias utilizadas

* Python
* Flask
* Docker
* Ubuntu Server

## Estrutura do projeto

```text
RASI-Docker-Flask/
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Aplicação

A aplicação possui três páginas:

### Página inicial

```text
/
```

Página principal da aplicação Flask.

### Página Sobre

```text
/sobre
```

Página com informações sobre o projeto, utilizando um layout diferente da página inicial.

### Página Contato

```text
/contato
```

Página de contato com título e layout próprios.

## Docker

O projeto utiliza um `Dockerfile` baseado na imagem:

```text
python:3.14-slim
```

A aplicação utiliza a porta:

```text
5000
```

## Arquivos do projeto

### app.py

Contém o código da aplicação Flask e as rotas das páginas.

### requirements.txt

Contém a dependência necessária para executar a aplicação:

```text
Flask
```

### Dockerfile

Contém as instruções utilizadas para criar a imagem Docker da aplicação.

### README.md

Este arquivo apresenta informações sobre o projeto e sua estrutura.

## Autor

**Kennedy Vieira Teixeira**

**IFSP - Campus Campos do Jordão**

**Redes e Administração de Sistemas (RASI) - 2026**