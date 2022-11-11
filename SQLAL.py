from flask import Flask, request, render_template, url_for, redirect,json
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://kaigabriel:372306kai@kaigabriel.mysql.pythonanywhere-services.com/kaigabriel$default'
db = SQLAlchemy(app)

# etapa 1 - criação do db
# no console python
# >>> from flask_app import db
# >>> db.create_all()
# flask db init
#

# criação da classe com a estrutura da tabela Usuario
class votacao(db.Model):
    id_voto = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.String(20))
    hora = db.Column(db.String(20))
    nome_modelo = db.Column(db.String(20),nullable=False)
    avaliacao = db.Column(db.Integer,nullable=False)

    def to_json(self):
        return {"id": self.id_voto,"data": self.data, "hora": self.hora, "nome_modelo": self.nome_modelo, "avaliacao": self.avaliacao }

class curtida(db.Model):
    id_voto = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.String(20))
    hora = db.Column(db.String(20))
    nome_modelo = db.Column(db.String(20),nullable=False)

    def to_json(self):
        return {"id": self.id_voto,"data": self.data, "hora": self.hora, "nome_modelo": self.nome_modelo}

@app.route('/voto')
def inserir():
    data = str(datetime.today().strftime("%d/%m/%Y"))
    hora = str(datetime.time(datetime.now()))
    hora = hora[0:8]
    nome_modelo=str("Rec's n Play")
    avaliacao = 5
    novo = votacao(data=data,hora=hora, nome_modelo=nome_modelo,avaliacao=avaliacao)
    db.session.add(novo)
    db.session.commit()
    return str({"Data":data,"Hora":hora,"Nome Do Modelo":nome_modelo, "Avaliação":avaliacao})

@app.route('/curtida')
def curtir():
    data = str(datetime.today().strftime("%d/%m/%Y"))
    hora = str(datetime.time(datetime.now()))
    hora = hora[0:8]
    nome_modelo=str("Play")
    novo = curtida(data=data,hora=hora, nome_modelo=nome_modelo)
    db.session.add(novo)
    db.session.commit()
    return str({"Data":data,"Hora":hora,"Nome Do Modelo":nome_modelo})

@app.route('/consulta')
def consulta():
    consulta = curtida.query.filter(curtida.nome_modelo.like("Rec's n Play"))
    return str(consulta.count())

@app.route('/busca', methods=['GET'])
def busca():
    consulta=  curtida.query.all()
    curtir=[]
    for c in consulta:
        curtir.append({'id': c.id_voto,'data': c.data, 'hora': c.hora, 'nome do modelo': c.nome_modelo })
    return json.dumps(curtir)