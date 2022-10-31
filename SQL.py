from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import os
import time
from datetime import datetime, date


os.environ["TZ"] = "America/Recife"
time.tzset()

header_key = '*'


# configuração base do sqlalchemy
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://kaigabriel12:372306kai@kaigabriel12.mysql.pythonanywhere-services.com/kaigabriel12$rec'
db = SQLAlchemy(app)

# etapa 1 - criação do db
# no console python
# >>> from flask_app import db
# >>> db.create_all()
# flask db init
#

# criação da classe com a estrutura da tabela Usuario
class Dados(db.Model):
    id_voto = db.column(db.Interger, primary_key=True)
    data_hora = db.column(db.String(20))
    nome_modelo = db.column(db.String(20))

    def to_json(self):
        return {"id": self.id_voto, "data_hora": self.data_hora, "nome_modelo": self.nome_modelo }
