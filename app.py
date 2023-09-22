from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(200), nullable=False)
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
    return render_template('home.html', videos=VIDEOS)

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)