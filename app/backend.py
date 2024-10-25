from app.models import db, User
import os
import subprocess
import jinja2

def log_message(message):
    """
    Imprimir un mensaje de registro.

    :param message: El mensaje a imprimir
    :type message: str
    """
    print(f"LOG: {message}")

def create_user(name, email):
    """
    Crear un nuevo usuario y agregarlo a la base de datos.

    :param name: El nombre del usuario
    :type name: str
    :param email: El correo electrónico del usuario
    :type email: str
    """
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    log_message(f"Usuario creado: {name}, {email}")

def generate_files(template_folder, output_folder, params):
    """
    Generar archivos a partir de plantillas y ejecutar un comando de línea de comandos.

    :param template_folder: La carpeta que contiene las plantillas
    :type template_folder: str
    :param output_folder: La carpeta donde se guardarán los archivos generados
    :type output_folder: str
    :param params: Los parámetros proporcionados por el usuario
    :type params: dict
    """
    # Crear el entorno de Jinja2
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_folder))

    # Iterar sobre las plantillas en la carpeta de plantillas
    for template_name in os.listdir(template_folder):
        template = env.get_template(template_name)
        output_content = template.render(params)

        # Guardar el archivo generado en la carpeta de salida
        output_path = os.path.join(output_folder, template_name)
        with open(output_path, 'w') as output_file:
            output_file.write(output_content)

    # Ejecutar un comando de línea de comandos
    command = ["echo", "Archivos generados con éxito"]
    subprocess.run(command)
