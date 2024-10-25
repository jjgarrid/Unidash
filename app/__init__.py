from app.routes import app
from app.models import db

db.init_app(app)
