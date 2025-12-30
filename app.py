import numpy as np
from flask import Flask, request, render_template
import joblib
     
app = Flask(__name__)
model = joblib.load(r"C:\Arman\FSDS GenAI 2025\Practicals\Projects\New folder\student_mark_predictor.pkl")


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            hours = float(request.form["hours"])

            if hours <= 0 or hours > 24:
                error = "Please enter valid hours between 1 and 24."
            else:
                predicted_value = model.predict(np.array([[hours]]))[0]
                predicted_value = round(float(predicted_value), 2)
                prediction = f"For {hours} hours of study, the predicted marks are {predicted_value}."

        except ValueError:
            error = "Please enter a valid number."

    return render_template("index.html", prediction=prediction, error=error)


if __name__ == "__main__":
    app.run(debug=True)