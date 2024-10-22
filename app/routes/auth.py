from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    error_message = ""
    
    if session.get("user_id") != "None":
        return redirect("/home")
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        get_user_with_username = User.query.filter_by(username=username).first()
        
        if get_user_with_username:
            if check_password_hash(get_user_with_username.password, password):
                session["user_id"] = get_user_with_username.username
                return redirect("/home")
            else:
                error_message = "Invalid username or password."
        else:
            error_message = "Invalid username or password."
            
    return render_template("login.html", error_message=error_message)


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    error_message = ""


    if session.get("user_id") != "None":
        return redirect("/home")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Check username length
        if len(username) > 16:
            error_message = "Username over 16 characters."
            return render_template("signup.html", error_message=error_message)

        # Check if username is taken
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            error_message = "Username already taken. Please choose a different one."
            return render_template("signup.html", error_message=error_message)

        # Hash the password before saving it to the database
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        session["user_id"] = username
        return redirect('/home')  # Redirect to login or another page

    return render_template("signup.html", error_message=error_message)
