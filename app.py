import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_locations")
def get_locations():
    locations = mongo.db.locations.find()
    return render_template("locations.html", locations=locations)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Retrieve form data
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Check if username already exists
        existing_user = mongo.db.user.find_one({"username": username.lower()})
        if existing_user:
            flash("Username already exists", "error")
            return redirect(url_for("register"))

        # Check if passwords match
        if password != confirm_password:
            flash("Passwords do not match", "error")
            return redirect(url_for("register"))

        # Hash the password using werkzeug's generate_password_hash
        password_hash = generate_password_hash(password)

        # Insert the new user into the database
        register = {
            "username": username.lower(),
            "password": password_hash
        }
        mongo.db.user.insert_one(register)

        # Put the new user into 'session' cookie
        session["user"] = username.lower()
        flash("Registration Successful!", "success")
        return redirect(url_for("register"))  # Redirect to the home page or wherever you'd like

    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
