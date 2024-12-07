from flask import Flask, render_template, request,redirect, url_for

app = Flask(__name__)




# Route for the home page
@app.route("/")
def home():
    return render_template("index.html")  # Renders the HTML file


# Route to handle form submissions or API calls
@app.route("/submit", methods=["POST"])
def submit():
    data = request.form["input_name"]  # Gets data from a form
    return f"Received: {data}"

form_data = {}
@app.route("/choose-user", methods=["GET", "POST"])
def choose_user():
    print("SUPEEEEE")
    if request.method == "POST":
        form_data["zodiac-sign"] = None
        form_data["destination"]  = request.form.get("select-destination")
        form_data["seat-number"] = request.form.get("select-seat-number")
        form_data["date"] = request.form.get("select-date")
        form_data["time"] = request.form.get("select-time")
        form_data["email"] = request.form.get("select-email")
        print(form_data)
        return redirect(url_for("payment"))
        # return destination
    
    return render_template("choose_user.html")

@app.route("/payment")
def payment():
    return render_template("payment.html")

@app.route("/choose-space", methods=["GET", "POST"])
def choose_space():
    if request.method == "POST":
        form_data["zodiac-sign"] = request.form.get("zodiac_signs")
        return redirect(url_for("destiny"))

    print(request.method)
    return render_template("choose_space.html")

@app.route("/destiny",methods=["POST", "GET"])
def destiny():
    if form_data["zodiac-sign"]:
        if request.method == "POST":
            return redirect(url_for("payment"))
        return render_template("destiny.html")
    return "<h1>Zodiac sign was not choosen</h1>"
if __name__ == "__main__":
    app.run(debug=True)