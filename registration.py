
from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from database import get_db
import sqlite3

registration_bp = Blueprint("registration", __name__)


@registration_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        department = request.form.get("department", "").strip()

        if not all([name, email, password, department]):
            return "All fields are required", 400

        try:
            with get_db() as connection:
                connection.execute("""
                    INSERT INTO students (name, email, password, department)
                    VALUES (?, ?, ?, ?)
                """, (
                    name,
                    email,
                    generate_password_hash(password),
                    department
                ))

        except sqlite3.IntegrityError:
            return "Email already registered", 409

        return redirect(url_for("registration.registered"))

    return render_template("register.html")


@registration_bp.route("/registered")
def registered():
    return """
        <h2>Student registered successfully!</h2>
        <a href="/">Go Home</a>
    """
