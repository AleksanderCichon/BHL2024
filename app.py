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
@app.route("/choose-user", methods=["GET", "POST"])
def choose_user():
    print("SUPEEEEE")
    if request.method == "POST":
        form_data["zodiac_sign"] = None
        form_data["destination"]  = request.form.get("select-destination")
        form_data["seat-number"] = request.form.get("select-seat-number")
        form_data["date"] = request.form.get("select-date")
        form_data["time"] = request.form.get("select-time")
        form_data["email"] = request.form.get("select-email")
        print(form_data)
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

            # Insert the zodiac sign into the ZodiacInfo table
        cursor.execute('''
            INSERT INTO FlightData (ZodiacSign, Planet, Date, Seat)
            VALUES (?,?,?,?);
        ''', (form_data["zodiac-sign"], form_data["destination"], form_data["date"] + " " + form_data["time"], form_data["seat-number"]))

        conn.commit()
        conn.close()
        return redirect(url_for("payment"))
        # return destination
    
    return render_template("choose_user.html")

@app.route("/choose-space", methods=["GET", "POST"])
def choose_space():
    if request.method == "POST":
        # Retrieve the selected zodiac sign from the form
        zodiac_sign = request.form.get('zodiac_signs')
        session['zodiac_sign'] = zodiac_sign
        form_data["zodiac_sign"] = zodiac_sign
        print(f"Selected Zodiac Sign: {zodiac_sign}")

        if zodiac_sign:  # Check if a value was submitted
            # Connect to the database
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            # Insert the zodiac sign into the FlightData table
            cursor.execute('''
                INSERT INTO FlightData (ZodiacSign)
                VALUES (?);
            ''', (zodiac_sign,))

            conn.commit()
            conn.close()
        else:
            print("No zodiac sign selected.")
            
    return render_template("choose_space.html")

def get_last_zodiac_sign_from_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT ZodiacSign FROM FlightData ORDER BY ROWID DESC LIMIT 1")
    zodiac_sign = cursor.fetchone()
    conn.close()
    return zodiac_sign[0] if zodiac_sign else "Not chosen"

@app.route("/schedule_zodiac_flight", methods=["GET", "POST"])
def schedule_zodiac_flight():
    zoidiac_sign = get_last_zodiac_sign_from_db()
    print(zoidiac_sign)
    
    return render_template("schedule_zodiac_flight.html")

@app.route("/destiny",methods=["POST", "GET"])
def destiny():
    return render_template("destiny.html")

if __name__ == "__main__":
    app.run(debug=True)