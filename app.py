from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost:3306/db_name'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    role = db.Column(db.String(120))

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(1200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            # login and redirect to dashboard
            return redirect('/dashboard')
        else:
            # display error message
            return render_template('login.html', error="Invalid username or password")
    else:
        return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        user = User(username=username, password=password, role=role)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    else:
        return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    # display events and chat functionality
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run()
