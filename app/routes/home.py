from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app import db

home_bp = Blueprint('home', __name__)

@home_bp.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")