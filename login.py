
from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
from database import get_db

login_bp = Blueprint("login", __name__)


@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        with get_db() as connection:
            student = connection.execute(
                "SELECT * FROM students WHERE email = ?",
                (email,)
            ).fetchone()

        if student and check_password_hash(student["password"], password):
            session["student_id"] = student["id"]
            return redirect(url_for("login.dashboard"))

        return "Invalid email or password", 401

    return render_template("login.html")


@login_bp.route("/dashboard")
def dashboard():
    if "student_id" not in session:
        return redirect(url_for("login.login"))

    with get_db() as connection:
        student = connection.execute(
            "SELECT id, name, email, department FROM students WHERE id = ?",
            (session["student_id"],)
        ).fetchone()

    if student is None:
        session.clear()
        return redirect(url_for("login.login"))

    return render_template("students.html", students=[student])


@login_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login.login"))
