import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, jsonify
)
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


# Custom filter to format datetime for HTML date input
@app.template_filter("date")
def format_date(value, format="%Y-%m-%d"):
    """Convert datetime object to string in the specified format."""
    if value is None:
        return ""
    return value.strftime(format)


@app.route("/")
@app.route("/get_locations")
def get_locations():
    locations = list(mongo.db.locations.find())
    return render_template("home.html", locations=locations)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        existing_user = mongo.db.user.find_one({"username": username.lower()})
        if existing_user:
            flash("Username already exists", "error")
            return redirect(url_for("register"))

        if password != confirm_password:
            flash("Passwords do not match", "error")
            return redirect(url_for("register"))

        password_hash = generate_password_hash(password)
        register = {"username": username.lower(), "password": password_hash}
        mongo.db.user.insert_one(register)

        session["user"] = username.lower()
        flash("Registration Successful!", "success")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    if "user" in session:
        username = mongo.db.user.find_one({"username": session["user"]})["username"]
        return render_template("home.html", username=username)
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user and check_password_hash(
                existing_user["password"], request.form.get("password")):
            session["user"] = request.form.get("username").lower()
            flash(f"You are successfully logged in as {session['user']}", "success")
            return redirect(url_for("profile", username=session["user"]))
        else:
            flash("Incorrect Username and/or Password", "error")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You have been signed out", "success")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/browse_sites")
def browse_sites():
    locations = list(mongo.db.locations.find())
    return render_template("browse_sites.html", locations=locations)


@app.route("/add_site", methods=["GET", "POST"])
def add_site():
    if "user" not in session:
        flash("Please log in to add a site", "error")
        return redirect(url_for("login"))

    if request.method == "POST":
        site_data = {
            "site_name": request.form.get("site_name"),
            "deity": request.form.get("deity"),
            "part_name": request.form.get("part_name"),
            "description": request.form.get("description"),
            "access": request.form.get("access") is not None,
            "created_by": session["user"]
        }
        mongo.db.locations.insert_one(site_data)
        flash("Site Successfully Added", "success")
        return redirect(url_for("browse_sites"))

    part_names = mongo.db.part.distinct('part_name')
    return render_template("add_site.html", part_names=part_names)


@app.route("/edit_site/<locations_id>", methods=["GET", "POST"])
def edit_site(locations_id):
    if request.method == "POST":
        site_name = request.form.get("site_name")
        deity = request.form.get("deity")
        part_name = request.form.get("part_name")
        description = request.form.get("description")
        disabled_access = request.form.get("access") is not None

        if not all([site_name, deity, part_name, description]):
            flash("All fields are required.", "error")
            return redirect(url_for("edit_site", locations_id=locations_id))

        site_data = {
            "site_name": site_name,
            "deity": deity,
            "part_name": part_name,
            "description": description,
            "access": disabled_access,
            "created_by": session["user"]
        }
        mongo.db.locations.update_one({"_id": ObjectId(locations_id)}, {"$set": site_data})
        flash("Site Information Successfully Updated!", "success")
        return redirect(url_for("browse_sites"))

    locations = mongo.db.locations.find_one({"_id": ObjectId(locations_id)})
    part_names = mongo.db.part.distinct("part_name")
    return render_template("edit_site.html", locations=locations, part=part_names)


@app.route("/delete_site/<locations_id>")
def delete_site(locations_id):
    try:
        # Attempt to delete the site using its ObjectId
        result = mongo.db.locations.delete_one({"_id": ObjectId(locations_id)})
        if result.deleted_count == 0:
            flash("No site found with the given ID.", "error")
        else:
            flash("Site Data and Information Successfully Deleted!", "success")
    except Exception as e:
        # Handle invalid ID or other unexpected errors
        flash(f"An error occurred while deleting the site: {str(e)}", "error")
    return redirect(url_for("browse_sites"))


@app.route('/get_part_names', methods=['GET'])
def get_part_names():
    """Return a JSON list of distinct 'Part of India' values."""
    part_names = mongo.db.locations.distinct('part_name')  # Fetch unique parts of India
    return jsonify(part_names)


