from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.user import User
from app import db

pages_bp = Blueprint('pages', __name__)


@pages_bp.route("/")
def index():
    username = session.get("user_id")
    return render_template("index.html", username=username)
