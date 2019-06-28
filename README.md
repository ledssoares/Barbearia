# Barbearia
Aplicação do Barbearia

# Instruções para execução
```
git clone https://github.com/ledssoares/Barbearia
cd Barbearia
python3 -m venv venv
source venv/bin/activate
pip install flask flask-bootstrap flask-moment flask-wtf flask-sqlalchemy flask-migrate
```
# Adicionando valores ao banco de dados:

```python
flask shell
from app import db
db.create_all()

cliente = Cliente(nome="Milena", email="milena@gmail.com, telefone=40028922)
cliente = Cliente(nome="Drielle", email="drielle@gmail.com, telefone=40028923)
cliente = Cliente(nome="Victor", email="victor@gmail.com, telefone=40028924)
cliente = Cliente(nome="Leticia", email="leticia@gmail.com, telefone=40028925)

db.session.add(cliente)
db.session.add(cliente)
db.session.commit()
# CTRL+D para sair
```
# Executando a aplicação

```
export FLASK_APP=app.py
flask run -p 8080
```

# Autores
```
Victor da Silva 
Leticia de Sousa
Drielle de Moura
Milena Batista
```
