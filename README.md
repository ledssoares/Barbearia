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
from datetime import date
db.create_all()


hoje = date.today()

cliente = Cliente(nome="Milena", email="milena@gmail.com", telefone="40028922", data_de_nascimento=hoje)
cliente = Cliente(nome="Drielle", email="drielle@gmail.com", telefone="40028923", data_de_nascimento=hoje)
cliente = Cliente(nome="Victor", email="victor@gmail.com", telefone="40028924", data_de_nascimento=hoje)
cliente = Cliente(nome="Leticia", email="leticia@gmail.com", telefone="40028925", data_de_nascimento=hoje)

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
