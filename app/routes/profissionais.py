from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.models import Profissional
from app import db

profissionais = Blueprint('profissionais', __name__, url_prefix='/profissionais')

@profissionais.route('/')
@login_required
def index():
    profissionais_list = Profissional.query.all()
    return render_template('profissionais/index.html', profissionais=profissionais_list)

@profissionais.route('/novo', methods=['GET', 'POST'])
@login_required
def novo():
    if request.method == 'POST':
        profissional = Profissional(
            nome=request.form.get('nome'),
            especialidade=request.form.get('especialidade'),
            telefone=request.form.get('telefone')
        )
        db.session.add(profissional)
        db.session.commit()
        flash('Profissional cadastrado!')
        return redirect(url_for('profissionais.index'))
    return render_template('profissionais/novo.html')
