
from flask import Flask, render_template
from database import init_db
from registration import registration_bp

app = Flask(__name__)

app.register_blueprint(registration_bp)

@app.route("/")
def home():
    return render_template("index.html")

init_db()

if __name__ == "__main__":
    app.run(debug=True)
