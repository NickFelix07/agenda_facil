from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.models import Servico
from app import db

servicos = Blueprint('servicos', __name__, url_prefix='/servicos')

@servicos.route('/')
@login_required
def index():
    servicos_list = Servico.query.all()
    return render_template('servicos/index.html', servicos=servicos_list)

@servicos.route('/novo', methods=['GET', 'POST'])
@login_required
def novo():
    if request.method == 'POST':
        servico = Servico(
            nome=request.form.get('nome'),
            preco=float(request.form.get('preco')),
            duracao_minutos=int(request.form.get('duracao'))
        )
        db.session.add(servico)
        db.session.commit()
        flash('Serviço cadastrado!')
        return redirect(url_for('servicos.index'))
    return render_template('servicos/novo.html')
