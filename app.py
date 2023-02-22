from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Python Developer',
    'location': 'Berlin, Germany',
    'salary': '15,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'London, UK',
    'salary': '20,000'
  },
  {
    'id': 3,
    'title': 'React Developer',
    'location': 'New York, USA',
    'salary': '10,000'
  },
  {
    'id': 4,
    'title': 'Data Engineer',
    'location': 'Absterdam, Netherlands',
    'salary': '150,000'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="Turin")


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
