import os
from flask import Flask, render_template, request, jsonify
from database import init_db, get_db
from registration import registration_bp
from login import login_bp
from management import management_bp

app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY", "classroom-demo-only-secret"
)

# Register existing application modules
app.register_blueprint(registration_bp)
app.register_blueprint(login_bp)
app.register_blueprint(management_bp)


@app.route("/")
def home():
    return render_template("index.html")


# Student search feature for Week-8(b)
@app.route("/search")
def search_student():
    name = request.args.get("name", "").strip()

    with get_db() as con:
        students = con.execute(
            """
            SELECT id, name, department
            FROM students
            WHERE name LIKE ?
            """,
            ("%" + name + "%",)
        ).fetchall()

    return jsonify([dict(student) for student in students])


# Initialize the database
init_db()


if __name__ == "__main__":
    app.run(debug=True)