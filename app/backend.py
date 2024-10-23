import logging
from app.routes import db, User

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_user(name, email):
    """
    Create a new user and add to the database.

    :param name: The name of the user
    :type name: str
    :param email: The email of the user
    :type email: str
    """
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    logger.info(f"User created: {name}, {email}")
