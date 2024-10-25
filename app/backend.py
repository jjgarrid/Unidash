from app.routes import db, User

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
