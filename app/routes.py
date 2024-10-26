from flask import Flask, render_template, request, redirect, url_for, send_file
from flask_sqlalchemy import SQLAlchemy
from app.models import db, User
from app.backend import create_user, generate_files

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

@app.route('/pared2d')
def pared2d():
    """
    Renderizar la página de Pared 2D.

    :return: La plantilla de la página de Pared 2D renderizada
    :rtype: str
    """
    return render_template('pared2d.html')

@app.route('/pared3d')
def pared3d():
    """
    Renderizar la página de Pared 3D.

    :return: La plantilla de la página de Pared 3D renderizada
    :rtype: str
    """
    return render_template('pared3d.html')

@app.route('/barovel')
def barovel():
    """
    Renderizar la página de Barovel.

    :return: La plantilla de la página de Barovel renderizada
    :rtype: str
    """
    return render_template('barovel.html')

@app.route('/generate_files', methods=['POST'])
def generate_files_route():
    """
    Manejar la generación de archivos y la ejecución de comandos.

    :return: Una respuesta de redirección a la página de inicio
    :rtype: werkzeug.wrappers.Response
    """
    template_folder = request.form['template_folder']
    output_folder = request.form['output_folder']
    params = request.form.to_dict()
    generated_file_path = generate_files(template_folder, output_folder, params)
    return send_file(generated_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
