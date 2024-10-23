from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from app.backend import create_user

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/')
def home():
    """
    Render the home page.

    :return: The rendered home page template
    :rtype: str
    """
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    """
    Handle form submission, create a new user, and redirect to the home page.

    :return: A redirect response to the home page
    :rtype: werkzeug.wrappers.Response
    """
    name = request.form['name']
    email = request.form['email']
    create_user(name, email)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
