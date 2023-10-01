from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///video.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Video_List(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(200), nullable=False)
   level = db.Column(db.String(200), nullable=False)
   difficulty = db.Column(db.String(200), nullable=False)
   topic = db.Column(db.String(200), nullable=False)
   link = db.Column(db.String(200), nullable=False)
   date_uploaded = db.Column(db.DateTime, default=datetime.utcnow)

   def __repr__(self):
      return f'{self.id} {self.title}'

##VIDEOS = Video_List.query.all()##

@app.route("/", methods=['POST', 'GET'])
def hello_world():
    listvid = Video_List.query.all()
    return render_template('login.html', videos=listvid)

@app.route('/home', methods=['POST', 'GET'])
def login():
   listvid = Video_List.query.all()
   return render_template('home.html', videos=listvid)

@app.route('/admin', methods=['POST', 'GET'])
def admin():
   listvid = Video_List.query.all()
   if request.method == 'POST':
      task_title = request.form['title']
      task_level = request.form['level']
      task_difficulty = request.form['difficulty']
      task_topic = request.form['topic']
      task_link = request.form['link']
      new_task = Video_List(title= task_title, level= task_level, difficulty= task_difficulty, topic=task_topic, link= task_link)
      
      

      try:
         db.session.add(new_task)
         db.session.commit()
         return redirect('/admin')
      except: 
         return 'There was an issue adding your task'
   else:
      tasks = Video_List.query.order_by(Video_List.date_uploaded).all()
      return render_template('admin.html', videos=listvid, tasks=tasks)
   
@app.route('/delete/<int:id>')
def delete(id):
   task_to_delete = Video_List.query.get_or_404(id)

   try: 
      db.session.delete(task_to_delete)
      db.session.commit()
      return redirect('/admin')
   except:
      return 'There was a problem deleting that task'
   

if __name__=="__main__":
  app.run(debug=True)