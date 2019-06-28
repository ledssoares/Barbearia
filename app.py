import os
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField, HiddenField
from wtforms.validators import DataRequired, NumberRange, Optional
#from wtforms.fields.html5 import IntegerField
from wtforms.widgets.html5 import NumberInput
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(128), index=True)
    Data_de_nascimento=db.Column(db.String(64))
    Telefone = db.Column(db.String(64))
    Email = db.Column(db.String(64), unique=True)
    
    
class Myform(FlaskForm):
    Nome = StringField('Nome', validators=[DataRequired()])
    Data_de_nascimento=DateField('Data de Nascimento', format='%d/%m/%Y', validators=[Optional()])
    Telefone = StringField('Telefone', validators=[DataRequired()])
    Email = StringField('E-mail', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')


@app.route("/Cadastrar", methods=['GET', 'POST'])
def cadastrar():
    form = Myform()
    if form.validate_on_submit():

        cliente = Cliente(Nome=form.Nome.data, Data_de_nascimento=form.Data_de_nascimento.data, Email=form.Email.data, Telefone=form.Telefone.data)
        
        
        db.session.add(cliente)
        db.session.commit()

        return redirect("inicio")
    return render_template("Cadastrar.html", form=form)
    
    
@app.route('/', methods=['GET'])
def inicio():
    clientes = Cliente.query.all()
    return render_template('Inicio.html', clientes=clientes)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
    
@app.route('/Cadastrar', methods=['GET','POST'])
def Cadastrar():
    form = Cadastrar()
    
    return render_template('Cadastrar', form=form)