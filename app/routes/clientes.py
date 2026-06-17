from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.models import Cliente
from app import db

clientes = Blueprint('clientes', __name__, url_prefix='/clientes')

@clientes.route('/')
@login_required
def index():
    clientes_list = Cliente.query.all()
    return render_template('clientes/index.html', clientes=clientes_list)

@clientes.route('/novo', methods=['GET', 'POST'])
@login_required
def novo():
    if request.method == 'POST':
        cliente = Cliente(
            nome=request.form.get('nome'),
            telefone=request.form.get('telefone'),
            email=request.form.get('email'),
            data_nascimento=request.form.get('data_nascimento'),
            observacoes=request.form.get('observacoes')
        )
        db.session.add(cliente)
        db.session.commit()
        flash('Cliente cadastrado com sucesso!')
        return redirect(url_for('clientes.index'))
    return render_template('clientes/novo.html')
