from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///video.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   content = db.Column(db.String(200), nullable=False)
   difficulty = db.Column(db.String(200), nullable=False)
   topic = db.Column(db.String(200), nullable=False)
   date_uploaded = db.Column(db.DateTime, default=datetime.utcnow)

   def __repr__(self):
      return '<Task %r>' % self.id

VIDEOS = [
  {
    'id': 1,
    'title': 'Chain Rule',
    'level': '12',
    'difficulty': 'Hard',
    'topic': 'Calculus' 
  },
  {
    'id': 2,
    'title': 'Pythagorean Theorem',
    'level': '10',
    'difficulty': 'Easy',
    'topic': 'Trigonometry' 
  },
  {
    'id': 3,
    'title': 'Binomial Distribution',
    'level': '11',
    'difficulty': 'Medium',
    'topic': 'Statistics' 
  },
  {
    'id': 4,
    'title': 'Translations',
    'level': '11',
    'difficulty': 'Medium',
    'topic': 'Affine Transformations' 
  },
]

@app.route("/", methods=['POST', 'GET'])
def hello_world():
    return render_template('login.html', videos=VIDEOS)

@app.route('/home', methods=['POST', 'GET'])
def login():
   return render_template('home.html', videos=VIDEOS)

@app.route('/admin', methods=['POST', 'GET'])
def admin():
   if request.method == 'POST':
      task_content = request.form['content']
      task_difficulty = request.form['difficulty']
      task_topic = request.form['topic']
      new_task = Todo(content=task_content, difficulty= task_difficulty, topic=task_topic)
      
      

      try:
         db.session.add(new_task)
         db.session.commit()
         return redirect('/admin')
      except: 
         return 'There was an issue adding your task'
   else:
      tasks = Todo.query.order_by(Todo.date_uploaded).all()
      return render_template('admin.html', videos=VIDEOS, tasks=tasks)
   
@app.route('/delete/<int:id>')
def delete(id):
   task_to_delete = Todo.query.get_or_404(id)

   try: 
      db.session.delete(task_to_delete)
      db.session.commit()
      return redirect('/admin')
   except:
      return 'There was a problem deleting that task'
   

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)