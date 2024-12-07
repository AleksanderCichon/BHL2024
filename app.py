from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import queries

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

@app.route("/payment")
def payment():
    return render_template("payment.html")

form_data = {}
@app.route("/choose-user")
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

@app.route("/choose-space", methods=["GET", "POST"])
def choose_space():
    if request.method == "POST":
        # Retrieve the selected zodiac sign from the form
        zodiac_sign = request.form.get('select_zodiac_sign')
        print(f"Selected Zodiac Sign: {zodiac_sign}")

        if zodiac_sign:  # Check if a value was submitted
            # Connect to the database
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            # Insert the zodiac sign into the ZodiacInfo table
            cursor.execute('''
                INSERT INTO ZodiacInfo (ZodiacSign)
                VALUES (?);
            ''', (zodiac_sign,))

            conn.commit()
            conn.close()
        else:
            print("No zodiac sign selected.")
    return render_template("choose_space.html")

@app.route("/schedule_zodiac_flight", methods=["GET", "POST"])
def schedule_zodiac_flight():
    # Function to handle flight scheduling
    return render_template("schedule_zodiac_flight.html")

if __name__ == "__main__":
    app.run(debug=True)