@app.route('/filter_sites', methods=['GET', 'POST'])
def filter_sites():
    # Get filter parameters from request
    part_name = request.args.get('part_name')  # Part name filter
    deity = request.args.get('deity')  # Deity filter (free-text)

    # Build the query dictionary dynamically
    query = {}
    if part_name:
        query['part_name'] = part_name
    if deity:
        # Perform case-insensitive partial match using regex
        query['deity'] = {"$regex": deity, "$options": "i"}

    # Fetch filtered locations from the database
    locations = list(mongo.db.locations.find(query))

    # Fetch unique part names for the dropdown
    part_names = mongo.db.locations.distinct('part_name')

    # Render the browse_sites.html template with filtered data
    return render_template(
        'browse_sites.html',
        locations=locations,
        part_names=part_names
    )


@app.route("/read_insights")
def read_insights():
    reviews = list(mongo.db.reviews.find())
    return render_template("read_insights.html", reviews=reviews)


@app.route("/add_insights", methods=["GET", "POST"])
def add_insights():
    # Ensure the user is logged in
    if "user" not in session:
        flash("Please log in to add insights", "error")
        return redirect(url_for("login"))

    if request.method == "POST":
        try:
            # Retrieve and validate form inputs
            where = request.form.get("where")
            rating = request.form.get("rating")
            visit_date = request.form.get("visit_date")  # Expect 'YYYY-MM-DD' format from the date picker
            purpose = request.form.get("purpose")
            review_des = request.form.get("review_des")

            # Ensure all fields are provided
            if not all([where, rating, visit_date, purpose, review_des]):
                flash("All fields are required.", "error")
                return redirect(url_for("add_insights"))

            # Convert visit_date to a datetime object for MongoDB
            visit_date_obj = datetime.strptime(visit_date, "%Y-%m-%d")

            # Prepare review data for insertion
            review_data = {
                "where": where,
                "rating": rating,
                "visit_date": visit_date_obj,
                "purpose": purpose,
                "review_des": review_des,
                "created_by": session["user"]
            }

            # Insert review into the database
            mongo.db.reviews.insert_one(review_data)
            flash("Review added successfully!", "success")
            return redirect(url_for("read_insights"))

        except Exception as e:
            # Handle unexpected errors
            flash(f"An error occurred while adding the review: {str(e)}", "error")
            return redirect(url_for("add_insights"))

    # Render the add insights form for GET request
    return render_template("add_insights.html")


@app.route("/edit_insights/<review_id>", methods=["GET", "POST"])
def edit_insights(review_id):
    if request.method == "POST":
        # Retrieve form data
        where = request.form.get("where")
        rating = request.form.get("rating")
        visit_date = request.form.get("visit_date")  # Expect 'YYYY-MM-DD' format
        purpose = request.form.get("purpose")
        review_des = request.form.get("review_des")

        # Validate all fields
        if not all([where, rating, visit_date, purpose, review_des]):
            flash("All fields are required.", "error")
            return redirect(url_for("edit_insights", review_id=review_id))

        try:
            # Convert visit_date to datetime object for MongoDB
            visit_date_obj = datetime.strptime(visit_date, "%Y-%m-%d")

            # Update the review in MongoDB
            review_data = {
                "where": where,
                "rating": rating,
                "visit_date": visit_date_obj,  # Store as a datetime object
                "purpose": purpose,
                "review_des": review_des,
                "created_by": session["user"]
            }
            mongo.db.reviews.update_one({"_id": ObjectId(review_id)}, {"$set": review_data})
            flash("Review successfully updated!", "success")
            return redirect(url_for("read_insights"))

        except Exception as e:
            flash(f"An error occurred: {str(e)}", "error")
            return redirect(url_for("edit_insights", review_id=review_id))

    # Handle GET request: Fetch existing review data
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    if not review:
        flash("Review not found.", "error")
        return redirect(url_for("read_insights"))

    # Convert visit_date to string for pre-filling the form
    if "visit_date" in review and isinstance(review["visit_date"], datetime):
        review["visit_date"] = review["visit_date"].strftime("%Y-%m-%d")

    return render_template("edit_insights.html", review=review)


@app.route("/delete_insights/<review_id>")
def delete_insights(review_id):
    try:
        # Attempt to delete the review using its ObjectId
        result = mongo.db.reviews.delete_one({"_id": ObjectId(review_id)})
        if result.deleted_count == 0:
            flash("No review found with the given ID.", "error")
        else:
            flash("Review Successfully Deleted!", "success")
    except Exception as e:
        # Handle invalid ID or other unexpected errors
        flash(f"An error occurred while deleting the review: {str(e)}", "error")
    return redirect(url_for("read_insights"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)