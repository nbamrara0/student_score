import os
import pickle
import pandas as pd
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

model=pickle.load(open("student_score_model.pkl", "rb"))

# https://gunvattagurukul.qcin.org/user/all-level-registration.aspx
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    hours_studied = db.Column(db.Float, nullable=False)
    attendance = db.Column(db.Float, nullable=False)
    previous_score = db.Column(db.Float, nullable=False)
    predicted_score = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()


@app.route("/",methods=["GET", "POST"])
def home ():
   return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    name = request.form.get("name", "").strip()
    hours_studied = float(request.form.get("hours_studied", 0))
    attendance = float(request.form.get("attendance", 0))
    previous_score = float(request.form.get("previous_score", 0))

    input_df = pd.DataFrame(
        [[hours_studied, attendance, previous_score]],
        columns=["hours_studied", "attendance", "previous_score"],
    )
    prediction = model.predict(input_df)[0]

    student = Student(
        name=name,
        hours_studied=hours_studied,
        attendance=attendance,
        previous_score=previous_score,
        predicted_score=prediction,
    )
    db.session.add(student)
    db.session.commit()

    return render_template("index.html", prediction=prediction)

if __name__=="__main__":
    app.run(debug=True)