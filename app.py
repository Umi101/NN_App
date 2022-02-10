from flask import Flask
app = Flask(__name__)

from flask import request, render_template
import joblib

@app.route("/", methods = ["GET", "POST"])
def i():
    if request.method == "POST":
        sugar = request.form.get("sugar")
        milk = request.form.get("milk")
        print(sugar, milk)
        model = joblib.load("Chocolate")
        pred = model.predict([[float(sugar), float(milk)]])
        pred = pred[0]
        print(pred)
        s = "The predicted taste is " + str(pred)
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result = "Chocolate Taste Prediction"))

if __name__ == '__main__':
    app.run()

