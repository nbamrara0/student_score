import os
import pickle
import pandas as pd
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

model=pickle.load(open("student_score_model.pkl", "rb"))

# https://gunvattagurukul.qcin.org/user/all-level-registration.aspx

@app.route("/",methods=["GET", "POST"])
def home ():
   return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    hours_studied=float(request.form.get("hours_studied", 0))
    attendance=float(request.form.get("attendance", 0))
    previous_score=float(request.form.get("previous_score", 0))

    input_df = pd.DataFrame(
        [[hours_studied, attendance, previous_score]],
        columns=["hours_studied", "attendance", "previous_score"],
    )
    prediction = model.predict(input_df)
    return render_template("index.html", prediction=prediction[0])

if __name__=="__main__":
    app.run(debug=True)