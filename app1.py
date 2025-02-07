from flask import Flask, request, render_template, redirect, url_for, session
import pymysql

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Konfigurasi Database
db = pymysql.connect(host="localhost", user="root", password="", database="login_system")
cursor = db.cursor()

@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("dashboard"))
    return render_template("index1.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
    user = cursor.fetchone()

    if user:
        session["user"] = user[1]  # Simpan email ke sesi
        return redirect(url_for("dashboard"))
    else:
        return "Login failed. Invalid credentials."

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("home"))
    return render_template("dashboard1.html", user=session["user"])

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
