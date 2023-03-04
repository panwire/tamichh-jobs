from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='templates')

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bonadikombo, Limbe',
    'salary': '200.000 FRS CFA'
  },
  {
    'id': 2,
    'title': 'Chief Engineer',
    'location': 'Isokolo, Limbe',
    'salary': '600.000 FRS CFA'
  },
  {
    'id': 3,
    'title': 'Executive Accountant',
    'location': 'Down Beach, Limbe',
    'salary': '400.000 FRS CFA'
  },
  {
    'id': 4,
    'title': 'Polic Officer',
    'location': 'Middle Farms, Limbe',
    'salary': '130.000 FRS CFA'
  },
  {
    'id': 5,
    'title': 'Bank Clerk',
    'location': 'Church Street, Limbe',
    'salary': '150.000 FRS CFA'
  },
]


@app.route("/")
def hello_home():
  return render_template('home.html', jobs=JOBS, company_name="Tamichh")


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
