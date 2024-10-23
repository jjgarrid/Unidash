from app.routes import db, User

def create_user(name, email):
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
