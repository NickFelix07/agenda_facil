from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import db

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    perfil = db.Column(db.String(20), default='funcionario')  # admin ou funcionario

    def __repr__(self):
        return f'<Usuario {self.nome}>'

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120))
    data_nascimento = db.Column(db.Date)
    observacoes = db.Column(db.Text)
    agendamentos = db.relationship('Agendamento', backref='cliente', lazy=True)

    def __repr__(self):
        return f'<Cliente {self.nome}>'

class Profissional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especialidade = db.Column(db.String(100))
    telefone = db.Column(db.String(20))
    agendamentos = db.relationship('Agendamento', backref='profissional', lazy=True)

    def __repr__(self):
        return f'<Profissional {self.nome}>'

class Servico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    duracao_minutos = db.Column(db.Integer, nullable=False)
    agendamentos = db.relationship('Agendamento', backref='servico', lazy=True)

    def __repr__(self):
        return f'<Servico {self.nome}>'

class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_horario = db.Column(db.DateTime, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    profissional_id = db.Column(db.Integer, db.ForeignKey('profissional.id'), nullable=False)
    servico_id = db.Column(db.Integer, db.ForeignKey('servico.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    status = db.Column(db.String(20), default='confirmado')  # confirmado, cancelado, concluido
    observacoes = db.Column(db.Text)

    def __repr__(self):
        return f'<Agendamento {self.data_horario}>'
