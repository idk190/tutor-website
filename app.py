from flask import Flask, render_template

app = Flask(__name__)

VIDEOS = [
  {
    'id': 1,
    'title': 'Chain Rule',
    'level': 'Grade 12',
    'difficulty': 'Hard',
    'topic': 'Calculus' 
  },
  {
    'id': 2,
    'title': 'Pythagorean Theorum',
    'level': 'Grade 10',
    'difficulty': 'Easy',
    'topic': 'Trigonometry' 
  },
  {
    'id': 3,
    'title': 'Binomial Distribution',
    'level': 'Grade 11',
    'difficulty': 'Medium',
    'topic': 'Statistics' 
  },
  {
    'id': 4,
    'title': 'Translations',
    'level': 'Grade 11',
    'difficulty': 'Medium',
    'topic': 'Affine Transformations' 
  },
]
@app.route("/")
def hello_world():
    return render_template('home.html', videos=VIDEOS)

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)