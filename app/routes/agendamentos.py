from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from datetime import datetime
from app.models.models import Agendamento, Cliente, Profissional, Servico
from app import db

agendamentos = Blueprint('agendamentos', __name__, url_prefix='/agendamentos')

@agendamentos.route('/')
@login_required
def index():
    agendamentos_list = Agendamento.query.order_by(Agendamento.data_horario).all()
    return render_template('agendamentos/index.html', agendamentos=agendamentos_list)

@agendamentos.route('/novo', methods=['GET', 'POST'])
@login_required
def novo():
    if request.method == 'POST':
        data_str = request.form.get('data_horario')
        data_horario = datetime.fromisoformat(data_str.replace('T', ' '))
        
        agendamento = Agendamento(
            data_horario=data_horario,
            cliente_id=int(request.form.get('cliente_id')),
            profissional_id=int(request.form.get('profissional_id')),
            servico_id=int(request.form.get('servico_id')),
            observacoes=request.form.get('observacoes')
        )
        db.session.add(agendamento)
        db.session.commit()
        flash('Agendamento realizado com sucesso!')
        return redirect(url_for('agendamentos.index'))
    
    clientes = Cliente.query.all()
    profissionais = Profissional.query.all()
    servicos = Servico.query.all()
    return render_template('agendamentos/novo.html', clientes=clientes, profissionais=profissionais, servicos=servicos)
