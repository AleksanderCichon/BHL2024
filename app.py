from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route("/")
def home():
    return render_template("index.html")  # Renders the HTML file

# Route to handle form submissions or API calls
@app.route("/submit", methods=["POST"])
def submit():
    data = request.form['input_name']  # Gets data from a form
    return f"Received: {data}"

if __name__ == "__main__":
    app.run(debug=True)
