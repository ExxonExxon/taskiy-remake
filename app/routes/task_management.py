from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app.models.task import Task
from app import db

task_management_bp = Blueprint('task_management', __name__)

# @task_management_bp.route("/add_task")
    