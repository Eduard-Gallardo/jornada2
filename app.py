from flask import Flask, render_template, url_for
from routes.login import login_bp

app = Flask(__name__)

app.register_blueprint(login_bp)

@app.route('/')
def index():
    return render_template('index.html')