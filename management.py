
from flask import Blueprint, render_template, request, redirect, url_for, session
from database import get_db

management_bp = Blueprint("management", __name__)


@management_bp.route("/students")
def students():
    if "student_id" not in session:
        return redirect("/login")

    with get_db() as connection:
        records = connection.execute(
            "SELECT id, name, email, department FROM students"
        ).fetchall()

    return render_template("students.html", students=records)


@management_bp.route("/update/<int:student_id>", methods=["GET", "POST"])
def update_student(student_id):
    if "student_id" not in session:
        return redirect("/login")

    with get_db() as connection:
        student = connection.execute(
            "SELECT id, name, email, department FROM students WHERE id = ?",
            (student_id,)
        ).fetchone()

        if student is None:
            return "Student not found", 404

        if request.method == "POST":
            name = request.form.get("name", "").strip()
            email = request.form.get("email", "").strip()
            department = request.form.get("department", "").strip()

            if not all([name, email, department]):
                return "All fields are required", 400

            connection.execute(
                """UPDATE students
                   SET name = ?, email = ?, department = ?
                   WHERE id = ?""",
                (name, email, department, student_id)
            )

            return redirect(url_for("management.students"))

    return render_template("update.html", student=student)


@management_bp.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    if "student_id" not in session:
        return redirect("/login")

    with get_db() as connection:
        connection.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

    if session["student_id"] == student_id:
        session.clear()

    return redirect(url_for("management.students"))
