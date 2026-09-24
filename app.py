from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask no Docker</title>
        <style>
            body {
                background-color: #e8f1f8;
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
            }

            h1 {
                color: #1f4e79;
            }

            p {
                font-size: 18px;
            }
        </style>
    </head>

    <body>
        <h1>Bem-vindo ao Flask no Docker!</h1>
        <p>Aplicação desenvolvida para o trabalho de RASI.</p>
        <p>Python + Flask + Docker</p>
    </body>
    </html>
    """


@app.route("/sobre")
def sobre():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sobre o Projeto</title>
        <style>
            body {
                background-color: #dff5e1;
                font-family: Georgia, serif;
                text-align: center;
                padding: 50px;
            }

            h1 {
                color: #287a35;
            }

            p {
                font-size: 18px;
            }
        </style>
    </head>

    <body>
        <h1>Sobre o Projeto</h1>
        <p>Este projeto foi desenvolvido para a disciplina de Redes e Administração de Sistemas (RASI).</p>
        <p>A aplicação utiliza Python, Flask e Docker.</p>
    </body>
    </html>
    """


@app.route("/contato")
def contato():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Contato</title>
        <style>
            body {
                background-color: #fff0d6;
                font-family: Verdana, sans-serif;
                text-align: center;
                padding: 50px;
            }

            h1 {
                color: #b45f06;
            }

            p {
                font-size: 18px;
            }
        </style>
    </head>

    <body>
        <h1>Contato</h1>
        <p>Projeto desenvolvido por Kennedy Vieira Teixeira.</p>
        <p>Trabalho de RASI - 2026.</p>
    </body>
    </html>
    """


app.run(host="0.0.0.0", port=5000)