import logging
from app.routes import db, User

# Configurar el registro
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
    logger.info(f"Usuario creado: {name}, {email}")
