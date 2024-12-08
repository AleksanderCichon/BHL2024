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

            # Insert the zodiac sign into the FlightData table
        try:
            date_time_data = form_data["date"] + " "+form_data["time"]
            cursor.execute('''
                INSERT INTO FlightData (ZodiacSign, Planet, Date, Seat)
                VALUES (?,?,?,?);
            ''', (form_data["zodiac_sign"], form_data["destination"], date_time_data, form_data["seat-number"]))
            print(conn)
            conn.commit()
            print("Insert succesful")
            # conn.close()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        
        return redirect(url_for("payment"))
        # return destination
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Execute a query to fetch data
    cursor.execute("SELECT * FROM ZodiacSignToDestination")

    rows = cursor.fetchall()  # Retrieves all rows as a list of tuples
    clean_rows = [i[1] for i in rows]
    # Close the connection
    conn.close()

    print(rows)
    return render_template("choose_user.html", planets = clean_rows)

@app.route("/choose-space", methods=["GET", "POST"])
def choose_space():
    print("dupa1")
    if request.method == "POST":
        print("dupa2")
        # Retrieve the selected zodiac sign from the form
        zodiac_sign = request.form.get('zodiac_signs')
        print("aaaaa")
        # session['zodiac_sign'] = zodiac_sign
        print("aaaaa")
        form_data["zodiac_sign"] = zodiac_sign
        print("aaaaa")
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

            return redirect(url_for("destiny"))
        else:
            print("No zodiac sign selected.")
            
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Execute a query to fetch data
    cursor.execute("SELECT * FROM ZodiacSignToDestination")

    rows = cursor.fetchall()  # Retrieves all rows as a list of tuples
    clean_rows = [i[0] for i in rows]
    # Close the connection
    conn.close()
    return render_template("choose_space.html", zodiacs = clean_rows)

def get_desc_from_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Description FROM ZodiacSignToDestination ORDER BY ROWID DESC LIMIT 1")
    zodiac_sign = cursor.fetchone()
    conn.close()
    return zodiac_sign[0] if zodiac_sign else "Not chosen"

@app.route("/schedule_zodiac_flight", methods=["GET", "POST"])
def schedule_zodiac_flight():
    # zoidiac_sign = get_last_zodiac_sign_from_db()
    # print(zoidiac_sign)
    
    return render_template("schedule_zodiac_flight.html")

@app.route("/destiny",methods=["POST", "GET"])
def destiny():
    description = get_desc_from_db()
    print(description)
    return render_template("destiny.html", description=description)

if __name__ == "__main__":
    app.run(debug=True)