
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("floods.save")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict")
def predict_page():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    temp = float(request.form["Temp"])
    humidity = float(request.form["Humidity"])
    cloud_cover = float(request.form["Cloud_Cover"])
    annual_rainfall = float(request.form["Annual_Rainfall"])
    jan_feb = float(request.form["Jan_Feb_Rainfall"])
    mar_may = float(request.form["Mar_May_Rainfall"])
    jun_sep = float(request.form["Jun_Sep_Rainfall"])
    oct_dec = float(request.form["Oct_Dec_Rainfall"])
    avgjune = float(request.form["avgjune"])
    sub = float(request.form["sub"])

    data = np.array([[
        temp,
        humidity,
        cloud_cover,
        annual_rainfall,
        jan_feb,
        mar_may,
        jun_sep,
        oct_dec,
        avgjune,
        sub
    ]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        return render_template("chance.html")
    else:
        return render_template("no_chance.html")
if __name__ == "__main__":
    app.run(debug=True)