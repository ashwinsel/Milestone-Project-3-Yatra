import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
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
    locations = list (mongo.db.locations.find())
    return render_template("home.html", locations=locations)


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
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")  # Redirect to the register page

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash(f"You are successfully logged in as, {request.form.get('username')}")
                    return redirect(url_for("profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # pulls through session user's username value from database
    username = mongo.db.user.find_one({"username": session["user"]})["username"]

    if session["user"]:
        return render_template("home.html", username=username)
    
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been signed out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/browse_sites")
def browse_sites():
    locations = mongo.db.locations.find()
    return render_template("browse_sites.html", locations=locations)    


@app.route("/add_site", methods=["GET", "POST"])
def add_site():
    if request.method == "POST":
        try:
            # Retrieve form data
            site_name = request.form.get("site_name")
            deity = request.form.get("deity")
            part_name = request.form.get("part_name")
            description = request.form.get("description")

            # Check if the 'access' checkbox is ticked
            disabled_access = request.form.get("access") is not None        

            # Prepare the site data for insertion
            site_data = {
                "site_name": site_name,
                "deity": deity,
                "part_name": part_name,
                "description": description,
                "access": disabled_access,
                "created_by": session["user"]
            }

            # Insert the site data into the MongoDB collection
            mongo.db.locations.insert_one(site_data)
            flash("Site Successfully Added", "success")

            # Redirect to the browse sites page
            return redirect(url_for("browse_sites"))
        
        except Exception as e:
            # Handle any exceptions that occur
            flash(f"An error occurred while adding the site: {str(e)}", "error")
            return redirect(url_for("add_site"))

    # Fetch unique part names from the collection named 'part' for the dropdown in the add_site form
    part_names = mongo.db.part.distinct('part_name')
    return render_template("add_site.html", part_names=part_names)


@app.route("/edit_site/<locations_id>", methods=["GET", "POST"])
def edit_site(locations_id):
    if request.method == "POST":
        try:
            # Retrieve form data
            site_name = request.form.get("site_name")
            deity = request.form.get("deity")
            part_name = request.form.get("part_name")
            description = request.form.get("description")

            # Check if the 'access' checkbox is ticked
            disabled_access = request.form.get("access") is not None        

            # Prepare the site data for update
            site_data = {
                "site_name": site_name,
                "deity": deity,
                "part_name": part_name,
                "description": description,
                "access": disabled_access,
                "created_by": session["user"]
            }

            # Update the site data in the MongoDB collection
            mongo.db.locations.update_one({"_id": ObjectId(locations_id)}, {"$set": site_data})
            flash("Site Information Sucessfully Updated!", "success")

            # Redirect to the browse sites page or another relevant page
            return redirect(url_for("browse_sites"))

        except Exception as e:
            # Handle any exceptions that occur
            flash(f"An error occurred while updating the site: {str(e)}", "error")
            return redirect(url_for("edit_site", locations_id=locations_id))

    # If GET request, render the edit site form with existing data
    locations = mongo.db.locations.find_one({"_id": ObjectId(locations_id)})
    direction = mongo.db.part.find().sort("part_name", 1)
    return render_template("edit_site.html", locations=locations, part=direction)


@app.route("/delete_site/<locations_id>")
def delete_site(locations_id):
    mongo.db.locations.remove({"_id": ObjectId(locations_id)})
    flash("Site Data and Information Sucessfully Deleted!", "success")
    return redirect(url_for("browse_sites"))

# Logic developed, based on Functions module in 'Let us Python' by Y.Kanetkar and MongoDB Fundamentals by Amit Phaltankar.
@app.route('/filter_sites', methods=['GET', 'POST'])
def filter_sites():
    # Get filter parameters from request
    part_name = request.args.get('part_name')
    deity = request.args.get('deity')
    
    # Build the query dictionary based on filters
    query = {}
    if part_name:
        query['part_name'] = part_name
    if deity:
        query['deity'] = deity

    # Fetch filtered locations from the database
    locations = list(mongo.db.locations.find(query))
    
    # Fetch unique part names and deities for the filter form
    part_names = mongo.db.locations.distinct('part_name')
    deities = mongo.db.locations.distinct('deity')

    return render_template('browse_sites.html', locations=locations, part_names=part_names, deities=deities)


@app.route("/read_insights")
def read_insights():
    reviews = mongo.db.reviews.find()
    return render_template("read_insights.html", reviews=reviews)
    

@app.route("/add_insights", methods=["GET", "POST"])
def add_insights():
    if request.method == "POST":
        created_by = session.get("user")  # Get the current user's username
        review_data = {
            "where": request.form.get("where"),
            "rating": request.form.get("rating"),
            "visit_date": datetime.strptime(request.form.get("visit_date"), '%d.%m.%Y'),
            "purpose": request.form.get("purpose"),
            "review_des": request.form.get("review_des"),
            "created_by": created_by
        }
        mongo.db.reviews.insert_one(review_data)
        flash("Review added successfully!", "success")
        return redirect(url_for("read_insights"))
    return render_template("add_insights.html")

@app.route("/edit_insights/<review_id>", methods=["GET", "POST"])
def edit_insights(review_id):
    if request.method == "POST":
        try:
            # Retrieve form data
            where = request.form.get("where")
            rating = request.form.get("rating")
            visit_date = datetime.strptime(request.form.get("visit_date"), '%d.%m.%Y')
            purpose = request.form.get("purpose")
            review_des = request.form.get("review_des")

            # Prepare the review data for update
            review_data = {
                "where": where,
                "rating": rating,
                "visit_date": visit_date,
                "purpose": purpose,
                "review_des": review_des,
                "created_by": session["user"]
            }

            # Update the review data in the MongoDB collection
            mongo.db.reviews.update_one({"_id": ObjectId(review_id)}, {"$set": review_data})
            flash("Review successfully updated!", "success")

            # Redirect to the insights page or another relevant page
            return redirect(url_for("read_insights"))

        except Exception as e:
            # Handle any exceptions that occur
            flash(f"An error occurred while updating the review: {str(e)}", "error")
            return redirect(url_for("edit_insights", review_id=review_id))

    # If GET request, render the edit insights form with existing data
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template("edit_insights.html", review=review)


@app.route("/delete_insights/<review_id>")
def delete_insights(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Sucessfully Deleted!", "success")
    return redirect(url_for("read_insights"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
