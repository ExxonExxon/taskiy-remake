from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app.models.task import Task
from app import db

home_bp = Blueprint('home', __name__)

@home_bp.route("/home", methods=["GET", "POST"])
def home():
    username: str = session.get("user_id")
    
    # Get all the tasks
    
    if not username:
        redirect(url_for("login"))
    
    tasks = Task.query.filter_by(username=username).all()
    
    return render_template("home.html", username=username, tasks=tasks)