from flask import Flask, render_template, url_for, request, redirect, session
from flask.ctx import F
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

SECRET_KEY = "KEY"
app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exercises.db'
db = SQLAlchemy(app)


class Users(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Exercise %r>' % self.userID

class Exercises(db.Model):
    logID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    userID = db.Column(db.Integer, foreign_key=True)
    
    def __repr__(self):
        return '<Exercise %r>' % self.logID
    
"""
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Task %r>' % self.id
"""
    
with app.app_context():
    db.create_all()

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        user_email = request.form['email']
        user_password = request.form['password']
        
        if not (user_email and user_password):
            return render_template('register.html', message="All fields are required.")
        
        hashed_password = generate_password_hash(user_password)
        new_user = Users(email=user_email, password=hashed_password)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')
        except:
            return "There was an issue creating your account"
    return render_template("register.html")
            
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user_email = request.form['email']
        user_password = request.form['password']

        user = Users.query.filter(Users.email == user_email).first()
            
        if user and check_password_hash(user.password, user_password):
            session["userID"] = user.userID
            return redirect('/tracker')
        else:
            return render_template('login.html', message="Invalid email or password")
    return render_template('login.html')

@app.route('/tracker', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        exercise_name = request.form['name']
        exercise_reps = request.form['reps']
        unextracted_date = request.form['date']
        exercise_date = datetime.strptime(unextracted_date, '%Y-%m-%d')
        new_exercise = Exercises(name=exercise_name, reps=exercise_reps, date=exercise_date, userID = session["userID"])
        
        if not (exercise_name and exercise_reps):
            return render_template('index.html', message="All fields are required.")
        try:
            db.session.add(new_exercise)
            db.session.commit()
            return redirect('/tracker')
        except:
            return "There was an issue adding your exercise"
    else:
        exercises = Exercises.query.filter(Exercises.userID == session["userID"]).order_by(Exercises.date).all()
        return render_template('index.html', exercises=exercises)
    
@app.route('/delete/<int:logID>')
def delete(logID):
    entry_to_delete = Exercises.query.get_or_404(logID)
    
    try:
        db.session.delete(entry_to_delete)
        db.session.commit()
        return redirect('/tracker')
    except:
        return "There was an error deleting the exercise"

@app.route('/update/<int:logID>', methods=['GET','POST'])
def update(logID):
    entry_to_update = Exercises.query.get_or_404(logID)
    if request.method == 'POST':
        entry_to_update.name = request.form['name']
        entry_to_update.reps = request.form['reps']
        unextracted_date = request.form['date']
        entry_to_update.date = datetime.strptime(unextracted_date, '%Y-%m-%d')

        try:
            db.session.commit()
            return redirect('/tracker')
        except:
            return "There was an issue updating your exercise"
    else:
        return render_template('update.html', exercise = entry_to_update)



"""
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
            
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)        

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'
 
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        
        try:
            db.session.commit()
            return  redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', task=task)
"""
        
if __name__ == "__main__":
    app.run(debug=True)