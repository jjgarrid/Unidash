from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from app.models import db, User
from app.backend import create_user

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

@app.route('/')
def home():
    """
    Renderizar la página de inicio.

    :return: La plantilla de la página de inicio renderizada
    :rtype: str
    """
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    """
    Manejar el envío del formulario, crear un nuevo usuario y redirigir a la página de inicio.

    :return: Una respuesta de redirección a la página de inicio
    :rtype: werkzeug.wrappers.Response
    """
    name = request.form['name']
    email = request.form['email']
    create_user(name, email)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
